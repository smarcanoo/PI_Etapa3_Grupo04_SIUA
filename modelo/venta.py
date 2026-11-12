from modelo import persistencia

registro_ventas = []

def registrar_venta(numero_factura, fecha, productos_vendidos, total_impuestos, total_general):
    """Guarda la venta en memoria y escribe cada línea en el archivo CSV de ventas."""
    venta = {
        "numero_factura": numero_factura,
        "fecha": fecha,
        "productos_vendidos": productos_vendidos,
        "total_impuestos": total_impuestos,
        "total_general": total_general
    }
    registro_ventas.append(venta)
    
    for prod in productos_vendidos:
        persistencia.guardar_linea_venta(
            numero_factura=numero_factura,
            fecha=fecha,
            codigo_producto=prod["codigo"],
            cantidad=prod["cantidad"],
            subtotal=prod["subtotal"],
            impuestos=total_impuestos,
            total=total_general
        )

def obtener_ventas():
    return registro_ventas