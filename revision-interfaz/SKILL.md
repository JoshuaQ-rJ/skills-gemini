---
name: revision-interfaz
description: Audita una interfaz web ya existente (página, landing, dashboard, app o componente, por URL, captura o código) y entrega un informe priorizado de problemas de usabilidad, accesibilidad, layout, tipografía, color, textos y pulido, con la corrección concreta de cada uno. Úsala cuando pidan revisar, auditar, criticar o "decirme qué está mal" en un diseño o sitio, cuando algo "se siente raro" o "es difícil de usar", o antes de entregar una web a un cliente.
---

# Revisión de interfaz

Síntesis de design-ux de ckw-design-skill (heurísticas de Nielsen con un juez distinto al que construyó), better-interface de jakubkrehel (evidencia y severidad) y las críticas de owl-listener/designer-skills.

Que algo sea bonito no lo hace usable. Esta revisión comprueba si alguien que llega por primera vez puede completar la tarea sin que se la expliquen, y si la interfaz se sostiene en móvil, con teclado y con lector de pantalla.

## 1. Alcance y tarea

Define qué se revisa (pantalla, flujo o sitio) y cuál es la tarea principal (por ejemplo: "un visitante entiende qué ofrece la inmobiliaria y agenda una asesoría"). Todo se juzga respecto a esa tarea. Si el alcance es muy grande, revisa un flujo completo y di qué quedó fuera.

Si el proyecto documenta sus propias reglas de diseño (guía de estilo, tokens, CLAUDE.md), respétalas: una preferencia documentada no es un hallazgo, pero tampoco excusa una falla de accesibilidad.

## 2. Evidencia, no gusto

Renderiza el estado inicial real (no un estado arreglado a mano) a 390px y 1440px, y recorre la tarea principal tomando captura de cada paso. Si solo hay código, lee todos los estados definidos (hover, foco, cargando, vacío, error). Cada hallazgo cita dónde está: archivo:línea, selector o la zona de la captura. Lo que no pudiste comprobar se marca "No verificado", nunca como hallazgo inventado.

Mejor aún: que el puntaje lo dé un subagente que no construyó la interfaz y que busque activamente lo que está mal.

## 3. Qué revisar, en este orden

Primero lo fundacional, para que el pulido no tape problemas de fondo.

Usabilidad (heurísticas de Nielsen):
1. Estado visible del sistema: cada acción tiene feedback; progreso en operaciones lentas.
2. Lenguaje y metáforas del mundo real del usuario.
3. Control y libertad: deshacer, cancelar, salir de cualquier estado; "seleccionar todo" siempre con "deseleccionar".
4. Consistencia: lo mismo se ve y se comporta igual; convenciones de la plataforma.
5. Prevención de errores: acciones destructivas confirmadas o fáciles de deshacer; envío deshabilitado mientras procesa.
6. Reconocer en vez de recordar: si hace falta un párrafo de instrucciones, falta una pista visual.
7. Flexibilidad: buenos valores por defecto para novatos, atajos para expertos.
8. Diseño minimalista: la superficie principal tiene el mayor peso visual.
9. Errores en lenguaje claro y con salida.
10. Ayuda en contexto, no un muro de texto arriba.

Accesibilidad (WCAG 2.2): nombres accesibles en todo control, foco visible, orden de tabulación lógico, contraste 4.5:1 en texto y 3:1 en bordes de inputs e íconos funcionales, labels visibles en formularios, objetivos táctiles de 44×44px, respeto a `prefers-reduced-motion`, zoom permitido.

Layout: sin scroll horizontal en ningún ancho (`scrollWidth - clientWidth` = 0), sin choques entre elementos, agrupación por proximidad, orden de lectura igual al orden visual, acción final donde termina la tarea.

Textos de interfaz: botones con verbo que dice qué pasa ("Agendar asesoría", no "Enviar"), errores que explican cómo resolver, estados vacíos que invitan a la siguiente acción, mismo término para lo mismo.

Tipografía: jerarquía clara al entrecerrar los ojos, cuerpo ≥16px, líneas de 60–75 caracteres, `tabular-nums` en cifras alineadas, sin viudas en titulares.

Color: tokens en vez de hex sueltos, el color nunca es el único portador de significado, hover y foco ganan contraste, modo oscuro diseñado y no invertido.

Pulido: radios anidados concéntricos, `transition: all`, animaciones con keyframes en estados que deberían revertirse, hover sin `@media (hover: hover)`, botón presionado por debajo de `scale(0.96)`, íconos de distintas librerías o con colores fijos.

## 4. Severidad

ALTA: bloquea la tarea, engaña, oculta contenido o controles, riesgo de perder datos, o falla repetida en todo el sistema. Siempre son ALTA: control interactivo sin nombre accesible, control sin foco visible, scroll horizontal, contraste de texto por debajo de 4.5:1, información transmitida solo con color o solo con movimiento.

MEDIA: confunde, hace más lento o rompe la consistencia de forma visible.

BAJA: pulido aislado.

Dentro de cada nivel, primero lo que un solo arreglo corrige en más lugares (un token o un componente compartido antes que un caso suelto).

Distingue defectos de convenciones: una asimetría o un solapamiento deliberado no es un error. Señálalo solo si a ojo empeora la página.

## 5. Formato del informe

Alcance revisado y tarea principal en una línea.

Tabla:

| Severidad | Dónde | Problema | Corrección | Por qué |
|---|---|---|---|---|

Una fila por causa raíz, con todas sus ubicaciones.

Luego: lista de arreglos priorizada (ALTA → MEDIA → BAJA, agrupando los que tocan la misma pieza), lo que quedó "No verificado", y el veredicto: Bloquear si queda algún hallazgo ALTA, Aprobar si no. No apruebes nada que no inspeccionaste.

Después de corregir, vuelve a renderizar y a puntuar; no declares nada arreglado sin revisar de nuevo.
