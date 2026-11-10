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
