---
name: buenas-practicas
description: Buenas prácticas para empezar y mantener proyectos. Arranque de proyectos Python con uv (init, python pin, add, lock, sync, run), configuración de Ruff y pytest en pyproject.toml, estructura base del repo, .gitignore y .env.example, Git y commits, manejo de secretos, estilo de código, Docker con uv, CI con GitHub Actions, y equivalentes en Node/TypeScript. Usar al crear un proyecto o servicio nuevo, al agregar dependencias, al preparar un repo para entregar o desplegar, o cuando el usuario pida revisar si un proyecto sigue buenas prácticas.
---

# Buenas prácticas

Esta skill cubre CÓMO arrancar y mantener un proyecto sano. La forma interna del código (capas, carpetas) la da estilo-janner; cuánto código escribir lo decide ponytail; las versiones y comandos se confirman en la documentación oficial (source-driven-development).

Si el proyecto ya existe y tiene su propia convención, síguela y solo propone cambios donde haya un riesgo real (secretos expuestos, dependencias sin lock, sin pruebas).

## 1. Arrancar un proyecto Python con uv

Nunca `pip install` global, nunca `requirements.txt` escrito a mano y nunca un venv creado a mano. Todo pasa por uv.

```bash
uv init mi-servicio            # aplicación con layout src/ y build system (uv_build)
uv init --no-package mi-api    # API/servicio que no se instala como paquete: main.py en la raíz
cd mi-servicio
uv python pin 3.12             # crea/actualiza .python-version
uv add fastapi[standard] sqlmodel alembic "psycopg[binary]" pydantic-settings
uv add --dev pytest ruff       # quedan en [dependency-groups] dev
uv run pytest                  # uv run crea/sincroniza el .venv automáticamente
```

Reglas:
- Se versionan en Git `pyproject.toml`, `uv.lock` y `.python-version`. El `.venv` nunca.
- Las dependencias se agregan con `uv add` y se quitan con `uv remove`; no se edita `uv.lock` a mano.
- Después de clonar o de un pull: `uv sync`. En CI y Docker: `uv sync --locked` (falla si el lock no coincide con pyproject).
- Comandos siempre con `uv run` (`uv run fastapi dev app/src/main.py`, `uv run alembic upgrade head`) para usar el entorno del proyecto.
- Si otra herramienta exige un requirements.txt: `uv export --format requirements-txt > requirements.txt`, generado, nunca escrito a mano.
- Python 3.12 en los proyectos de Joshua (3.14 dio incompatibilidades).

## 2. pyproject.toml base

```toml
[dependency-groups]
dev = ["pytest", "ruff"]

[tool.ruff]
line-length = 88
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "B", "UP", "SIM"]   # pycodestyle, pyflakes, isort, bugbear, pyupgrade, simplify

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["."]
```

Antes de cada commit: `uv run ruff format .`, `uv run ruff check --fix .` y `uv run pytest`.

## 3. Estructura mínima de cualquier repo

```
README.md          qué es, cómo se ejecuta, variables de entorno, decisiones
.gitignore         .venv/, __pycache__/, *.py[oc], .env, dist/, build/, .pytest_cache/, .ruff_cache/, node_modules/
.env.example       todas las variables con un valor de ejemplo o vacío y un comentario
.python-version / .nvmrc
pyproject.toml + uv.lock   (o package.json + package-lock.json)
src/ o app/        código
tests/             pruebas
docs/              arquitectura, ADR, guía de features cuando el proyecto crece
```

El README responde siempre: qué hace, requisitos, cómo correrlo en local (comandos copiables), variables de entorno, cómo correr pruebas, cómo desplegar, limitaciones conocidas.

## 4. Configuración y secretos

- Toda configuración sale de variables de entorno, validada al arrancar: `pydantic-settings` en Python (`class Settings(BaseSettings)` + `settings = Settings()`), Zod en Node.
- `.env` está en `.gitignore`; `.env.example` sí se versiona y documenta cada variable.
- Nombres de variables en MAYÚSCULAS_CON_GUION_BAJO (`DATABASE_URL`, no `Database_url`).
- Nunca credenciales, IPs de servidores, tokens ni contraseñas en el código, en notebooks o en el README. Si alguna se subió, se considera filtrada: se cambia la contraseña, no basta con borrar el archivo.
- Gitleaks en CI (y opcionalmente como hook de pre-commit).
- CORS con lista de orígenes, nunca `*` si hay credenciales.

## 5. Git

- Rama principal protegida; trabajo en ramas `feature/<clave>`, `fix/<clave>`. En SonoraPlay: `main / develop / feature/EG-XX` y la clave de Jira en el commit.
- Commits pequeños que hacen una sola cosa, en imperativo. Si el proyecto no tiene convención propia, usar Conventional Commits: `feat: agrega cancelación de órdenes`, `fix: ...`, `docs: ...`, `refactor: ...`, `test: ...`, `chore: ...`.
- Nunca subir `.env`, `.venv`, `node_modules`, archivos de datos pesados ni credenciales.
- Pull request con descripción de qué cambia, por qué y cómo probarlo.

## 6. Estilo de código Python

- PEP 8 aplicado por `ruff format`; nombres descriptivos en `snake_case`, clases en `PascalCase`, constantes en `MAYUSCULAS`.
- Type hints en funciones públicas (`def execute(self, order_id: UUID) -> Order:`).
- `is None` / `is not None`, nunca `== None`.
- `logging` en vez de `print` en código de servidor.
- Excepciones específicas de negocio; nunca `except Exception: pass`.
- SQL siempre parametrizado (`%s` con tupla o el ORM); nunca f-strings con datos del usuario.
- Dinero con `Decimal`, fechas en UTC con zona horaria, rutas con `pathlib`.
- Comentarios que expliquen el porqué, no el qué.

## 7. Pruebas

- pytest con nombres que describen la regla (`test_rechaza_sku_repetido`).
- Estructura Arrange / Act / Assert.
- La lógica de negocio se prueba sin base de datos (repositorio en memoria); las pruebas contra la base se saltan si no hay `TEST_DATABASE_URL`.
- Cada bug se reproduce primero con una prueba que falla (ver test-driven-development).

## 8. Docker con uv

```dockerfile
FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:<version> /uv /uvx /bin/   # fijar una versión concreta de uv
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy UV_NO_DEV=1
WORKDIR /app

# Primero solo dependencias: esta capa se cachea mientras no cambie el lock
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

COPY . .
RUN --mount=type=cache,target=/root/.cache/uv uv sync --locked

RUN useradd --create-home app && chown -R app /app
USER app
CMD ["uv", "run", "fastapi", "run", "app/src/main.py", "--port", "8000"]
```

`.dockerignore` con `.venv`, `.env`, `.git`, `__pycache__`, `tests` si no se necesitan. Un `docker-compose.dev.yml` con solo la base de datos para desarrollo local.

## 9. CI con GitHub Actions (Python)

```yaml
name: CI
on: [push, pull_request]
concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true
permissions:
  contents: read
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v9      # fijar versión o SHA
      - run: uv sync --locked --all-extras --dev
      - run: uv run ruff format --check .
      - run: uv run ruff check .
      - run: uv run pytest
```

Más un job de gitleaks como primer paso, igual que en los repos de Janner.

## 10. Node / TypeScript

- Node 22 LTS fijado en `.nvmrc` y en `"engines"` del package.json.
- `npm ci` en CI y Docker (respeta el lock); `package-lock.json` siempre versionado.
- TypeScript con `"strict": true`.
- ESLint + Prettier (`singleQuote: true`, `trailingComma: "all"`), scripts `lint`, `format`, `test`, `build` en package.json.
- Variables de entorno validadas con Zod al arrancar.

## 11. Checklist antes de entregar o hacer push

1. `uv run ruff format .` y `uv run ruff check .` sin errores (o `npm run lint`).
2. `uv run pytest` en verde.
3. `uv.lock` / `package-lock.json` actualizados y versionados.
4. Ninguna credencial en el diff; `.env.example` al día con cualquier variable nueva.
5. README actualizado si cambió cómo se ejecuta o configura.
6. Migraciones nuevas revisadas antes de aplicarlas; nunca editar una ya aplicada.

## Fuentes oficiales

- uv, proyectos: https://docs.astral.sh/uv/concepts/projects/init/
- uv con Docker: https://docs.astral.sh/uv/guides/integration/docker/
- uv con GitHub Actions: https://docs.astral.sh/uv/guides/integration/github/
- Ruff: https://docs.astral.sh/ruff/configuration/
- pytest: https://docs.pytest.org/en/stable/reference/customize.html
- PEP 8: https://peps.python.org/pep-0008/
- pydantic-settings: https://docs.pydantic.dev/latest/concepts/pydantic_settings/
- Conventional Commits: https://www.conventionalcommits.org/es/v1.0.0/
- The Twelve-Factor App, configuración: https://12factor.net/es/config
