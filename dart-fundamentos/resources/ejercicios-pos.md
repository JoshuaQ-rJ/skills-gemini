# Ejercicios del POS: soluciones verificadas

Probadas con `dart run` en Dart 3.13; la salida coincide con el 'Resultado esperado' de la guía. Úsalas para revisar el trabajo de María Clara o para comparar. Al enseñar, da primero pistas y el algoritmo.

Las advertencias 'Dead code' y 'unnecessary_null_comparison' que muestra `dart analyze` en los ejercicios 1 a 3 son normales: los datos son literales y el analizador ya conoce el resultado. No son errores.

## Ejercicio 1. Abrir la caja

Practica: Variables, operadores lógicos, if/else, listas

Algoritmo: Validar en orden: caja ya abierta, rol (solo cajero o admin), base negativa, base mayor que baseMaxima. Si todo pasa: cajaAbierta = true, agregar 'APERTURA por <usuario> con base <base>' a movimientos y confirmar. Al final, estado con ternario y lista de movimientos.

```dart
void main() {
  String usuario = 'Laura';
  String rol = 'cajero'; // puede ser 'admin', 'cajero' o 'mesero'
  bool cajaAbierta = false;
  int baseInicial = 200000;
  const int baseMaxima = 10000000;
  List<String> movimientos = [];

  // Las validaciones van en orden: la primera que falle detiene la apertura.
  bool rolPermitido = rol == 'cajero' || rol == 'admin';

  if (cajaAbierta) {
    print('Error: ya hay una caja abierta');
  } else if (!rolPermitido) {
    print('Error: el rol $rol no puede abrir la caja');
  } else if (baseInicial < 0) {
    print('Error: la base no puede ser negativa');
  } else if (baseInicial > baseMaxima) {
    print('Error: la base supera el máximo permitido ($baseMaxima)');
  } else {
    cajaAbierta = true;
    movimientos.add('APERTURA por $usuario con base $baseInicial');
    print('Caja abierta por $usuario con una base de $baseInicial');
  }

  String estado = cajaAbierta ? 'ABIERTA' : 'CERRADA';
  print('Estado de la caja: $estado');
  print('Movimientos: $movimientos');
}
```

Casos 'Pruebe también':
- rol = 'mesero' -> Error de rol, CERRADA, []
- baseInicial = -5000 -> base negativa, CERRADA
- baseInicial = 10000001 -> supera el máximo, CERRADA
- cajaAbierta = true -> 'Error: ya hay una caja abierta', ABIERTA

## Ejercicio 2. Registrar la venta de la mesa 4

Practica: Map, for-in, continue, ternario, switch

Algoritmo: Recorrer pedido; si el producto no está en menu, avisar y continue. Imprimir cada línea y acumular subtotal. Propina con ternario (subtotal * 10 ~/ 100). switch sobre medioPago: efectivo (cambio o cuánto falta), debito (error si referencia es null), default (no válido).

```dart
void main() {
  Map<String, int> menu = {
    'Ajiaco': 28000,
    'Bandeja paisa': 32000,
    'Sancocho': 26000,
    'Limonada': 6000,
    'Jugo natural': 7000,
    'Gaseosa': 5000,
    'Postre del día': 9000,
  };
  Map<String, int> pedido = {
    'Bandeja paisa': 2,
    'Limonada': 3,
    'Postre del día': 1,
    'Cazuela': 1, // no está en el menú
  };
  bool incluirPropina = true; // propina voluntaria del 10 %
  String medioPago = 'efectivo'; // 'efectivo' o 'debito'
  int valorRecibido = 110000; // solo para efectivo
  String? referencia; // solo para débito

  int subtotal = 0;
  for (var producto in pedido.keys) {
    if (!menu.containsKey(producto)) {
      print('$producto: no existe en el menú, se omite');
      continue;
    }
    int cantidad = pedido[producto]!;
    int valorLinea = menu[producto]! * cantidad;
    print('$producto x$cantidad = $valorLinea');
    subtotal += valorLinea;
  }

  int propina = incluirPropina ? subtotal * 10 ~/ 100 : 0;
  int total = subtotal + propina;
  print('Subtotal: $subtotal · Propina: $propina · TOTAL: $total');

  switch (medioPago) {
    case 'efectivo':
      if (valorRecibido >= total) {
        print('Cambio: ${valorRecibido - total}');
      } else {
        print('Dinero insuficiente: faltan ${total - valorRecibido}');
      }
    case 'debito':
      if (referencia == null) {
        print('Error: falta la referencia del datáfono');
      } else {
        print('Pago con débito aprobado. Referencia: $referencia');
      }
    default:
      print('Medio de pago no válido');
  }
}
```

Casos 'Pruebe también':
- incluirPropina = false -> Propina 0, TOTAL 91000, Cambio 19000
- valorRecibido = 90000 -> 'Dinero insuficiente: faltan 10100'
- debito sin referencia -> error; con 'A-48213' -> aprobado
- 'bitcoin' -> 'Medio de pago no válido'

## Ejercicio 3. Venta con descuento

Practica: Acumuladores, condicionales anidados, switch, null safety

Algoritmo: Subtotal. Sumar porcentajes: >= 150000 (10), cupón (solo si no es null, con toUpperCase: CUMPLE 15, ESTUDIANTE 5, otro avisa), cliente frecuente (5). Guardar motivos. Si supera 20, avisar y dejar 20. descuento = subtotal * porcentaje ~/ 100.

```dart
void main() {
  Map<String, int> menu = {
    'Ajiaco': 28000,
    'Bandeja paisa': 32000,
    'Sancocho': 26000,
    'Limonada': 6000,
    'Jugo natural': 7000,
    'Gaseosa': 5000,
    'Postre del día': 9000,
  };
  Map<String, int> pedido = {
    'Ajiaco': 3,
    'Jugo natural': 4,
    'Postre del día': 2,
    'Bandeja paisa': 1,
  };
  String? cupon = 'CUMPLE'; // puede ser null si no hay cupón
  bool clienteFrecuente = true;
  const int descuentoMaximo = 20; // porcentaje máximo

  int subtotal = 0;
  for (var item in pedido.entries) {
    subtotal += menu[item.key]! * item.value;
  }
  print('Subtotal: $subtotal');

  int porcentaje = 0;
  List<String> motivos = [];

  if (subtotal >= 150000) {
    porcentaje += 10;
    motivos.add('compra mayor a 150.000 (10 %)');
  }

  if (cupon != null) {
    switch (cupon.toUpperCase()) {
      case 'CUMPLE':
        porcentaje += 15;
        motivos.add('cupón CUMPLE (15 %)');
      case 'ESTUDIANTE':
        porcentaje += 5;
        motivos.add('cupón ESTUDIANTE (5 %)');
      default:
        print('Aviso: el cupón $cupon no es válido');
    }
  }

  if (clienteFrecuente) {
    porcentaje += 5;
    motivos.add('cliente frecuente (5 %)');
  }

  if (porcentaje > descuentoMaximo) {
    print(
      'El descuento de $porcentaje % supera el máximo; se aplica $descuentoMaximo %',
    );
    porcentaje = descuentoMaximo;
  }

  int descuento = subtotal * porcentaje ~/ 100;
  int totalPagar = subtotal - descuento;
  print('Descuento: $descuento · TOTAL A PAGAR: $totalPagar');
  print('Motivos: ${motivos.isEmpty ? 'ninguno' : motivos.join(', ')}');
}
```

Casos 'Pruebe también':
- cupon = null -> 15 %, descuento 24300, total 137700
- 'estudiante' -> 20 % exacto, sin aviso de tope
- 'GRATIS' -> aviso de cupón no válido, 15 %
- clienteFrecuente = false -> 25 % y aviso de tope

## Ejercicio 4. Devolución de un producto

Practica: Validaciones, modificar y eliminar en un Map

Algoritmo: Total original. Validar que el producto esté en la venta, cantidad > 0 y <= vendida. Valor = precio * cantidad; si supera 30000 y no hay autorización, avisar sin cambios. Si no, restar en el Map, eliminar si queda en 0, registrar texto en devoluciones. Recalcular total.

```dart
void main() {
  Map<String, int> menu = {
    'Ajiaco': 28000,
    'Bandeja paisa': 32000,
    'Sancocho': 26000,
    'Limonada': 6000,
    'Jugo natural': 7000,
    'Gaseosa': 5000,
    'Postre del día': 9000,
  };
  Map<String, int> venta = {'Sancocho': 2, 'Gaseosa': 3, 'Postre del día': 2};
  String productoDevuelto = 'Gaseosa';
  int cantidadDevuelta = 1;
  String motivo = 'Producto en mal estado';
  bool autorizadoPorAdmin = false;
  const int limiteSinAutorizacion = 30000;
  List<String> devoluciones = [];

  int totalOriginal = 0;
  for (var item in venta.entries) {
    totalOriginal += menu[item.key]! * item.value;
  }
  print('Total original: $totalOriginal');

  if (!venta.containsKey(productoDevuelto)) {
    print('Error: $productoDevuelto no hace parte de la venta');
  } else if (cantidadDevuelta <= 0) {
    print('Error: la cantidad a devolver debe ser mayor que 0');
  } else if (cantidadDevuelta > venta[productoDevuelto]!) {
    print(
      'Error: solo se vendieron ${venta[productoDevuelto]} unidades de $productoDevuelto',
    );
  } else {
    int valorDevolucion = menu[productoDevuelto]! * cantidadDevuelta;
    if (valorDevolucion > limiteSinAutorizacion && !autorizadoPorAdmin) {
      print(
        'Aviso: la devolución de $valorDevolucion requiere autorización del administrador',
      );
    } else {
      venta[productoDevuelto] = venta[productoDevuelto]! - cantidadDevuelta;
      if (venta[productoDevuelto] == 0) {
        venta.remove(productoDevuelto);
      }
      devoluciones.add(
        '$cantidadDevuelta x $productoDevuelto ($motivo): $valorDevolucion',
      );
      print('Devolución registrada: $valorDevolucion');
    }
  }

  int nuevoTotal = 0;
  for (var item in venta.entries) {
    nuevoTotal += menu[item.key]! * item.value;
  }
  print('Venta actualizada: $venta');
  print('Nuevo total: $nuevoTotal');
  print('Devoluciones: $devoluciones');
}
```

Casos 'Pruebe también':
- 3 gaseosas -> Gaseosa desaparece, nuevo total 70000
- 5 gaseosas -> error de cantidad
- 'Ajiaco' -> no hace parte de la venta
- 2 sancochos (52000) sin autorización -> aviso; con autorización -> {Gaseosa: 3, Postre del día: 2}, total 33000

## Ejercicio 5. Jornada completa y cierre de caja

Practica: Listas paralelas, for con índice, totales por medio de pago

Algoritmo: porMedio en 0; for con índice acumulando por medio, total y venta mayor. Promedio con toStringAsFixed(0). Sumar egresos. Efectivo esperado = base + efectivo - egresos (débito y crédito NO entran a la caja). Comparar con lo contado: cuadrada, sobrante o faltante.

```dart
void main() {
  int baseInicial = 200000;
  // Las dos listas van en el mismo orden: la venta i se pagó con el medio i
  List<int> totales = [45000, 120000, 38000, 76000, 54000, 91000];
  List<String> medios = [
    'efectivo',
    'debito',
    'efectivo',
    'credito',
    'efectivo',
    'debito',
  ];
  Map<String, int> egresos = {
    'Compra de hielo': 15000,
    'Recarga de gas': 20000,
  };
  int efectivoContado = 300000;

  Map<String, int> porMedio = {'efectivo': 0, 'debito': 0, 'credito': 0};
  int totalVendido = 0;
  int ventaMayor = 0;

  for (var i = 0; i < totales.length; i++) {
    porMedio[medios[i]] = porMedio[medios[i]]! + totales[i];
    totalVendido += totales[i];
    if (totales[i] > ventaMayor) {
      ventaMayor = totales[i];
    }
  }

  int cantidadVentas = totales.length;
  double promedio = cantidadVentas > 0 ? totalVendido / cantidadVentas : 0;

  int totalEgresos = 0;
  for (var valor in egresos.values) {
    totalEgresos += valor;
  }

  // Solo el efectivo entra físicamente a la caja; débito y crédito no.
  int efectivoEsperado = baseInicial + porMedio['efectivo']! - totalEgresos;
  int diferencia = efectivoContado - efectivoEsperado;

  print(
    'Ventas en efectivo: ${porMedio['efectivo']} · débito: ${porMedio['debito']} · crédito: ${porMedio['credito']}',
  );
  print(
    'Total vendido: $totalVendido ($cantidadVentas ventas) · Venta mayor: $ventaMayor · Promedio: ${promedio.toStringAsFixed(0)}',
  );
  print('Egresos: $totalEgresos');
  print(
    'Efectivo esperado: $efectivoEsperado · Efectivo contado: $efectivoContado',
  );
  if (diferencia == 0) {
    print('Caja cuadrada');
  } else if (diferencia > 0) {
    print('Sobrante de $diferencia');
  } else {
    print('Faltante de ${-diferencia}');
  }
}
```

Casos 'Pruebe también':
- efectivoContado = 302000 -> Caja cuadrada
- 305000 -> Sobrante de 3000
- agregar una venta con add en ambas listas -> cambian totales y promedio
