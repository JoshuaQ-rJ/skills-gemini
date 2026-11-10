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
