---
name: auto-aprendizaje
description: Memoria de errores y correcciones. Usar SIEMPRE en dos momentos. Al empezar una tarea, para consultar las lecciones guardadas del tema. Y cada vez que Joshua corrige algo, dice que algo está mal, deshace un cambio tuyo, o una prueba o comando falla por una suposición tuya, para guardar la lección y no repetir el error.
---

# Auto-aprendizaje

Las lecciones NO se guardan en esta skill, para no llenar el espacio de skills. Viven en archivos aparte que solo se leen cuando hacen falta:

```
~/.gemini/aprendizajes/
├── INDICE.md        una línea por archivo de tema: qué cubre y cuántas lecciones tiene
├── python.md        uv, FastAPI, SQLModel, pytest, pandas...
├── git.md           ramas, commits, PR, GitHub
├── arquitectura.md  capas, Clean Architecture, microservicios, estilo-janner
├── sonoraplay.md    proyecto SonoraPlay, Jira EG, AWS del proyecto
├── cuc.md           cursos de la universidad, informes, formatos
├── escritura.md     tono, idioma, formato de respuestas y documentos
└── herramientas.md  Antigravity, Docker, Windows, terminal, MCP
```

Si una lección es solo de un proyecto concreto y ese proyecto tiene la carpeta `.agents/`, va en `<proyecto>/.agents/aprendizajes.md` en vez de los archivos globales.

Si la carpeta o un archivo no existe, créalo con un encabezado `# <Tema>` y agrégalo al INDICE.md.

## Momento 1: antes de trabajar (consultar)

1. Lee `~/.gemini/aprendizajes/INDICE.md` (es corto).
2. Abre solo los archivos de los temas que toca la tarea. Si el proyecto tiene `.agents/aprendizajes.md`, léelo también.
3. Si un archivo es largo, busca con grep las palabras clave de la tarea en vez de leerlo entero.
4. Aplica las lecciones sin anunciarlas una por una. Si una lección choca con lo que Joshua pide ahora, gana lo que pide ahora (y eso es una lección para actualizar).

No leas todos los archivos por si acaso: el objetivo es gastar poco contexto.

## Momento 2: cuando hay un error o una corrección (aprender)

Señales de que toca aprender:
- Joshua te corrige ("no", "eso está mal", "así no", "te dije que...", "otra vez...").
- Joshua deshace o reescribe un cambio que hiciste.
- Un comando, prueba o build falla por algo que supusiste en vez de verificar.
- Descubres que una lección guardada estaba mal o desactualizada.

Pasos:
1. Arregla primero el problema que te señalaron.
2. Identifica la causa en una frase: qué hiciste, qué era lo correcto y por qué.
3. Busca en el archivo del tema si ya existe una lección parecida:
   - Si existe y sigue siendo cierta, súmale una repetición (`x2`, `x3`): significa que se volvió a fallar.
   - Si existe pero estaba mal, reemplázala; no dejes dos versiones.
   - Si no existe, agrégala al final.
4. Actualiza el contador de ese tema en INDICE.md.
5. Cierra tu respuesta con una línea: `Aprendido: <la lección en pocas palabras>`.

Formato de cada lección (una sola línea):

```
- [AAAA-MM-DD] Cuando <situación>, <hacer lo correcto> (no <lo que se hizo mal>). Motivo: <por qué>. x1
```

Ejemplos:

```
- [2026-10-23] Cuando creo un proyecto Python, uso `uv init` y `uv add` (no pip install ni requirements.txt). Motivo: Joshua usa uv en todos sus proyectos. x1
- [2026-10-23] Cuando escribo historias en Jira de SonoraPlay, las escribo en inglés (no en español). Motivo: el tablero va en inglés. x2
```

## Qué NO se guarda

- Contraseñas, tokens, API keys, IPs de servidores ni datos personales.
- Instrucciones de una sola tarea ("este archivo llámalo así") que no aplican después.
- Opiniones tuyas que Joshua no confirmó.
- Cosas que ya están en GEMINI.md o en otra skill: en ese caso no se duplica; si la skill estaba mal, se avisa a Joshua para corregir la skill.

## Mantenimiento (para que no crezca sin control)

- Cada archivo de tema debe tener como máximo unas 40 lecciones. Si pasa de eso, fusiona las parecidas, borra las que ya no aplican y deja las de más repeticiones.
- Una lección con x3 o más es una regla importante: propónle a Joshua en una línea pasarla a GEMINI.md o a la skill correspondiente para que se cumpla siempre.
- Si Joshua pide "repasa lo aprendido", resume por tema las lecciones con más repeticiones.
