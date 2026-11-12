---
name: diseno-figma
description: Diseña, rediseña o arregla archivos de Figma (tableros/dashboards, pantallas, landings, componentes, FigJam) para que se vean profesionales y no "hechos por IA", usando el MCP de Figma. Úsala SIEMPRE que haya un link de figma.com o se pida crear, mejorar, revisar o "arreglar porque se ve horrible" algo en Figma, incluido un tablero de métricas, aunque no se diga "diseño".
---

# Diseño en Figma

Síntesis de la mecánica oficial del MCP de Figma (skills figma-use y figma-generate-design), la revisión basada en datos de nodos de shomtsm/figma-review-skill, la lista anti "look IA" del frontend-design oficial de Anthropic y de nutlope/hallmark, y los criterios de diseño de las skills diseno-frontend y revision-interfaz.

Por qué un archivo de Figma "se ve horrible" casi siempre es medible: demasiados valores de espaciado distintos, demasiados colores sueltos, tamaños que no se repiten entre elementos del mismo rol, nada en auto layout, sin jerarquía clara y todo con el mismo peso visual. Por eso el trabajo empieza midiendo y termina mirando.

## 0. Antes de tocar nada

1. Saca el fileKey y el nodeId del link (`figma.com/design/:fileKey/...?node-id=1-2` → nodeId `1:2`; `figma.com/board/...` es FigJam).
2. Abre sesión con `create_session` y carga la skill oficial `figma-use` antes de cualquier `use_figma` (y `figma-generate-design` si vas a construir pantallas completas, `figma-use-figjam` si es FigJam). Ellas mandan en la mecánica; esta skill manda en el criterio. En Antigravity el servidor suele ser el de escritorio de Figma (`figma-desktop`, http://127.0.0.1:3845/mcp), que exige la app de Figma abierta con el archivo y el frame seleccionado; si no expone `create_session` ni `use_figma`, trabaja con las herramientas que sí liste (get_metadata, get_screenshot, get_variable_defs, get_design_context) y entrega los cambios como instrucciones paso a paso.
3. Toma `get_screenshot` del frame y `get_metadata` para la estructura. Revisa variables, estilos y librerías existentes (`get_variable_defs`, `search_design_system`, `get_libraries`): si ya hay sistema de diseño, se usa, no se inventa otro.
4. Pregunta lo mínimo que falte: para qué es el tablero, quién lo mira y qué decisión toma con él. Si no hay respuesta, infiérelo y dilo en una línea.

## 1. Diagnóstico medible

Recorre el árbol de nodos y cuenta, en vez de opinar:

- Espaciados: cuántos valores distintos de padding y gap hay. Más de 5–6 es ruido; deben caer en una escala de 4/8 (4, 8, 12, 16, 24, 32, 48, 64).
- Colores: cuántos fills distintos. Más de ~8 sin variables es caos; cada color debe tener rol (fondo, superficie, borde, texto, acento, estado).
- Tipografía: cuántas combinaciones tamaño/peso. Un tablero sano usa 5–7 estilos de texto, máximo dos familias.
- Tamaños por rol: botones, tarjetas, íconos y filas del mismo tipo con el mismo alto y radio.
- Estructura: frames sin auto layout, grupos en vez de frames, anidación muy profunda, capas sin nombre ("Frame 427").
- Alineación: bordes que casi coinciden (1–7px de diferencia) en lugar de compartir línea.
- Contraste: texto sobre su fondo efectivo por debajo de 4.5:1 (3:1 en texto grande).

Muestra el diagnóstico en una tabla corta (Categoría | Qué encontré | Propuesta) antes de cambiar nada si el archivo es de otra persona o el cambio es grande.

## 2. Dirección antes de pintar

Igual que en web: define en pocas líneas propósito, público, paleta con rol (4–6 colores con hex), tipografías y una firma. Evita los defaults que delatan diseño generado:

- Fondo crema con serif de alto contraste y acento terracota; fondo casi negro con un solo acento verde ácido.
- Todo en tarjetas idénticas redondeadas con la misma sombra gris y degradados de adorno.
- Etiquetas en MAYÚSCULAS con tracking sobre cada título, textos unidos con "·", flechas "→" pegadas a los botones, números 01/02/03 cuando el contenido no es una secuencia.
- Una sola palabra del titular en otro color o en itálica.
- Degradado morado-azul, tarjeta dentro de tarjeta, emojis como íconos.
- Métricas, logos o testimonios inventados: usa marcadores claros si no hay datos reales.

Si el usuario pidió explícitamente uno de esos estilos, se respeta.

## 3. Construcción limpia

- Primero tokens: variables de color (con modos claro/oscuro si aplica), espaciado y radios; estilos de texto. Luego componentes, luego la pantalla. Nada de hex sueltos en capas.
- Auto layout en todo contenedor; gaps desde la escala; `Fill container` / `Hug contents` en lugar de anchos fijos arbitrarios.
- Grilla: 12 columnas en escritorio (1440 de ancho, márgenes 24–32), 4 en móvil. Las tarjetas se alinean a columnas.
- Radios anidados: exterior = interior + padding. Un radio por nivel de anidación.
- Nombres de capa con sentido ("KPI / Ventas del mes", no "Frame 12").
- Construye por secciones e inspecciona cada una con `get_screenshot` antes de seguir; es más fácil corregir una sección que la pantalla entera.

## 4. Tableros (dashboards)

Un tablero sirve para decidir rápido. Reglas que más cambian el resultado:

- Arriba lo que responde "¿cómo vamos?": 3–5 KPIs como máximo, cada uno con valor grande, etiqueta clara en minúscula, comparación con periodo anterior (▲/▼ con color y signo, nunca solo color) y periodo explícito.
- Debajo, la explicación: 1–2 gráficos principales grandes; luego detalle (tablas, rankings). Lectura en Z o F, de lo general a lo particular.
- Un tipo de gráfico por pregunta: línea para tendencia en el tiempo, barras para comparar categorías (horizontales si los nombres son largos), barras apiladas o donut solo para partes de un total con pocas categorías (≤5). Nada de 3D, nada de tortas con 10 porciones.
- Color con intención: grises para estructura y datos de contexto, un color de marca para la serie principal, rojo/verde reservados para estados. Paleta de series accesible y consistente en todos los gráficos.
- Ejes que empiezan en cero en barras, etiquetas directas sobre las series en vez de leyendas lejanas, cuadrícula suave o ninguna, números con separador de miles y `tabular` alineados a la derecha en tablas.
- Filtros (fecha, segmento) arriba y agrupados; el estado activo se ve.
- Diseña también los estados: sin datos, cargando (skeleton), error.
- Densidad: aire suficiente entre tarjetas (16–24), padding interno consistente (16–24), máximo ~6–8 bloques visibles en la primera pantalla.

## 5. Verificación

1. `get_screenshot` del resultado completo y míralo buscando lo que está mal: choques, bordes casi alineados, jerarquía confusa, contraste bajo, zonas vacías o amontonadas, algo que compita con el KPI principal.
2. Repite el conteo del paso 1: los números (valores de espaciado, colores, estilos de texto) deben haber bajado y caer en la escala.
3. Si es una pantalla con versión móvil, revisa también ese frame.
4. Si puedes, pide la crítica a un subagente que no hizo el diseño.

## 6. Entrega

Resumen breve: dirección elegida, antes/después del diagnóstico (por ejemplo "espaciados: 14 valores → 6; colores: 23 → 9 variables"), qué quedó con marcadores por falta de datos reales y qué no pudiste verificar. Si la revisión es para otra persona y las herramientas disponibles permiten comentar, deja un comentario por problema sobre el elemento, con formato "[Categoría] problema → propuesta"; si no, entrega la misma lista en la respuesta.
