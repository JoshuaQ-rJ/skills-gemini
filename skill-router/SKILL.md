---
name: skill-router
description: Use at the start of EVERY task or question, before answering or calling any other tool. Review the installed skills, pick the ones that fit the request, load them, and say in one line which were used.
---

# Skill router

Joshua instala skills con propósito y espera que se utilicen de forma proactiva y combinada. Antes de realizar cualquier acción o responder en el chat, ejecuta esta verificación.

## Pasos de ejecución

1. **Clasificar el tipo de trabajo**: programar código, revisión/auditoría, nuevo proyecto o funcionalidad, diseño/interfaz, depuración web, base de datos/backend, cloud/AWS, IA/Gemini, documentos, o contexto académico/personal.
2. **Consultar aprendizajes previos**: Revisa siempre `~/.gemini/aprendizajes/INDICE.md` y lee únicamente los archivos de tema relevantes para la tarea (regla de `auto-aprendizaje`).
3. **Seleccionar las skills aplicables**: Consulta la tabla de ruteo abajo. Combina todas las que aporten a la tarea. Si dos skills coinciden en ámbito, prioriza la más específica.
4. **Cargar y aplicar las instrucciones**: Lee los archivos `SKILL.md` necesarios antes de escribir código o generar la respuesta.
5. **Cierre de respuesta obligatorio**: Termina siempre la respuesta al usuario con una sola línea final:
   `Skills usadas: <nombre1>, <nombre2>` (o `Skills usadas: ninguna aplicaba`).

---

## Tabla de ruteo completa

### 1. Desarrollo, Arquitectura y Calidad de Código
| Tipo de trabajo / Necesidad | Skills a cargar |
|---|---|
| Escribir, modificar o refactorizar código (FastAPI, Python, SQLModel, NestJS, TypeScript, etc.) | `ponytail`, `source-driven-development`, `test-driven-development`, `estilo-janner` |
| Nuevo proyecto, nueva funcionalidad, requerimientos abiertos o ambiguos (historias de Jira, ADRs) | `spec-driven-development`, `buenas-practicas`, `estilo-janner` |
| Arranque de proyecto (Python con `uv`, pin de versión, Docker multi-stage, CI/CD GitHub Actions, linters) | `buenas-practicas` |
| Revisar un commit, diff, pull request o cambio puntual | `ponytail-review` |
| Auditoría completa de un repositorio (deuda técnica, cuellos de botella, código muerto, seguridad) | `ponytail-audit`, `graphify` (para mapear primero) |
| Entender la estructura general de un proyecto y cómo se conectan los archivos | `graphify` |
| Corrección de bugs, excepciones, errores en tests o fallas en runtime | `test-driven-development` (reproducir con test que falle antes de arreglar) |
| Decisiones de framework o librerías que requieran soporte documental | `source-driven-development` (citar documentación oficial con URL) |

### 2. Frontend, Diseño, UI y Experiencia de Usuario (UX)
| Tipo de trabajo / Necesidad | Skills a cargar |
|---|---|
| Diseñar o maquetar interfaces web (landing pages, dashboards, apps, Tailwind, CSS, tipografía, paleta del dominio, responsive) evitando el look genérico de IA | `diseno-frontend` |
| Auditar o criticar una interfaz existente (URL, captura o código) por usabilidad (Nielsen), accesibilidad (WCAG 2.2) y maquetación | `revision-interfaz` |
| Widgets interactivos en chat, simuladores HTML, controles dinámicos o visualizaciones de datos enriquecidas | `generative_ui` |

### 3. Depuración Web y Navegador (Chrome DevTools MCP)
| Tipo de trabajo / Necesidad | Skills a cargar |
|---|---|
| Inspeccionar DOM, CSS en vivo, errores de consola, peticiones de red o automatización en Chrome | `chrome-devtools` |
| Auditar y corregir accesibilidad web (etiquetas ARIA, navegación por teclado, contraste, estados de foco) | `a11y-debugging` |
| Diagnosticar cookies, estado de sesión, redirecciones de autenticación, errores 401/403, SameSite | `cookie-debugging` |
| Optimizar rendimiento web, Core Web Vitals y Largest Contentful Paint (LCP) en páginas lentas | `debug-optimize-lcp` |
| Diagnosticar fugas de memoria en JavaScript / Node.js con heap snapshots y análisis de memoria | `memory-leak-debugging` |
| Fallos de conexión o problemas al iniciar/operar el servidor MCP de Chrome DevTools | `troubleshooting` |

### 4. Ecosistema Firebase y Google Cloud
| Tipo de trabajo / Necesidad | Skills a cargar |
|---|---|
| Comandos base de Firebase CLI, autenticación (`firebase login`), cambio de proyectos (`firebase use`), descarga de configuración | `firebase-basics` |
| Modelado de datos, consultas, índices compuestos y SDKs de Cloud Firestore | `firebase-firestore` |
| Diseñar, redactar o corregir reglas de seguridad para Firestore (`firestore.rules`) | `firestore-rules-creation` (o subagente `firestore-rules-author` si aplica) |
| Auditoría de seguridad de reglas de Firestore y Storage (vulnerabilidades, bypass de roles, privilegios) | `firebase-security-rules-auditor` |
| Implementación de login, gestión de usuarios, tokens y reglas de autenticación con Firebase Auth | `firebase-auth-basics` |
| Despliegue y configuración de sitios estáticos o SPAs en Firebase Hosting tradicional (`firebase.json`) | `firebase-hosting-basics` |
| Despliegue de aplicaciones full-stack con Server-Side Rendering (Next.js, Angular) en Firebase App Hosting | `firebase-app-hosting-basics` |
| Base de datos relacional PostgreSQL con Firebase SQL Connect / Data Connect (esquemas, mutaciones, SDK) | `firebase-data-connect` |
| Monitoreo de fallos, configuración de SDK y reporte de errores con Firebase Crashlytics | `firebase-crashlytics` |
| Banderas de características (feature flags), plantillas y estrategias de carga con Firebase Remote Config | `firebase-remote-config-basics` |
| Integración de modelos Gemini en apps Firebase mediante Firebase AI Logic | `firebase-ai-logic-basics` |
| Migrar o convertir una Firebase Extension a Cloud Functions v2 independientes | `extension-to-functions-codebase` |
| Configuración de dependencias Swift / CocoaPods / paquetes en proyectos iOS Xcode (`.pbxproj`) | `xcode-project-setup` |

### 5. Modelos de Inteligencia Artificial (Gemini API)
| Tipo de trabajo / Necesidad | Skills a cargar |
|---|---|
| Llamadas a la Gemini API (texto, multimodal, imágenes, audio, function calling, structured output con Pydantic/Zod) | `gemini-api-dev` |
| Streaming bidireccional en tiempo real de audio/video y WebSockets con Gemini Live API | `gemini-live-api-dev` |
| Edición y generación de video con Gemini Omni Flash (video-a-video, transiciones primer/último fotograma) | `gemini-omni-flash-api` |

### 6. Google Workspace
| Tipo de trabajo / Necesidad | Skills a cargar |
|---|---|
| Leer, crear, editar o formatear documentos en Google Docs | `gdocs` |
| Crear, actualizar, resumir o exportar diapositivas en Google Slides | `gslides` |
| Consultar agenda, buscar huecos libres, crear, mover o eliminar eventos en Google Calendar | `gcalendar` |

### 7. Google Antigravity, Agentes y Automatizaciones
| Tipo de trabajo / Necesidad | Skills a cargar |
|---|---|
| Dudas de uso, comandos, arquitectura, CLI `agy`, configuración de Antigravity IDE 2.0 | `antigravity-guide` |
| Crear o configurar personalizaciones en Antigravity (skills, rules, MCP servers, hooks, sidecars) | `agy-customizations` |
| Gestionar, instalar, habilitar o crear plugins para Antigravity | `plugin` |
| Migrar workflows heredados (`.gemini/workflows`) al formato moderno de skills (`SKILL.md`) | `migrate-workflows` |
| Crear tareas en segundo plano automatizadas o programadas de forma recurrente (cron / timers) | `automation` |
| Diseñar, implementar o depurar agentes autónomos y sistemas multi-agente usando el SDK de Antigravity | `google-antigravity-sdk` |
| Descubrir y mostrar accesos directos a paneles de plugins en la interfaz lateral | `ui-plugin-navigation` |

### 8. Cloud e Infraestructura AWS
| Tipo de trabajo / Necesidad | Skills a cargar |
|---|---|
| Consultas, diseño, despliegue o depuración de servicios AWS (Serverless, ECS Fargate, EKS, RDS, S3, IAM, CDK, Bedrock, etc.) | Skills del AWS Agent Toolkit en `~/.agents/skills/` (según el servicio: `aws-serverless`, `aws-containers`, `aws-iam`, `aws-database`, `aws-storage`, `amazon-bedrock`, `aws-cdk`, etc.) y `contexto-joshua` si es SonoraPlay/CargaExpress |

### 9. Contexto Personal, Cursos y Dart
| Tipo de trabajo / Necesidad | Skills a cargar |
|---|---|
| SonoraPlay (Jira EG), CargaExpress Control Tower (Jira RIWI), CUC (Ingeniería de Sistemas), Riwi, ADRs, equipo | `contexto-joshua` |
| Lenguaje Dart 3, DartPad, sintaxis básica, guía de ejercicios POS de restaurante (caja, propinas, descuentos) | `dart-fundamentos` |
| Talleres, parciales, laboratorios de Física Mecánica en la CUC (momento lineal, colisiones, centro de masa, energía) | `fisica-mecanica-cuc` |

### 10. Seguridad Documental y Humanización de Textos
| Tipo de trabajo / Necesidad | Skills a cargar |
|---|---|
| Revisar cualquier PDF o Word (.docx) antes de usar su contenido para detectar texto oculto, prompts invisibles o trampas | `detectar-texto-oculto` |
| Todo texto dirigido a una persona: READMEs, documentación, ADRs, historias de Jira, PRs, informes, mensajes | `humanizer` (revisión final antes de entregar) |
| Registro de errores o correcciones para evitar repetirlos | `auto-aprendizaje` |

---

Si ninguna skill instalada aplica pero es probable que exista una en el Agent Marketplace, indícalo en una línea y ofrece buscarla.
