---
name: contexto-joshua
description: Context about Joshua Quintero's studies and projects at Universidad de la Costa (CUC) and Riwi, Ingeniería de Sistemas courses, SonoraPlay Regalías (Jira EG), and CargaExpress Supply Chain Control Tower (Jira RIWI, GitHub cargaexpress). Use whenever a task mentions SonoraPlay, CargaExpress, Jira EG-XX, Jira RIWI-XX, ADRs, Riwi, CUC, Física Mecánica, Cálculo Integral, his teammates, or his university and bootcamp work.
---

# Contexto de Joshua

Joshua Quintero estudia Ingeniería de Sistemas en la Universidad de la Costa (CUC) y hace formación en Riwi. GitHub: JoshuaQ-rJ.

## Universidad de la Costa (CUC)

### Física Mecánica
- Curso: FÍSICA MECANICA - PRESENCIAL-26382, profesor Luis Polo Ariza.
- Equipo de laboratorio: Gianluca Geraldino, José Rangel, Juan Herrera, Joshua Quintero.
- Equipo del proyecto ABP (Corte 2): Gianluca Geraldino, Matías Salgado, José Rangel, Juan Herrera, Joshua Quintero (Javith Santana ya no está).
- ABPr, situación problema 1: "Movilidad sostenible en zonas de borde costero", mejorar la movilidad urbana cerca de la Ciénaga de Mallorquín con principios de física e ingeniería.
- Entregables de laboratorio: pre-informe (formato de la guía del experimento) e informe (plantilla IEEE de la universidad).

### Cálculo Integral
- Trabajos grupales ABP; el grupo es de las ingenierías Civil y Sistemas.
- Integrantes del entregable "Segundo Momento": Joshua Quintero, Samuel Pacheco, José Barliss, Dylan Castro.
- Suele compartir diapositivas y guías de ejercicios de la clase para pedir ayuda.

## Riwi: Proyecto 08 · SonoraPlay Regalías

- Plataforma de streaming musical ficticia: liquidación de regalías, engagement y catálogo.
- Equipo de 3: Joshua, María Clara y Andrea.
- Repo: https://github.com/JoshuaQ-rJ/sonoraplay-proyect. Joshua es el dueño y sus commits van a su nombre; eso es correcto.
- Nunca proponer cambiar `git config user.name` / `user.email`: los commits quedan a nombre de quien trabaja en su máquina.
- Jira: proyecto existente `el_golf`, clave EG. El contenido del tablero (épicas, historias, sprints) va en inglés.
- Numeración: la historia N es EG-(N+9). Sprints: S1 = historias 01–09, S2 = 10–16, S3 = 17–23, S4 = 24–28, S5 = 29–34, S6 = 35–41.
- Feedback del backlog: poner MoSCoW (Must/Should/Could/Won't) a cada ítem por sprint y más criterios de aceptación.
- Requisito: el proyecto debe incluir servicios de AWS desplegados. Estrategia de costos: configurar y apagar los servicios con costo; prenderlos solo la última semana.

### Sprint 1 (EG-10 a EG-18, 31 pts)
- Stack local: Python 3.12, PostgreSQL 16 en Docker, pandas, Faker, SQLAlchemy Core, pytest, Ruff, Gitleaks, GitHub Actions.
- Monorepo `sonoraplay-regalias` con src layout.
- Ramas: main / develop / feature/EG-XX. Los commits llevan la clave de Jira.

### Arquitectura v1 (tarea 07 · EG-16, Sprint 1, lidera Joshua)
- Entrega: diagrama .drawio + PNG, arquitectura-v1.md, plantilla ADR, ADR-0001 y registro de ADR (en el repo bajo docs/arquitectura y docs/adr).
- Principios: servicios 24/7 y Spark bajo demanda; menor costo justificable; solo el ALB es público; secretos en SSM + OIDC; todo con Terraform. Región us-east-1.
- Stack: VPC con 2 AZ (subredes públicas y privadas); instancia NAT t4g.nano; endpoint Gateway de S3; ALB; API de titulares y API de contratos F4 en Fargate ARM On-Demand (0,25 vCPU / 0,5 GB); simulador F2 y consumidor→Bronze en Fargate Spot; RabbitMQ en EC2 t4g.small; Airflow + Celery en EC2 t4g.medium; Spark en tareas Fargate Spot bajo demanda; S3 Bronze/Silver/Gold en Parquet por año/mes/país; RDS PostgreSQL db.t4g.micro Single-AZ con backups de 7 días; ECR; SSM Parameter Store; CloudWatch; Budgets + SNS; EKS solo en el Sprint 5 y la demo; Terraform; GitHub Actions con OIDC; Power BI Desktop por túnel SSM.
- Descartados de la arquitectura de referencia: DynamoDB, Memcache, SES y Auto Scaling de EC2.
- Costo estimado con todo prendido ≈ 115–120 USD/mes sin EKS (a confirmar en la HU 23 con AWS Pricing Calculator).
- ADR-0001 (propuesto): opción híbrida C, frente a "todo en una EC2" (30–40 USD, no cubre los temas) y stack administrado con MWAA y Amazon MQ (> 450 USD).
- Plantilla ADR: metadatos (estado, fecha, historia/Jira, responsable, revisor, referencias), contexto, criterios de negocio/requisito/costo, opciones con costo, decisión, consecuencias, validación y fuentes.

### Registro de ADR (número · tema · historia · Jira · sprint · responsable)
- 0001 base AWS · HU07 · EG-16 · S1 · Joshua
- 0002 zona horaria día/mes · HU02 · EG-11 · S1 · María Clara
- 0003 duplicados F1 · HU03 · EG-12 · S1 · María Clara
- 0004 esquema F2 y dedup event_id · HU06 · EG-15 · S1 · Andrea
- 0005 umbrales de granjas · HU09 · EG-18 · S1 · María Clara
- 0006 autenticación y aislamiento de sellos · HU12 · EG-21 · S2 · Andrea
- 0007 cierre de mes append-only · HU14 · EG-23 · S2 · María Clara
- 0008 país que define la bolsa · HU14 · EG-23 · S2 · María Clara
- 0009 región · 0010 instancia NAT vs NAT Gateway · 0011 Terraform · HU17 · EG-26 · S3 · Joshua
- 0012 Fargate On-Demand/Spot/ARM · HU18 · EG-27 · S3 · Andrea
- 0013 RabbitMQ en EC2 vs Amazon MQ · HU20 · EG-29 · S3 · Andrea
- 0014 Data Lake Parquet · HU22 · EG-31 · S3 · María Clara
- 0015 Airflow en EC2 vs MWAA · HU25 · EG-34 · S4 · Joshua
- 0016 skew en Spark · HU30 · EG-39 · S5 · Joshua
- 0017 OIDC y secretos SSM · HU31 · EG-40 · S5 · Andrea
- 0018 ECS vs EKS · HU32 · EG-41 · S5 · Joshua
- 0019 Power BI por túnel SSM · HU35 · EG-44 · S6 · María Clara

Los ADR de Joshua: 0001, 0009, 0010, 0011, 0015, 0016, 0018.

## Riwi: Proyecto 09 · CargaExpress Supply Chain (Control Tower)

- Torre de control logístico multicanal que centraliza pedidos, despachos y eventos de transportadoras heterogéneas, traduciendo sus estados dispares a un vocabulario canónico único.
- Organización en GitHub: `https://github.com/cargaexpress`
- Repositorios locales en `C:\Users\J1shu\cargaexpress`:
  - `control_tower` (`https://github.com/cargaexpress/cargaexpress_control_tower.git`): Backend FastAPI, async SQLAlchemy, Alembic, PostgreSQL 16, Docker Compose, orquestación Airflow con CeleryExecutor y RabbitMQ.
  - `docs` (`https://github.com/cargaexpress/cargaexpress-docs.git`): Documentación técnica en Docusaurus con GitHub Pages.
  - `main_repo` (`https://github.com/cargaexpress/cargaexpress.git`): Repositorio central / landing del proyecto.
  - Repositorio auxiliar: `cargaexpress_seed` (semillero de datos mock, 25 tablas e inyección de anomalías).
- Equipo RIWI (Tablero Jira `RIWI` - "Los Andes" en `julivanegascri-1790011157852.atlassian.net`):
  - Alexandra Peña Orozco (Tech Lead / Infraestructura / Reportera)
  - Julian Vanegas (Desarrollo backend)
  - Helda Reyes (Desarrollo backend / conectores e ingesta)
  - Joshua Quintero (`JOSHUA QUINTERO`, accountId `712020:447fe5d8-b9b6-43e2-8e5b-d62dd9db9bc9`)

### Dominio y Reglas del Negocio
- **8 Estados Canónicos**: `CREATED`, `PICKED_UP`, `IN_TRANSIT`, `OUT_FOR_DELIVERY`, `EXCEPTION`, `DELIVERED`, `RETURNED`, `LOST_OR_DAMAGED`.
- **Integración de Transportadoras**:
  - Tipo A: 5 carriers por Webhooks push (eventos en tiempo real desacoplados vía RabbitMQ).
  - Tipo B: 4 carriers por Polling pull periódico REST (cada 30 min vía Airflow DAG).
  - Tipo C: 3 carriers por Lote de archivos CSV/XLSX (cada 4 horas vía Airflow DAG con limpieza de cabeceras repetidas y totales).
- **Reglas Críticas**:
  - `RN-02`: Protección de transiciones y estados terminales (`DELIVERED`, `RETURNED`, `LOST_OR_DAMAGED`); no se permite retroceder y se registran anomalías.
  - `RN-03`: SLA en días hábiles (excluye domingos y festivos del país destino, corte a las 4:00 PM).
  - `RN-04`: Órdenes en riesgo (< 24 h hábiles restantes sin estar en reparto, o excepción > 12 h).
  - `RNF-01`: Respuesta de webhook < 200 ms con encolamiento asíncrono en RabbitMQ.

### Sprints del Proyecto
- **Sprint 1 (US-01 a US-09)**: Comprensión, diseño ERD WMS, reglas de negocio, catálogo canónico y scaffolding inicial. 100% *Finalizado* en Jira.
- **Sprint 2 (HU-11 a HU-25)**: Persistencia ORM, APIs base de órdenes y guías, simuladores de carriers y conectores. En Jira: HU-11 a HU-19 finalizadas; HU-20 a HU-24 actualmente *En curso* (asignadas a Helda Reyes). En git: rama activa `fix/RIWI-61-state-transitions-rn02` implementando validación estricta de RN-02.
- **Sprint 3 (HU-26 a HU-40)**: Orquestación distribuida (Airflow + Celery + RabbitMQ), motor de SLA y despliegue cloud en AWS (Docker multi-stage, ECR, RDS, ECS Fargate, CI/CD).

### Historias de Usuario (HU) asignadas a Joshua Quintero (Sprint 3)
1. **HU-26 (`RIWI-131`) — Set up Airflow in Docker**:
   - Objetivo: Desplegar Apache Airflow (webserver, scheduler, postgres metastore) en contenedores Docker Compose.
   - Estado en Jira: **Finalizado** (Done). Subtareas RIWI-132, RIWI-133 y RIWI-134 finalizadas.
   - Estado en Repo: **Implementado y mergeado** a `develop` (PR #5) con `docker-compose.airflow.yml` y `AIRFLOW_SETUP.md`.
2. **HU-28 (`RIWI-139`) — Type-C file ingestion DAG**:
   - Objetivo: DAG periódico que procesa archivos CSV/XLSX de transportadoras Tipo C, filtra anomalías (cabeceras duplicadas, filas de total) y normaliza a estados canónicos.
   - Estado en Jira: **Finalizado** (Done). Subtareas RIWI-140, RIWI-141 y RIWI-142 finalizadas.
   - Estado en Repo: **Implementado** en `dags/dag_type_c_ingestion.py`.
3. **HU-29 (`RIWI-143`) — Configure CeleryExecutor in Airflow connected to RabbitMQ**:
   - Objetivo: Distribuir ejecución de tareas en Airflow usando `CeleryExecutor` con RabbitMQ como broker de mensajes.
   - Estado en Jira: **Finalizado** (Done). Subtareas RIWI-144 y RIWI-145 finalizadas.
   - Estado en Repo: **Implementado** en `docker-compose.airflow.yml` con servicio `airflow-worker` y broker RabbitMQ (`5672` AMQP, `15672` Management).
4. **HU-30 (`RIWI-147`) — Scale workers and validate distributed execution**:
   - Objetivo: Escalar workers Celery y probar que tareas paralelas se ejecutan en diferentes instancias sin colisiones.
   - Estado en Jira: **Finalizado** (Done). Subtareas RIWI-146, RIWI-148, RIWI-149 y RIWI-150 finalizadas.
   - Estado en Repo: **Implementado y validado** en rama `feature/RIWI-147-scale-celery-workers` (commit `54cc1b7`) con soporte de escalado horizontal en `docker-compose.airflow.yml`, DAG de validación `dags/dag_distributed_validation.py` y Runbook Operativo E-12 en `AIRFLOW_SETUP.md`.
5. **HU-34 (`RIWI-164`) — Optimize the backend Dockerfile with a multi-stage build**:
   - Objetivo: Convertir el Dockerfile del backend a multi-stage build eliminando uv y herramientas de compilación de la imagen final.
   - Estado en Jira: **Finalizado** (Done). Subtareas RIWI-165, RIWI-166 y RIWI-167 finalizadas.
   - Estado en Repo: **Implementado y validado** en rama `feature/RIWI-164-backend-dockerfile-multistage` (commit `1dba3a1`) con Dockerfile multi-stage (`builder` + `final` runtime en `python:3.12-slim`), usuario `appuser` no-root, reducción de 488 MB a 299 MB (-38.7% disco, -50.3% transferencia), `.dockerignore` sincronizado y documentación en `backend/README.md` y `README.md`.
6. **HU-35 (`RIWI-168`) — Optimize simulator and Airflow Dockerfiles**:
   - Objetivo: Aplicar optimizaciones y `.dockerignore` en imágenes de simuladores y Airflow para reducir tamaño y cumplir entregable E-13.
   - Estado en Jira: **Finalizado** (Done). Subtareas RIWI-169, RIWI-170 y RIWI-171 finalizadas.
   - Estado en Repo: **Implementado y validado** en repositorios `type_A_simulation_data`, `type_B_simulation_data`, `type_C_simulation_data` y `control_tower` sobre ramas `feature/RIWI-168-optimize-dockerfiles` y `feature/RIWI-168-optimize-simulator-airflow-dockerfiles`. Multi-stage builds en todos los carriers (A, B, C, D, tools, seed), `.dockerignore` sincronizados, usuarios no-root y reporte formal consolidado del Entregable E-13 en `control_tower/README.md` y `AIRFLOW_SETUP.md`. Reducción general de hasta 47.4% en disco y 50% en transferencia.

### Convenciones de Git y Flujo de Trabajo en CargaExpress
- Ramas: `main`, `develop`, `feature/RIWI-XX-*`, `fix/RIWI-XX-*`.
- Commits: En inglés, referenciando la clave de Jira (p. ej. `RIWI-131: Fix RabbitMQ volume permissions` o `feat(airflow): RIWI-131 ...`).
- Repositorio principal de desarrollo: `C:\Users\J1shu\cargaexpress\control_tower`.
