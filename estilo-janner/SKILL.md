---
name: estilo-janner
description: Patrones de arquitectura, stack y convenciones del Tech Lead Janner Gonzalez (github.com/Janner-GP) y de su curso de arquitectura de software (Clean Architecture, microservicios), sacados de sus repos ecommerce_microservices, taskflow, infinivirt-tickets, fastapi_app, custodio-riwi, data-platform y vida_api_express. Usar al crear o ampliar un microservicio o API FastAPI + SQLModel/psycopg, un backend NestJS + Prisma, un frontend Angular/Ionic, un cluster Airflow + Celery + RabbitMQ, un pipeline de CI, o al decidir arquitectura (monolito vs microservicios, REST vs eventos) o escribir el README/docs de un proyecto.
---

# Estilo Janner

Esta skill dice QUÉ forma tiene el código (carpetas, capas, nombres, convenciones).
ponytail sigue decidiendo CUÁNTO código escribir: la solución más pequeña que resuelva todo.
Si las dos chocan, gana ponytail en scripts y ejercicios cortos, y gana esta skill en proyectos con varios módulos o que se van a desplegar.

Antes de imponer un patrón, mira el repo actual. Si ya tiene su propia estructura, síguela; esta skill es la referencia cuando el proyecto empieza o cuando ya usa estos patrones.

## 1. Backend NestJS: arquitectura hexagonal (taskflow, infinivirt-tickets)

Cada módulo vive en `src/modules/<modulo>/` con cuatro capas:

```
domain/          entidades, value objects (*.vo.ts), errores (*.errors.ts), puertos (*.port.ts)
application/     un caso de uso por archivo: <verbo>-<cosa>.use-case.ts con un método execute()
infrastructure/  adaptadores: prisma-<cosa>.repository.ts, <cosa>.mapper.ts, servicios JWT/bcrypt/S3
presentation/    <cosas>.controller.ts, <cosa>.dto.ts, guards, decorators
<modulo>.module.ts  el único lugar donde se conecta puerto ↔ implementación
```

Lo compartido va en `src/shared/{domain,infrastructure,presentation}` (DomainError, PrismaService, config, S3, filtros, interceptores, health).

Reglas que no se rompen:

1. El dominio no importa nada de `@nestjs/*` ni de `@prisma/*`. Si lo hace, está en la capa equivocada.
2. Prisma nunca sale de `infrastructure/`. Los casos de uso dependen del puerto, no de PrismaClient.
3. Los casos de uso inyectan interfaces con un token `Symbol` exportado desde el puerto: `export const TASK_REPOSITORY = Symbol('TaskRepositoryPort')` y `@Inject(TASK_REPOSITORY) private readonly tasks: TaskRepositoryPort`.
4. El puerto expone solo lo que los casos de uso necesitan (`findByIdAndUserId`, `listByUser`), nunca un `findMany({ where })` genérico.
5. Un mapper estático (`TaskMapper.toDomain(record)`) convierte el registro de Prisma en entidad de dominio.
6. Los DTOs viven solo en `presentation/`. El caso de uso devuelve entidades; el controller las convierte con `TaskDto.from(entity)`.
7. La autorización es una regla de dominio, no un `if` en el controller: `task.assertOwnedBy(userId)`.
8. Recurso de otro usuario: responder 404, nunca 403 (el 403 confirma que existe).

Errores:

- `abstract class DomainError extends Error` con `code` estable en SNAKE_CASE mayúsculas (`TASK_NOT_FOUND`, `DUPLICATE_TAG_NAME`) y `details` opcional. El dominio no conoce códigos HTTP.
- El mapa `code → status` vive en `shared/presentation/errors/error-catalog.ts`, y un `AllExceptionsFilter` global lo aplica.
- Cuerpo de error uniforme: `{ statusCode, code, message, details?, timestamp, path }`.
- Respuestas de éxito marcadas con `@ResponseMessage('clave.i18n')` salen como `{ data, message }` por un interceptor. Los textos al usuario se traducen con nestjs-i18n (`src/i18n/es|en/messages.json`), nunca strings sueltos.

Configuración:

- Las variables de entorno se validan con Zod al arrancar (`shared/infrastructure/config/env.schema.ts`). Ese schema es la única fuente de verdad, cada variable va comentada y documentada en `.env.example`.
- Booleanos como `z.enum(['true','false'])`, números con `z.coerce.number()`, secretos con `min(32)`.

Prisma:

- Schema partido en un archivo por modelo: `prisma/schema/<Modelo>.prisma`, más `enums.prisma` y `schema.prisma`.
- `id String @id @default(uuid()) @db.Uuid`, `createdAt @default(now())`, `updatedAt @updatedAt`.
- Tablas con prefijo del proyecto vía `@@map("tsf_tasks")`. Índices compuestos que empiezan por `userId` para los filtros reales.
- Restricciones también en la BD (`@@unique([userId, name])`) aunque el caso de uso ya las valide.
- `npx prisma migrate dev --name <cambio>` en local, `prisma migrate deploy` en producción, y un `seed.ts`.

Seguridad que repite en sus proyectos: JWT con access de 15 min y refresh de 7 días con rotación y revocación en cascada si se detecta reuso; cookies httpOnly en web y Bearer en mobile, como dos adaptadores del mismo caso de uso; CSRF double-submit; CORS con lista de orígenes, nunca `*`; rate limiting en `/auth/*`; bcrypt con 12 rounds; Swagger en `/api/docs` apagado en producción.

Formato: Prettier con `singleQuote: true` y `trailingComma: "all"`. Imports con alias `@/`.

## 2. Frontend Angular / Ionic (taskflow web y mobile, custodio-riwi)

- Angular 21 standalone, zoneless, TypeScript estricto. Estado con NgRx Signals Store. PrimeNG en web, Ionic 8 + Capacitor en mobile.
- `src/app/core/` para guards, interceptors (auth, refresh, error), i18n y storage.
- `src/app/features/<feature>/{domain,application,infrastructure,presentation,state}`: el puerto del repositorio en domain, el adaptador HTTP en infrastructure (`http-task-repository.ts`), páginas en presentation (`tasks.page.ts`), store en state.
- Lo nativo (cámara, biometría, notificaciones) va detrás de un puerto con dos adaptadores: `capacitor-*.adapter.ts` y `noop-*.adapter.ts` para el navegador.
- Pruebas con Vitest. Proxy de desarrollo en `proxy.conf.json`; en producción, nginx.

## 3. Python / FastAPI

### 3.1 Servicios con varias reglas de negocio o microservicios (ecommerce_microservices)

Es su referencia actual para Python y la del curso de arquitectura. Clean Architecture dentro de cada servicio: `app/src/{domain,application,infrastructure,presentation,shared}`, entidades sin ORM separadas de los modelos SQLModel, contrato `ABC`, casos de uso con `execute()`, commit solo en `get_session`/`get_connection`, adaptador elegido en `presentation/dependencies.py`, tablas con prefijo por servicio y pruebas del caso de uso con un repositorio en memoria.

Antes de crear o ampliar un servicio así, lee `references/microservicios-python.md` (estructura completa, código de ejemplo, Alembic por servicio, pruebas, guía para crear un feature y cuándo es sobreingeniería).

### 3.2 APIs pequeñas o ejercicios (fastapi_app, custodio-riwi)

Un CRUD pequeño no necesita contrato ABC ni dos adaptadores (lo dice el propio curso). Para eso:

- Proyecto con uv: `pyproject.toml`, `.python-version`, `requires-python = ">=3.12"`.
- Estructura: `main.py` en la raíz o `app/main.py`; modelos en `src/models/<cosa>_model.py`; sesión en `src/shared/database/session_db.py`.
- Sesión como dependencia: `get_session()` con `yield` y `SessionDep = Annotated[Session, Depends(get_session)]`.
- SQLModel con `table=True`, `__tablename__` con prefijo (`app_inv_products`), enums `class X(str, Enum)`.
- Migraciones con Alembic usando `target_metadata = SQLModel.metadata` e importando los modelos en `alembic/env.py`.
- Config con `pydantic-settings` (`class Settings(BaseSettings)` + `settings = Settings()`), nunca `os.getenv` regado por el código.
- Esquemas de entrada separados (`schemas.py`, `CreateProduct(BaseModel)`) del modelo de tabla.
- Errores con `HTTPException`: 409 para duplicados, 422 para reglas de negocio, 404 si no existe.

## 4. Datos: Airflow + Celery + RabbitMQ (data-platform)

- Carpetas separadas por nodo: `master/` (scheduler, webserver, init de la BD), `worker/` (N workers), `rabbitmq/`, `nginx-proxy-manager/`, cada una con su `docker-compose.yml` y su `.env.template`.
- `AIRFLOW__CORE__EXECUTOR=CeleryExecutor`, PostgreSQL como metadata DB y RabbitMQ como broker. Workers con las mismas credenciales que el master.
- `pipelines/dags/<pipeline>.py` define el DAG con `@dag(dag_id=..., schedule=None, catchup=False, tags=[...])` y encadena `extraer() >> transformar() >> cargar()`.
- La lógica de cada paso va en `pipelines/tasks/<pipeline>/task1.py` con `@task`, separada del DAG.
- Cargas en lote (executemany / `to_sql`) en vez de fila por fila.

## 5. Docker, CI/CD y AWS

- `docker-compose.dev.yml` solo con la BD para desarrollo con hot reload; `docker-compose.yml` para el stack completo.
- GitHub Actions: `concurrency` por rama con `cancel-in-progress`, `permissions: contents: read`, primer job gitleaks con `.gitleaks.toml`, luego lint + build por app con Node 22 y `npm ci`.
- Deploy: imágenes a ECR con tag `sha-<commit>`, ECS Fargate detrás de un ALB (`/api/*` al backend, `/*` al web), RDS en subred privada, S3 para archivos.
- Secretos: GitHub Secrets → Secrets Manager → campo `secrets` de la task definition. Nunca en `environment`.
- Script de infraestructura idempotente (`aws/setup.sh` y `setup.ps1` para Windows).

## 6. Documentación

README en español con índice numerado: 1 Descripción, 2 Arquitectura (diagrama ASCII + árbol de carpetas), 3 Tecnologías y justificación (tabla Tecnología | Motivo), 4 Cómo ejecutarlo, 5 Variables de entorno (tabla), 6 Despliegue, 7 Decisiones técnicas (cada una con su porqué), 8 Capturas, 9 Limitaciones conocidas.

Además, en `docs/`: `ARCHITECTURE.md`, `BUSINESS.md` (reglas de negocio), `FEATURE_GUIDE.md` (cómo añadir un módulo paso a paso con un ejemplo real) y `CONTRACT.md` (contrato de API compartido entre web y mobile).
Cada decisión técnica se escribe con el motivo, incluida la versión elegida y por qué no la siguiente.
Comentarios de código en español, explicando el porqué y no el qué.

## 7. Lo que NO se copia de sus repos

Algunos repos son material de clase y traen atajos que no deben repetirse:

- Credenciales escritas en el código (data-platform tiene usuario y contraseña de una BD en `task1.py`). Siempre `.env` + `.env.example`.
- Variables con nombres mezclados como `Database_url`; usar `DATABASE_URL`.
- Comparar con `== None`; usar `is None`.
- `run_migrations_online()` llamado dos veces en `alembic/env.py`; dejar solo el bloque `if context.is_offline_mode()`.
- `allow_methods=["*"]` y `allow_headers=["*"]` en CORS de producción.
- `.one()` sin manejar el caso de que no exista (lanza 500 en vez de 404).
