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
