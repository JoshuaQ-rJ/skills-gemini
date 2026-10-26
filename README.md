# Skills de Gemini / Antigravity

Repositorio personal con las skills personalizadas creadas para Gemini y Antigravity.

## Skills incluidas

- **`auto-aprendizaje`**: Registro de errores, correcciones y lecciones aprendidas para evitar repetir fallos.
- **`buenas-practicas`**: Configuración de proyectos Python con uv, linters (Ruff), pytest y estructura base.
- **`contexto-joshua`**: Información sobre materias en la CUC y proyectos en Riwi (SonoraPlay, CargaExpress).
- **`estilo-janner`**: Patrones de arquitectura (Clean Architecture, microservicios) y convenciones de Janner Gonzalez.
- **`graphify`**: Análisis y mapeo de proyectos en grafos de conocimiento.
- **`humanizer`**: Ajuste de textos para retirar muletillas y estructuras típicas de redacción por IA.
- **`ponytail`**: Enfoque en la solución más simple y directa que resuelva el problema sin sobreingeniería.
- **`ponytail-audit`**: Auditoría de repositorios para identificar código innecesario, riesgos y cuellos de botella.
- **`ponytail-review`**: Revisión práctica de cambios, diffs y pull requests.
- **`skill-router`**: Selección y carga automática de las skills necesarias al inicio de cada tarea.
- **`source-driven-development`**: Soporte en documentación oficial con enlaces directos para decisiones técnicas.
- **`spec-driven-development`**: Definición de especificaciones y requerimientos antes de escribir código.
- **`test-driven-development`**: Flujo de pruebas primero (TDD) y reproducción de errores mediante tests.

---

## Cómo usarlas en otro PC

Para tener todas estas skills disponibles en otra máquina, solo clona este repositorio en la carpeta global de configuración de Gemini:

### En Windows (PowerShell)

```powershell
git clone https://github.com/JoshuaQ-rJ/skills-gemini.git "$HOME\.gemini\config\skills"
```

### En Linux o macOS (Bash/Zsh)

```bash
git clone https://github.com/JoshuaQ-rJ/skills-gemini.git ~/.gemini/config/skills
```

---

## Mantenerlas sincronizadas

- **Para subir una nueva skill o cambios desde este PC:**
  ```powershell
  cd ~/.gemini/config/skills
  git add .
  git commit -m "feat: agrega nueva skill o actualizacion"
  git push
  ```

- **Para recibir cambios en tu otro equipo:**
  ```powershell
  cd ~/.gemini/config/skills
  git pull
  ```
