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
