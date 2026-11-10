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
