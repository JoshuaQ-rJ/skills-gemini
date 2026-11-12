---
name: diseno-frontend
description: Diseña y construye interfaces web con criterio de diseñador senior (landing pages, sitios de marca, dashboards, componentes, apps en HTML/CSS, React, Next.js o Tailwind) evitando el "look genérico de IA". Úsala SIEMPRE que haya que crear o mejorar cómo se ve algo en la web, aunque no se diga "diseño" — "hazme una página", "que se vea más pro", "arregla el espaciado", "landing para un cliente", "sitio para la inmobiliaria", colores, tipografía, animaciones, responsive o pulido visual.
---

# Diseño frontend

Síntesis de lo mejor de ckw-design-skill (dirección + verificación renderizada), jakubkrehel/skills (valores exactos de pulido), ui-ux-pro-max (prioridades UX), scroll-craft (landings con ritmo), owl-listener/designer-skills (leyes de UX), el frontend-design oficial de Anthropic y nutlope/hallmark (señales de diseño generado) y emilkowalski/skills (criterio de animación).

La idea central: un modelo genera la UI como texto, nunca la ve. Por eso (1) su primera idea es el promedio de todo lo que ha visto y (2) no puede notar choques, desbordes ni desequilibrios. Este proceso corrige las dos cosas: decidir una dirección propia antes de codificar, y renderizar y mirar antes de dar algo por terminado.

## 1. Dirección antes de código

Antes de escribir CSS, responde en 5–8 líneas (muéstraselas al usuario si la tarea es nueva):

- Propósito y público: qué problema resuelve y para quién. Si es para un negocio, cuál es la acción que importa (agendar, comprar, escribir por WhatsApp).
- Mundo del producto: 5 conceptos o palabras del dominio (una inmobiliaria en el Caribe: brisa, terraza, escritura, llave, atardecer).
- Paleta del mundo: 5 colores que verías si el producto fuera un lugar físico. Nombra colores reales del dominio, no "cálido/frío".
- Tono: elige un extremo y ejecútalo con intención (editorial, minimal refinado, orgánico, lujo sobrio, juguetón, industrial, retro…).
- Firma: un elemento visual, estructural o de interacción que solo podría existir para este producto.

Trata tu primer instinto como el promedio y aléjate a propósito hacia el mundo del producto, no hacia otra moda. Hay dos promedios que evitar:

- Promedio genérico de IA: Inter, degradado morado sobre blanco, una columna centrada, tres tarjetas iguales, emojis como íconos.
- Promedio "de diseñador de moda": mayúsculas condensadas gigantes, modo oscuro con grano, microtexto monoespaciado decorativo ("35MM · SCAN"), stickers.

Señales concretas de diseño generado (lista del frontend-design oficial de Anthropic y de nutlope/hallmark), úsalas solo si el brief las pide:
- Fondo crema (~#F4F1EA) con serif de alto contraste y acento terracota (~#D97757); fondo casi negro con un único acento verde ácido o bermellón.
- Etiqueta en MAYÚSCULAS con tracking encima de cada título (eyebrow), metadatos unidos con "·", "→" pegada al texto de links y botones, numeración 01/02/03 cuando el contenido no es una secuencia.
- Una sola palabra del titular en itálica, negrita u otro color.
- Todo cortado en tarjetas idénticas con el mismo radio y la misma sombra gris, tarjeta dentro de tarjeta, degradado morado-azul.
- Monoespaciada para etiquetas pequeñas, negro teñido (#111) en lugar de negro.
- Fade-and-slide en cada sección y hover animado en cada tarjeta.

Haz el plan en dos pasadas: primero un plan corto (4–6 colores con hex, tipografías y su rol, layout en una frase o wireframe ASCII, principios), luego revísalo contra el brief y cambia todo lo que saldría igual en cualquier página parecida. Solo después escribe código.

Si el resultado podría ser de cualquier startup, entregaste el promedio.

Reserva el impacto para la puntuación: 1–2 momentos grandes (hero, cierre) y el resto tranquilo. Un acento de color, no cinco. Un movimiento de firma, no animación constante.

## 2. Sistema: tokens primero, pantallas después

Orden de construcción: tokens → primitivos → componentes → secciones → páginas. Si el proyecto ya tiene tokens, componentes o librería (shadcn, Tailwind config), úsalos y extiéndelos; no inventes un sistema paralelo.

Tokens de color (CSS variables, nunca hex sueltos en componentes):
- texto: primario, secundario, apagado
- fondo: base, elevado, overlay
- borde: sutil, normal, énfasis
- marca: acento principal
- semánticos: éxito, aviso, error (info opcional)

El gris construye estructura; el color comunica estado, acción o identidad. Color sin motivo es ruido.

Contraste: WCAG 2 como mínimo obligatorio (4.5:1 texto normal, 3:1 texto grande y bordes de inputs). Los estados hover, active y focus deben ganar contraste, nunca perderlo (un hover que aclara el texto parece deshabilitado). Modo oscuro: define los tokens otra vez, no inviertas colores.

Tipografía:
- Una display + una de texto. Elige desde el dominio, no la primera que se te ocurra.
- Jerarquía por tamaño, peso y tracking juntos: titulares más pesados y con tracking apretado; texto cómodo (base 16px, interlineado ~1.5, 60–75 caracteres por línea); etiquetas de UI en peso medio.
- Números que se alinean en columnas: `font-variant-numeric: tabular-nums`. Monoespaciada solo para datos reales, no como decoración.
- `text-wrap: balance` en titulares y `text-wrap: pretty` en párrafos para evitar viudas.
- Prueba del entrecerrar ojos: si no distingues titular de cuerpo, la jerarquía es débil.

Espaciado: una escala (4/8px) y aplícala con consistencia; más aire alrededor de un elemento aumenta su importancia. Agrupa lo relacionado (ley de proximidad) y separa grupos con más espacio que el interno.

## 3. Valores exactos de pulido

Estos valores vienen probados; úsalos tal cual salvo que el proyecto tenga una convención propia consistente.

Antes de animar algo, pregunta en orden (emilkowalski/skills): ¿debe animarse? (no en acciones de teclado, superficies de uso muy frecuente ni datos funcionales), ¿qué comunica?, ¿qué propiedades? (transform y opacity), ¿qué curva y duración? (ease-out para entrar, menos de 300ms en UI), ¿se puede interrumpir?

- Radios anidados: radio exterior = radio interior + padding (+ borde). El hijo nunca más redondo que el padre. Con más de 24px de padding, trátalos como superficies independientes.
- Sombras para elevación, bordes para estructura. Mantén bordes en divisores, tablas, inputs y estados seleccionados. Bajo un anillo de sombra deja `border: 1px solid transparent` para que el modo alto contraste aún dibuje el borde.
- Imágenes de contenido: `outline: 1px solid` con `outline-offset: -1px`, color `oklch(0 0 0 / 0.1)` en claro y `oklch(1 0 0 / 0.1)` en oscuro.
- Botón presionado: `scale(0.96)` en 150ms `ease-out`; nunca escalar un botón deshabilitado.
- Interacciones frecuentes (teclear, hover de filas, cambiar tabs): respuesta instantánea o ≤150ms solo en `opacity`/`background-color`.
- Entradas escalonadas (solo en momentos poco frecuentes como el primer load): bloques semánticos separados 100ms, cada uno con opacity, blur 4px y translateY 12px en 300ms `ease-out`.
- Salidas más cortas que entradas: 150ms, translateY -12px.
- Cambios de estado con transiciones CSS, no keyframes (las transiciones se pueden revertir a mitad de camino).
- `transition-property` con las propiedades exactas, nunca `all`. Anima solo `transform`, `opacity` y `filter`; no animes width/height.
- Hover solo en `@media (hover: hover)` para que en móvil no quede "pegado".
- Modales, drawers y menús con scroll: `overscroll-behavior: contain`.
- Íconos: una sola librería, `currentColor`, trazo acorde al peso del texto (1.5px con 400, hasta 2.5px con 700). SVG, nunca emojis.
- Alineación óptica: ajusta 1–2px a ojo cuando la geometría "se ve" descentrada (triángulo de play, íconos junto a texto).
- Al cambiar tema, desactiva transiciones un frame para que no se "embarre" el cambio.
- Todo movimiento de traslación, escala o blur va dentro de `@media (prefers-reduced-motion: no-preference)`; con movimiento reducido usa un fundido de opacidad.
- Toda animación deja también una señal estática (color, ícono o texto). El movimiento nunca es el único canal de feedback.

## 4. UX que no se negocia

En orden de prioridad (ui-ux-pro-max):

1. Accesibilidad: HTML semántico, textos alternativos, todo usable con teclado, foco visible, botones de solo ícono con `aria-label`.
2. Táctil: objetivos de al menos 44×44px con 8px de separación; feedback de carga en acciones lentas.
3. Rendimiento: imágenes WebP/AVIF, `loading="lazy"` debajo del pliegue, `fetchpriority="high"` en la imagen del hero, espacio reservado con `aspect-ratio` (sin saltos de layout).
4. Layout: mobile-first, meta viewport, sin scroll horizontal, nunca deshabilitar zoom.
5. Formularios: label visible siempre (el placeholder no es label), error junto al campo, deshabilitar el envío mientras procesa.
6. Navegación: atrás predecible, máximo 5 ítems en navegación inferior móvil.

Cada componente tiene sus estados: vacío, cargando (skeleton que imita el layout final, no un spinner suelto), error con salida clara, éxito. Si alguien pudiera capturar la página a mitad de carga y te daría vergüenza, falta un estado intermedio.

Ordena la página según la tarea: orientar arriba, trabajar en el medio, confirmar donde termina la tarea. Si el usuario revisa una lista larga y luego actúa, el botón de acción también va abajo (o la barra es sticky).

Leyes útiles para decidir: Fitts (lo importante grande y cerca), Hick (menos opciones por pantalla), Jakob (respeta convenciones que ya conocen), Miller (agrupa la información en bloques), Von Restorff (lo distinto se recuerda: úsalo para el CTA).

Fuentes: si son externas, `preconnect` + `font-display: swap` con fallback ajustado (`size-adjust`) para que el cambio no mueva el layout; en proyectos propios, preferir WOFF2 autoalojado y precargar solo los pesos del primer viewport.

## 5. Landings y sitios de marca

Para páginas de marketing (servicios, inmobiliaria, marca personal, producto):

- Un mensaje héroe y una acción principal inequívoca arriba del pliegue; acciones secundarias presentes pero sin competir. Titular, una frase y la acción principal visibles a 1280×800 sin hacer scroll; unas 80 palabras como máximo por pantalla.
- El contenedor tiene ancho máximo y se centra: en 1920px crecen los márgenes, no la medida del texto ni la grilla.
- Decide si el primer golpe es emocional o racional y alinea copy y layout con eso.
- Variedad de secciones: no repitas el mismo patrón dos veces seguidas (texto+imagen, grilla, cita grande, cifras, galería, testimonio real, CTA). Cinco secciones idénticas son una sola sección vista cinco veces.
- Una curva emocional con un solo pico diseñado (el momento "wow"), no todo al máximo.
- Mundo fotográfico real cuando el negocio es real (fotos del cliente, del lugar). Nada de ilustración 3D genérica por defecto.
- Hero con capas (fondo, sujeto, primer plano) si quieres sensación premium; el parallax sutil basta.
- Scrollytelling solo para contenido que se lee (explicar un proceso, un caso). Para herramientas y formularios, interacción normal.
- Composición móvil pensada aparte, no solo "apilar" el escritorio.
- No inventes testimonios, cifras ni logos de clientes: usa marcadores claros ("[testimonio real aquí]") si no hay datos.

## 6. Verifica antes de decir "listo"

El modelo no puede ver lo que generó, así que míralo:

1. Renderiza la página (servidor estático + Playwright, o el navegador disponible) y toma capturas a 390px, ~1024px y 1440px.
2. Revisa desborde horizontal en cada ancho: `document.documentElement.scrollWidth - document.documentElement.clientWidth` debe dar 0. Es el error más común porque es invisible en pantalla ancha y reaparece cada vez que una fila (header, nav, toolbar) gana un elemento. Defensas por defecto: `flex-wrap: wrap` en filas de header/toolbar, `min-width: 0` en hijos de flex/grid, `overflow-wrap: anywhere` en URLs largas, `100%` en vez de `100vw`, y `body { overflow-x: clip }` como red (no como arreglo). Para encontrar al culpable:
   ```js
   document.querySelectorAll('*').forEach(el=>{const r=el.getBoundingClientRect();
     if(r.right>innerWidth+1||r.left<-1) console.log(Math.round(r.right), el);});
   ```
3. Mira las capturas buscando lo que está mal: textos que chocan con imágenes, alineaciones casi iguales (1–7px fuera), jerarquía confusa, contraste bajo, botones pequeños, nada que atraiga la vista primero.
4. Si puedes, pide la crítica a un subagente que no construyó la página: quien construye tiende a justificar lo que hizo.
5. Corrige, vuelve a renderizar y vuelve a mirar.

Distingue fallas de convenciones. Desborde, contraste y tamaño táctil son defectos reales: se corrigen siempre. Simetría, alineación perfecta y ritmo uniforme son solo señales: una asimetría deliberada o un solapamiento intencional suele ser lo más interesante de la página, no lo "arregles" hacia lo simétrico.

Si no pudiste verificar algo (no hay navegador, por ejemplo), dilo explícitamente en vez de afirmar que está bien.

## Entrega

Al terminar, en pocas líneas: la dirección elegida (tono, paleta, tipografías, firma), qué verificaste y en qué anchos, y lo que no pudiste comprobar.
