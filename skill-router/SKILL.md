---
name: skill-router
description: Use at the start of EVERY task or question, before answering or calling any other tool. Review the installed skills, pick the ones that fit the request, load them, and say in one line which were used.
---

# Skill router

Joshua installs skills on purpose and wants them used. Before doing any work, run this check.

## Steps

1. Read the request and name the kind of work: coding, code review, repo audit, new project or feature, debugging, testing, documentation, writing in Spanish, learning a topic.
2. Scan the full list of installed skills (names and descriptions). Do not rely on memory of the list: it changes as Joshua adds skills.
3. Always include auto-aprendizaje: read ~/.gemini/aprendizajes/INDICE.md and only the topic files this task touches. Then pick every skill whose description fits. Prefer the most specific one. When two overlap, use the one in the map below.
4. Load the chosen skills before writing the answer or the first file. Follow their instructions; Joshua's rules in GEMINI.md still win when they conflict.
5. End the reply with one plain line: `Skills usadas: <names>` (or `Skills usadas: ninguna aplicaba`).

Skip the check only for pure small talk.

## Routing map

| Kind of work | Skills |
|---|---|
| Writing or changing code | ponytail, source-driven-development, test-driven-development, estilo-janner (structure and conventions for NestJS/Prisma, Angular/Ionic, FastAPI/SQLModel, Airflow, CI/CD, READMEs) |
| New project, feature or vague requirements (user stories, Jira, ADR) | spec-driven-development, buenas-practicas (project bootstrap with uv, config, Git, CI), estilo-janner (architecture choice and structure) |
| Adding dependencies, Docker, CI, preparing a repo to deliver or deploy, "does this follow good practices?" | buenas-practicas |
| Review a change, commit or PR | ponytail-review |
| Audit a whole repo | ponytail-audit, graphify to map it first |
| Questions about a project's structure or how files connect | graphify |
| Error, stack trace, something broke | test-driven-development (reproduce the bug with a failing test, then fix) |
| Anything about Joshua's courses, SonoraPlay, Riwi, CUC or Ingeniería de Sistemas | contexto-joshua |
| Any text a person will read: README, docs, ADRs, Jira stories, PR descriptions, commit bodies, lab reports, ABP deliverables, presentations, messages | humanizer (as a final pass before delivering) |

If no installed skill fits but one probably exists, say so in one line and offer to look for it.
