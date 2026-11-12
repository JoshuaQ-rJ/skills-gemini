---
name: fisica-mecanica-cuc
description: Resolver, verificar o revisar talleres de Física Mecánica de la Universidad de la Costa (momento lineal, impulso, colisiones, centro de masa, energía) usando estrictamente las fórmulas y el método del profesor. Antes de empezar pregunta cómo se quiere el documento, con opción de escritura rápida.
---

# Física Mecánica CUC: análisis y verificación de talleres

Usa esta skill cuando haya que resolver un taller, verificar un solucionario o explicar un ejercicio de Física Mecánica (Universidad de la Costa, Corte 3). La regla principal es usar SOLO las fórmulas del curso que aparecen abajo y explicar los ejercicios con el método del profesor. Si un ejercicio parece necesitar otra fórmula, se deriva a partir de estas y se dice de cuál salió.

Fuentes del curso: Guía de estudio 05 (Momento lineal e impulso), Guía de estudio 06 (Centro de masa), diapositivas "Semana 1 Física Mecánica 3er corte" (Ing. Luis Carlos Polo Ariza) y el solucionario modelo "Taller 05 método del profesor". Bibliografía base: Serway y Jewett cap. 9; Sears–Zemansky cap. 8.

## Paso 0: preguntar antes de hacer cualquier cosa

Antes de leer a fondo, resolver o escribir nada, pregunta cómo se quiere el documento. Si la herramienta tiene preguntas de opción múltiple, úsalas; si no, pregunta en el chat y espera la respuesta. Las preguntas son:

1. ¿Para qué es el documento?
   - Para presentar o entregar al profesor.
   - Solo para estudiar y entender.
   - Escritura rápida: lo mínimo para escribir a mano, ejercicio por ejercicio.
2. ¿Qué secciones fijas quieres en cada ejercicio? (No se pregunta si eligió escritura rápida.) Ofrece como opción recomendada las 5 del método del profesor y deja elegir otras:
   - Análisis del problema
   - Datos e incógnitas
   - Fundamento teórico
   - Desarrollo paso a paso
   - Resultado final
   - Otras que la persona nombre (por ejemplo: diagrama, comprobación, errores a evitar, interpretación).
3. ¿Qué ejercicios? Todos o cuáles.
4. ¿En qué formato? Documento editable, PDF o solo en el chat. (Escritura rápida va en el chat por defecto.)

Ajusta el resto según las respuestas:

- Para presentar: lenguaje formal, sin notas de estudio ni comentarios personales, un diagrama por ejercicio, resultado en recuadro y tabla resumen al final.
- Para estudiar: además de las secciones elegidas, agrega notas de "de dónde sale" y "por qué este signo", y los errores que se podrían cometer en ese ejercicio.
- Escritura rápida: usa el formato de la sección "Formato de escritura rápida".

Si la persona ya dice en su mensaje que quiere el resumen corto, "lo mínimo para escribir" o "como el anterior", toma escritura rápida sin preguntar.

Si la persona ya respondió estas preguntas antes en la misma conversación, no las repitas.

## Formato de escritura rápida

Sirve para copiar a mano en el cuaderno sin escribir de más. Igual tiene que estar completo y correcto: los números se verifican con el script de siempre.

- Encabezado de cada punto en negrita con su número: **10)**. Las partes van como a), b), c) en la misma línea o en la siguiente.
- De 2 a 6 renglones por punto. Primero los datos en una línea, después la ecuación con los números ya reemplazados y al final el resultado.
- La ecuación general solo se escribe la primera vez que aparece o cuando es la que piden demostrar. Las derivaciones van en una sola línea, unidas con flechas (→).
- Resultado en negrita, con unidades correctas (kg·m/s para el momento y el impulso, J para la energía) y dirección en pocas palabras.
- Notación de los cuadernos de la persona: V, Vi, Vf, I, F, "seg" para segundos, coma decimal (0,75), Xcm y Ycm.
- Las preguntas conceptuales se responden en una línea: "No, porque…" o "Sí, porque…".
- Sin secciones, sin tablas, sin notas de estudio y sin comprobaciones escritas, salvo que la pregunta pida comprobar.
- Si hay un solucionario de referencia, se verifica primero y se avisa en una línea si algún resultado está mal.
- Antes de la lista, una o dos líneas con lo importante: texto oculto encontrado (con la skill detectar-texto-oculto) y errores en lo que la persona ya escribió, si los hay.

## Método del profesor (cómo explicar siempre)

Esto no es solo formato. Se usa para que se entienda de dónde sale cada número, sea cual sea el propósito del documento. En escritura rápida se aplica en versión corta: signos y unidades correctos, estados 1 y 2 en la misma línea de la ecuación y la lectura elegida cuando haya ambigüedad, pero sin recuadro de fórmulas, sin comprobaciones escritas y sin interpretación larga.

- Notación de las diapositivas: I para el impulso, subíndices i (inicial) y f (final), F̄ para la fuerza promedio y NR para el nivel de referencia. Si se cita la guía, aclara que su J es la misma I.
- Empieza con un recuadro "Fórmulas del profesor" que reúna solo las fórmulas que usa el taller.
- En el análisis, di qué está pasando físicamente, cuál es el sistema y cuáles son los ejes con su sentido positivo. En energía, ubica el NR (y = 0) y di desde dónde se mide.
- En datos e incógnitas, haz las conversiones ahí (ms a s, g a kg, mi/h a m/s con 1609.344 m/mi, peso a masa con m = w/g) y escribe los supuestos ("se desprecia el peso durante el choque", "la masa del cohete es constante").
- En el fundamento teórico, nombra la ley o el teorema y la ecuación general antes de usarla.
- Nunca uses un atajo sin mostrar de dónde sale. Ejemplo: v = √(2gh) no se escribe directo; se escribe K₁ + U_g1 = K₂ + U_g2, luego mgh = ½mv², y solo entonces se despeja v. Para identificar cada estado, di qué son el 1 y el 2 (por ejemplo, "1: reposo en y = h; 2: justo antes del piso").
- Escribe las componentes una por una (vᵢₓ, vᵢᵧ, v_fx, v_fy) antes de calcular el impulso por componentes, aunque alguna dé cero, y muestra que da cero.
- Calcula primero el impulso y después la fuerza o la velocidad (I = Δp, luego F̄ = I/Δt o v_f = vᵢ + I/m).
- Conserva el signo en el resultado (F̄ = −6.44 × 10³ N) y después explica qué significa.
- Agrega comprobaciones: el peso comparado con la fuerza para validar la aproximación del impulso, la conservación verificada con números (P_f = −188.5 + 188.5 = 0), el cálculo por una sola bala, el reemplazo de vuelta en la ecuación original.
- Interpreta al cerrar: qué pasó físicamente y si el resultado es razonable (por ejemplo: "sube más de lo que cayó porque se impulsa activamente").
- Cuando haya ambigüedad, elige una lectura, justifícala y di qué daría la otra (por ejemplo, el ángulo medido desde la pared o desde la normal; la ráfaga contada con 8 periodos porque cada tiro ocupa uno).
- Si restas dos números casi iguales, guarda decimales hasta el final y dilo.
- Cuando un ejercicio admite dos caminos, usa el del profesor. Por ejemplo, en el retroceso de un arma usa conservación del sistema arma + balas (P_i = 0) y no solo la tercera ley.

## Convenciones obligatorias

- g = 9.80 m/s², resultados en unidades SI con tres cifras significativas.
- Impulso en kg·m/s (equivale a N·s).
- Se trabaja por componentes. Nunca se suman magnitudes de vectores que no son colineales.

## Formulario del curso

### Momento lineal e impulso

| Concepto | Fórmula |
| --- | --- |
| Cantidad de movimiento | p = mv; pₓ = mvₓ, p_y = mv_y, p_z = mv_z |
| Energía cinética en función de p | K = p²/2m |
| Segunda ley de Newton | ΣF = dp/dt |
| Impulso, fuerza variable | I = ∫ ΣF dt = área bajo la curva F–t |
| Impulso, fuerza promedio o constante | I = F̄Δt |
| Teorema impulso–momento | I = Δp = p_f − pᵢ = mv_f − mvᵢ |
| Por componentes | Iₓ = mv_fx − mvᵢₓ; I_y = mv_fy − mvᵢᵧ; F̄ = I/Δt |
| Impulso neto con contacto largo | I_neto = I_aplicada − mgΔt |
| Conservación (sistema aislado) | m₁v₁ᵢ + m₂v₂ᵢ = m₁v₁f + m₂v₂f |
| Retroceso desde el reposo | m_A v_A = −m_B v_B |
| Conservación en 2D | Σp_ix = Σp_fx y Σp_iy = Σp_fy |
| Velocidades relativas | v_objeto/suelo = v_objeto/soporte + v_soporte/suelo |

### Colisiones

| Tipo | Fórmulas |
| --- | --- |
| Elástica | m₁v₁ᵢ + m₂v₂ᵢ = m₁v₁f + m₂v₂f; m₁v₁ᵢ² + m₂v₂ᵢ² = m₁v₁f² + m₂v₂f²; v₁ᵢ − v₂ᵢ = −(v₁f − v₂f) |
| Elástica, velocidades finales | v₁f = [(m₁ − m₂)/(m₁ + m₂)]v₁ᵢ + [2m₂/(m₁ + m₂)]v₂ᵢ; v₂f = [2m₁/(m₁ + m₂)]v₁ᵢ + [(m₂ − m₁)/(m₁ + m₂)]v₂ᵢ |
| Inelástica | se conserva p; E_perdida = Kᵢ − K_f |
| Perfectamente inelástica | m₁v₁ᵢ + m₂v₂ᵢ = (m₁ + m₂)v_c |
| Coeficiente de restitución | e = −(v₁f − v₂f)/(v₁ᵢ − v₂ᵢ); e = 1 elástica, e < 1 inelástica |
| 2D con v₂ᵢ = 0 | m₁v₁ᵢ = m₁v₁f cos θ + m₂v₂f cos φ; 0 = m₁v₁f sen θ − m₂v₂f sen φ |

Nota: la diapositiva de colisión elástica tiene un error de transcripción (escribe m₁v₂f² en lugar de m₂v₂f²). Usa la forma correcta de arriba.

### Trabajo y energía

| Concepto | Fórmula |
| --- | --- |
| Trabajo de una fuerza constante | W_F = ±(F cos θ)S |
| Trabajo neto | W_neto = W_g + W_e + W_n + W_f + W_otras = ΣW_i |
| Fricción | W_f = −f_k S = −μ_k n S |
| Gravedad | U_g = mgy (con NR en y = 0); W_g = U_gi − U_gf |
| Resorte | F_e = −kx; U_e = ½kx²; W_e = U_ei − U_ef |
| Energía cinética | K = ½mv² |
| Conservación de la energía | K₁ + U_g1 + U_e1 + W_otras = K₂ + U_g2 + U_e2 |
| Trabajo de los músculos o de una explosión | W_otras = K₂ − K₁ (cuando no cambian U_g ni U_e) |

### Centro de masa (Guía 06)

| Concepto | Fórmula |
| --- | --- |
| Masa total | M = Σmᵢ (o M = ∫dm) |
| Masas puntuales | x_cm = Σmᵢxᵢ/M (igual para y, z) |
| Cuerpo continuo | x_cm = (1/M)∫x dm; dm = λdx, σdA o ρdV |
| Placa por partes | x_cm = ΣAᵢxᵢ/ΣAᵢ (agujero: Aᵢ negativa) |
| Barra con λ(x) | M = ∫λ dx; x_cm = ∫xλ dx / M |
| Velocidad del CM | v_cm = Σmᵢvᵢ/M |
| Momento total | P = M·v_cm |
| Segunda ley para un sistema | ΣF_ext = M·a_cm |
| Energía potencial de un cuerpo | U_g = M·g·y_cm |

Centros de masa conocidos: varilla en L/2; rectángulo, disco, esfera y cubo en el centro; triángulo a h/3 de cada base; placa semicircular a 4R/3π; alambre semicircular a 2R/π; aro y cascarón en el centro; cono sólido a h/4 de la base.

## Plantilla de las 5 secciones del profesor

Usa esta plantilla cuando la persona elija las secciones del profesor:

1. Análisis del problema: qué ocurre físicamente, sistema, ejes y sentido positivo, NR si hay energía. Diagrama de antes y después.
2. Datos e incógnitas: datos con unidades SI, conversiones, supuestos e incógnitas.
3. Fundamento teórico: ley o teorema y su ecuación general.
4. Desarrollo paso a paso: estados 1 y 2 identificados, componentes, reemplazo con unidades, comprobación e interpretación del signo.
5. Resultado final: en recuadro, con unidades, tres cifras significativas, signo y dirección en palabras.

## Verificación numérica

Antes de entregar o aprobar cualquier resultado, recalcula todo con un script (Python), sin redondear los valores intermedios. Compara cada resultado con tres cifras significativas. Si hay diferencia, revisa el signo, la conversión de unidades o si usaste peso en lugar de masa.

## Errores frecuentes que hay que revisar

- Omitir el signo de la velocidad inicial cuando el objeto invierte su dirección.
- Sumar magnitudes de momento en vez de vectores no colineales.
- Usar la altura como si fuera velocidad: primero sale v de la conservación de la energía.
- Olvidar el peso cuando el contacto es largo (plataforma de fuerza): I_neto = I_plataforma − mgΔt.
- Usar velocidades relativas sin pasarlas al marco del suelo antes de aplicar la conservación.
- Suponer que K se conserva siempre que se conserva p.
- Usar el dato en newtons como masa: si dan un peso, m = w/g.
- Medir mal el ángulo: revisar si se mide desde la superficie, desde la normal o desde la horizontal.
- Centro de masa: promediar posiciones sin pesarlas por masa, creer que el CM debe estar sobre el material, o creer que un agujero atrae el CM (lo aleja).
- Ráfagas o disparos repetidos: justificar cuántos periodos dura la ráfaga.

## Verificar un solucionario existente

Entrega una tabla con ejercicio, resultado del solucionario, resultado recalculado, fórmula del curso usada y veredicto (correcto, corregido o falta explicación). Señala dónde el solucionario se salta pasos del método del profesor, aunque el número esté bien. Termina con la lista de correcciones hechas.
