---
name: dart-fundamentos
description: Teaches and writes beginner Dart 3 code (variables, types, operators, null safety, if/else, ternary, switch, List, Map, for/while/do-while loops) using a Colombian restaurant POS context (open/close cash register, tips, discounts, returns). Use when the user mentions Dart, DartPad, .dart files, the POS restaurante exercises, or asks to explain, review or solve Dart exercises. Responde en español.
---

# Dart fundamentos (POS restaurante)

Skill para enseñar Dart desde cero y resolver o revisar los ejercicios de la guía "Introducción al lenguaje Dart · Proyecto POS restaurante". Todo lo técnico está verificado contra dart.dev y probado con Dart 3.13 (estable desde agosto de 2026).

## Cómo responder

María Clara está aprendiendo programación (bootcamp Riwi y carrera de sistemas). Por eso:

1. Responde en español, como profesora experta: explica desde cero, paso a paso y con ejemplos del restaurante (menú, mesas, caja, medios de pago). Ella aprende mejor cuando entiende el porqué.
2. Apoya cada regla en la documentación oficial y cita el enlace de dart.dev cuando expliques un concepto (lista en `resources/lenguaje.md`).
3. Los ejercicios de la guía son evaluados. Si pide ayuda con uno, primero da pistas y el algoritmo en pasos; entrega el código completo solo si lo pide o si ya intentó. Cuando revises su código, señala el error, por qué pasa y cómo arreglarlo, sin reescribirlo todo.
4. Todo el código debe correr en DartPad (dartpad.dev) dentro de `void main() { }`. DartPad no lee teclado (no hay `stdin`), así que los datos van en variables.
5. Verifica antes de entregar. En Antigravity usa la terminal: si `dart --version` falla, pide a la usuaria instalar el SDK (https://dart.dev/get-dart) y luego ejecuta `dart run archivo.dart` y `dart analyze`; compara con el "Resultado esperado" de la guía. Si no puedes ejecutar, dilo.

## Reglas de la guía (respétalas siempre)

- Dinero en `int` (pesos colombianos, sin centavos). Porcentaje sin decimales: `total * 10 ~/ 100`. Nunca `total * 0.10` asignado a `int` (error de tipo) ni `/` (siempre devuelve `double`).
- Nombres en lowerCamelCase que digan qué guardan (`baseInicial`, `totalVenta`). Constantes también en lowerCamelCase (`const int baseMaxima`).
- Dart 3: un `case` con cuerpo no necesita `break`; un `case` vacío sí cae al siguiente.
- Los mensajes de salida deben coincidir con el "Resultado esperado" (mismo texto, separador ` · `, `%` con espacio antes).
- Criterios de evaluación: corre sin errores (20 %), resultado esperado (30 %), casos "Pruebe también" (30 %), nombres, comentarios y orden (20 %).

## Chuleta de Dart 3

```dart
void main() {
  // Variables
  String nombre = 'La Buena Mesa';
  int mesas = 12;               // entero
  double propinaPct = 0.10;     // decimal
  bool cajaAbierta = false;
  var ciudad = 'Bogotá';        // tipo inferido: String (no puede cambiar de tipo)
  final horaApertura = '07:00'; // se asigna una sola vez (en ejecución)
  const int baseMaxima = 10000000; // conocido al compilar, nunca cambia

  // Interpolación
  print('Restaurante: $nombre, propina ${propinaPct * 100} %');

  // Operadores: + - * / ~/ %   == != > < >= <=   && || !   += -= ++ --
  int total = 87000;
  print(total ~/ 7); // 12428 (división entera)
  print(total % 7);  // 4 (residuo)

  // Null safety
  String? observacion;                       // puede ser null
  print(observacion ?? 'Sin observaciones'); // valor por defecto
  observacion ??= 'Sin cebolla';             // asigna solo si es null
  Map<String, int> menu = {'Ajiaco': 28000};
  int? precio = menu['Cazuela'];             // clave que no existe: null
  if (menu.containsKey('Ajiaco')) {
    int precioAjiaco = menu['Ajiaco']!;      // ! solo si estás segura
  }

  // Condicionales
  String tipo = total >= 150000 ? 'Venta grande' : 'Venta normal';
  switch ('debito') {
    case 'efectivo':
      print('Calcular cambio');
    case 'debito' || 'credito':             // patrón "o" (Dart 3)
      print('Registrar referencia');
    default:
      print('Medio de pago no válido');
  }
  // Expresión switch (devuelve un valor)
  int descuento = switch ('CUMPLE') {
    'CUMPLE' => 15,
    'ESTUDIANTE' => 5,
    _ => 0,
  };

  // Listas y Map
  List<String> pedido = ['Ajiaco', 'Limonada'];
  pedido.add('Postre del día');
  for (var i = 0; i < pedido.length; i++) {
    print('${i + 1}. ${pedido[i]}');
  }
  for (var item in menu.entries) {
    print('${item.key}: ${item.value}');
  }

  // Ciclos: for, for-in, while, do-while; break termina, continue salta
}
```

Lo completo (Set, spread `...`, collection if/for, elementos null-aware `?valor`, funciones, if-case, `when`, `late`, `toStringAsFixed`, `join`, etc.) está en `resources/lenguaje.md`. Léelo cuando la pregunta vaya más allá de la chuleta.

## Ejercicios de la guía

Los cinco ejercicios (abrir caja, venta de la mesa 4, descuento, devolución, cierre de caja) con su enunciado resumido, algoritmo, solución probada y salida de cada caso "Pruebe también" están en `resources/ejercicios-pos.md` (los archivos ejecutables están en `examples/ej1.dart` a `examples/ej5.dart`). Úsalo para revisar el trabajo de ella o comparar resultados; no lo pegues entero sin que lo pida.

## Errores frecuentes que debes detectar

| Síntoma | Causa | Arreglo |
|---|---|---|
| `A value of type 'double' can't be assigned to a variable of type 'int'` | `total * 0.10` o `total / n` en un `int` | `total * 10 ~/ 100`, `~/`, o `.round()` |
| `The operator '*' can't be unconditionally invoked because the receiver can be 'null'` | Leer un Map da `int?` | Verificar con `containsKey` y usar `!` |
| `RangeError (index)` | Índice fuera de 0..length-1 | Ciclo con `i < lista.length` |
| Ciclo infinito | La condición del `while` nunca cambia | Aumentar el contador o quitar elementos |
| `if (rol = 'admin')` no compila | `=` es asignación | Usar `==` |
| Advertencia "Dead code" o "unnecessary_null_comparison" en DartPad | Los datos son literales y el analizador ya sabe el resultado | Es normal en estos ejercicios; desaparece al cambiar los datos. No es un error |
| `print(precio ?? 'No encontrado')` mezcla tipos | El resultado es `Object` | Válido para imprimir; para operar, usar un `int` por defecto (`?? 0`) |

## Ojo con la guía

En el ejercicio 5 el PDF dice que las ventas con débito y crédito "no entran" como efectivo a la caja (la palabra "no" está en negrita y se pierde al extraer el texto). El resultado esperado lo confirma: efectivo esperado = base + ventas en efectivo − egresos = 302000.
