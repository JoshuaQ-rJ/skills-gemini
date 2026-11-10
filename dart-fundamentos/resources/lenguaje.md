# Referencia de Dart 3 para principiantes

Versión verificada: Dart 3.13 (estable, agosto de 2026). Cada sección enlaza la página oficial de dart.dev para citarla al explicar.

## Contenido
1. Herramientas
2. Variables y tipos
3. Operadores
4. Null safety
5. Condicionales y patrones
6. Colecciones (List, Set, Map)
7. Ciclos
8. Funciones básicas
9. Métodos útiles
10. Estilo (Effective Dart)

## 1. Herramientas
- DartPad: https://dart.dev/tools/dartpad. Pegar código, Run, ver consola. No admite `stdin` ni `dart:io` para leer teclado.
- SDK local: https://dart.dev/get-dart. Comandos: `dart run archivo.dart`, `dart analyze`, `dart format .`, `dart create nombre_proyecto`.
- Todo programa empieza en `void main() { }`.

## 2. Variables y tipos
Docs: https://dart.dev/language/variables y https://dart.dev/language/built-in-types
- Tipos básicos: `int`, `double`, `num` (padre de ambos), `String`, `bool`.
- `var`: infiere el tipo y luego no cambia. `final`: se asigna una vez, en ejecución. `const`: constante de compilación.
- `late`: variable no nula que se inicializa después; si se lee antes, error en ejecución.
- Interpolación: `'$variable'` y `'${expresion}'`. Texto multilínea con `'''...'''`.
- Conversión: `int.parse('5000')`, `double.parse('0.1')`, `int.tryParse('x')` (da null si falla), `5000.toString()`, `9300.0.toInt()`.

## 3. Operadores
Docs: https://dart.dev/language/operators
- Aritméticos: `+ - * / ~/ %`. `/` siempre devuelve `double`; `~/` división entera.
- Asignación: `= += -= *= ~/= ??=`; incremento `++ --`.
- Comparación: `== != > < >= <=`. Lógicos: `&& || !`.
- Null-aware: `??`, `??=`, `?.`, `!`.
- Ternario: `condicion ? siVerdad : siFalso`.
- Cascada: `lista..add('a')..add('b')` (llama varios métodos sobre el mismo objeto).

## 4. Null safety
Docs: https://dart.dev/null-safety y https://dart.dev/null-safety/understanding-null-safety
- Los tipos no aceptan null salvo que lleven `?` (`String?`).
- Después de `if (x != null)` una variable local se "promueve" a no nula. Los campos públicos de una clase no se promueven; copiarlos a una variable local.
- `!` afirma que no es null; si lo es, el programa se detiene.
- Leer un Map (`menu['Ajiaco']`) siempre devuelve tipo nulable.

## 5. Condicionales y patrones
Docs: https://dart.dev/language/branches y https://dart.dev/language/patterns
- `if / else if / else`. Llaves siempre, salvo un `if` de una sola línea sin `else`.
- `switch` (sentencia): sin `break` en Dart 3; caso vacío cae al siguiente; `default` o `_` cuando nada coincide; patrones `'a' || 'b'`, rangos `>= 1 && <= 9`, guardas `when`.
- Expresión `switch`: `var x = switch (valor) { 'a' => 1, _ => 0 };` (sin `case`, con `=>`, separado por comas).
- if-case: `if (dato case int n) { ... }`.
- Exhaustividad: con enums o clases `sealed` el compilador exige cubrir todos los casos.

## 6. Colecciones
Docs: https://dart.dev/language/collections, https://api.dart.dev/dart-core/List-class.html, https://api.dart.dev/dart-core/Map-class.html
- List: `add`, `addAll`, `insert`, `remove`, `removeAt`, `removeLast`, `contains`, `indexOf`, `length`, `isEmpty`, `isNotEmpty`, `first`, `last`, `sort`, `reversed`, `sublist`.
- Set: `{'a', 'b'}` elementos únicos; vacío con `<String>{}` (porque `{}` solo es un Map).
- Map: `menu['x'] = 1` agrega o modifica; `remove`, `containsKey`, `containsValue`, `keys`, `values`, `entries`, `length`, `putIfAbsent`, `update`.
- Spread `...lista` y `...?listaNulable`; collection if `[if (c) 'x']`; collection for `[for (var n in nums) n * 2]`; elemento null-aware `[?valorNulable]` (Dart 3.8+).

## 7. Ciclos
Docs: https://dart.dev/language/loops
- `for (var i = 0; i < n; i++)` cuando importa la posición.
- `for (var x in coleccion)` para recorrer todo.
- `while (cond)` puede no ejecutarse nunca; `do { } while (cond);` se ejecuta al menos una vez.
- `break` sale del ciclo; `continue` salta a la siguiente vuelta.
- `lista.forEach((x) => print(x));` existe, pero Effective Dart recomienda `for-in`.
- No modificar un Map o List mientras se recorre con for-in (lanza `ConcurrentModificationError`); recorrer una copia (`.toList()`).

## 8. Funciones básicas
Docs: https://dart.dev/language/functions
```dart
int calcularPropina(int subtotal, {int porcentaje = 10}) {
  return subtotal * porcentaje ~/ 100;
}

int subtotalDe(Map<String, int> pedido, Map<String, int> menu) =>
    pedido.entries.fold(0, (suma, item) => suma + menu[item.key]! * item.value);
```
Parámetros posicionales, nombrados `{}` (con `required` o valor por defecto) y opcionales `[]`.

## 9. Métodos útiles
- String: `toUpperCase`, `toLowerCase`, `trim`, `contains`, `startsWith`, `split`, `padLeft`, `isEmpty`.
- Números: `toStringAsFixed(0)`, `round()`, `abs()`, `clamp(0, 20)`.
- Iterables: `join(', ')`, `where`, `map`, `reduce`, `fold`, `any`, `every`, `toList()`.

## 10. Estilo (Effective Dart)
Docs: https://dart.dev/effective-dart/style
- UpperCamelCase: clases, enums, typedefs. lowerCamelCase: variables, funciones, constantes. lowercase_with_underscores: archivos y paquetes.
- Líneas de 80 caracteres o menos; usar `dart format`.
- Llaves en todo control de flujo.
