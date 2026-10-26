# Microservicios Python con Clean Architecture (curso de Janner)

Fuentes: repo github.com/Janner-GP/ecommerce_microservices y las presentaciones del curso "Arquitectura de software: diseñar para evolucionar" y "Clean Architecture en la práctica" (sesión 2).

## 1. Ideas del curso

La arquitectura define responsabilidades, límites, dependencias y canales de comunicación. No es solo carpetas.

Hay tres decisiones distintas, cada una con sus compromisos:
- Arquitectura del sistema: monolito (simple, menor latencia; escala solo vertical y se despliega entero), monolito modular (límites lógicos, menos complejo que microservicios), microservicios (despliegue independiente y datos propios; cuesta latencia de red, observabilidad distribuida y operación), orientada a eventos (desacople y escalado por consumidor; cuesta consistencia y manejo de eventos). El curso usa microservicios para enseñar límites, fallos distribuidos y despliegue independiente, sabiendo lo que cuesta.
- Arquitectura interna: entre Layered, Hexagonal, Vertical Slice y Clean, el curso usa Clean Architecture dentro de cada servicio.
- Estilo de API: REST (FastAPI) para la interfaz principal; RPC para acciones explícitas; GraphQL añade complejidad en caché y permisos; gRPC para comunicación interna de alto rendimiento. Son estilos de interfaz, no arquitecturas completas. El curso usa REST con FastAPI y RabbitMQ para mensajería asíncrona.

Recorrido de una solicitud: Cliente → Endpoint (Presentation) → Caso de uso (Application) → Dominio (Domain) → Persistencia (Infrastructure).

Regla de dependencias: Presentation → Application → Domain. Infrastructure implementa los contratos que define Domain/Application. El dominio no conoce FastAPI, SQLModel ni RabbitMQ.

Límites de microservicios:
- Una responsabilidad de negocio por servicio.
- Cada servicio es dueño exclusivo de sus datos.
- No compartir modelos ORM entre servicios.
- Comunicación por contratos explícitos.
- No crear un servicio por cada tabla.

Comunicación: síncrona por HTTP/REST cuando se necesita respuesta inmediata (riesgo: acoplamiento temporal y latencia); asíncrona por eventos en RabbitMQ para notificaciones y procesos desacoplados (no garantiza entrega exactamente una vez sin diseño adicional). Ejemplo: orders-service publica OrderConfirmed y notifications-service envía el correo.

La buena arquitectura no consiste en cambiar de tecnología sin tocar nada; consiste en evitar que un cambio técnico obligue a reescribir la lógica de negocio.

Cuándo es sobreingeniería:
- Dos adaptadores sin necesidad real: si el proyecto solo usará SQLModel, mantener psycopg activo añade complejidad sin beneficio.
- Interfaces para un único repositorio: un CRUD pequeño que funciona con SQLModel no necesita una jerarquía ABC completa.
- `to_domain` que crece sin control indica un problema en el diseño de entidades.
- Cada abstracción (interfaz, factory, clase genérica) tiene que justificar su coste.

Temas siguientes del curso: patrones de diseño, testing y SonarQube, ciberseguridad, idempotencia, rate limiting y resiliencia, mensajería y consistencia, observabilidad y Docker, CI/CD y GHCR, despliegue en AWS ECS con Fargate.

## 2. Estructura de cada servicio

Cada servicio es un proyecto uv independiente (`pyproject.toml`, `.python-version`, `alembic/`, `tests/`, `README.md`, `.env.example`):

```
app/src/
├── domain/
│   ├── entities/        clases normales de Python, sin ORM (lo que conoce el caso de uso)
│   ├── models/          tablas SQLModel (las usa Alembic y el adaptador SQLModel)
│   ├── repositories/    contrato: class XRepository(ABC) con @abstractmethod
│   └── exceptions.py    errores de negocio: class XNotFoundError(Exception)
├── application/use_cases/   una clase por caso de uso con __init__(repo) y execute()
├── infrastructure/
│   ├── database/        get_session (SQLModel) y get_connection (psycopg)
│   └── repositories/    sqlmodel_x_repository.py y postgres_x_repository.py
├── presentation/
│   ├── dependencies.py  punto de composición: el único lugar que elige el adaptador
│   ├── schemas/         contrato HTTP en Pydantic (XCreate, XResponse)
│   └── routers/         APIRouter(prefix="/xs", tags=["xs"])
├── shared/              config.py, utils/date.py (utc_now)
└── main.py              FastAPI(title="x-service") + include_router
```

Servicios del ecommerce: user (8001, `usr_`), catalog (8002, `cat_`), order (8003, `ord_`), payment (8004, `pym_`), notification (8005, `ntf_`).

## 3. Patrones concretos

Contrato sin ORM:

```python
class ProductRepository(ABC):
    @abstractmethod
    def get_by_sku(self, sku: str) -> Product | None: ...

    @abstractmethod
    def create(self, product: Product) -> Product: ...
```

Caso de uso que solo conoce el contrato:

```python
class CreateProduct:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def execute(self, product: Product) -> Product:
        if self.product_repository.get_by_sku(product.sku) is not None:
            raise ProductAlreadyExistsError(product.sku)
        return self.product_repository.create(product)
```

La comprobación previa no reemplaza una restricción UNIQUE en PostgreSQL: dos peticiones concurrentes pueden pasar la validación a la vez.

Transacciones con un solo responsable: `get_session()` / `get_connection()` abren una sesión o conexión por petición y son el único sitio que hace commit, rollback y close. Los repositorios hacen `flush()` (envía el cambio sin confirmarlo), nunca `commit()`.

```python
def get_session():
    session = Session(engine)
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
```

Punto de composición en `presentation/dependencies.py`: `Depends(get_session, scope="function")` para que el commit ocurra antes de enviar la respuesta; el adaptador se elige una vez al arrancar con `PERSISTENCE_ADAPTER` (`sqlmodel` | `postgres`) del `.env`; factories `get_create_product(repo=Depends(get_product_repository))`.

Router delgado: construye la entidad desde el schema, llama `use_case.execute()`, traduce excepciones de dominio a HTTPException (409 duplicado, 404 no existe) y convierte la entidad con `to_response()`. Nunca SQL ni reglas de negocio.

SQL directo con psycopg 3: siempre parámetros `%s` con tupla, nunca interpolar datos del usuario; `RETURNING` para devolver la fila; mapeo manual fila → entidad. SQLAlchemy usa `postgresql+psycopg://`, psycopg usa `postgresql://`; se convierte con `replace` en cada módulo de conexión.

Tipos: dinero con `Decimal` (`max_digits=12, decimal_places=2`), ids `uuid.UUID` con `default_factory=uuid.uuid4`, fechas con `utc_now()`.

## 4. Alembic por servicio

- Tablas siempre con el prefijo del servicio y el modelo importado en `alembic/env.py`.
- `include_name` filtra para que el autogenerate solo compare las tablas del prefijo propio y no proponga borrar las de otros servicios.
- Cada servicio guarda su versión en su propia tabla (`version_table="cat_alembic_version"`).
- Entre servicios no hay foreign keys: una orden guarda `user_id` y `product_id` como identificadores.
- `uv run alembic revision --autogenerate -m "Agregar campo X a ord_orders"`, revisar el archivo generado y luego `uv run alembic upgrade head`. Nunca editar una migración ya aplicada: crear una nueva.

Nota: el repo comparte una sola base PostgreSQL entre los cinco servicios separados por prefijo. Es un atajo práctico del taller; el principio del curso es que cada servicio sea dueño exclusivo de sus datos, así que en producción lo correcto es una base (o al menos un esquema y un usuario) por servicio.

## 5. Pruebas

- `tests/test_create_x.py`: el caso de uso se prueba sin base de datos con un `InMemoryXRepository(XRepository)` basado en una lista.
- `tests/test_x_repositories.py`: la misma función de prueba se ejecuta con los dos adaptadores; se salta con `pytest.mark.skipif` si no existe `TEST_DATABASE_URL` y termina con rollback para no dejar datos.
- `[tool.pytest.ini_options] pythonpath = ["."]` y pytest en `[dependency-groups] dev`.
- Al agregar un método al contrato, todas las implementaciones deben tenerlo (los dos adaptadores y el repositorio en memoria) o Python lanza `TypeError: Can't instantiate abstract class`.
- Nombres de prueba en español que describen la regla: `test_rechaza_sku_repetido`, `test_no_cancela_orden_pagada`.

## 6. Cómo crear un feature (de adentro hacia afuera)

0. ¿Cambia la base de datos? Si sí: campo en `domain/entities/` y en `domain/models/`, y migración.
1. domain: excepción de negocio, entidad y método nuevo en el contrato.
2. application: el caso de uso con la regla de negocio.
3. tests: prueba del caso de uso con el repositorio en memoria (`uv run pytest` debe pasar sin base de datos).
4. infrastructure: el método en los dos adaptadores (flush, sin commit).
5. presentation: dependencia en `dependencies.py`, schema y endpoint.

Dónde va cada cosa:

| Si necesitas… | Va en… |
|---|---|
| Una regla de negocio ("solo se cancela si está pendiente") | `application/use_cases/` |
| Un error de negocio | `domain/exceptions.py` |
| Una operación nueva con la base | método en `domain/repositories/` + los dos adaptadores |
| Un campo o tabla nueva | `domain/entities/`, `domain/models/` y una migración |
| Una consulta SQL o de SQLModel | solo en `infrastructure/repositories/` |
| Validar formato de la petición | `presentation/schemas/` |
| Convertir errores en códigos HTTP | `presentation/routers/` |
