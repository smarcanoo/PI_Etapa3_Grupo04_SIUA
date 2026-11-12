from datetime import datetime

def leer_cadena(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor: return valor
        print("Error: El campo no puede estar vacío.")

def leer_numero_positivo(mensaje, es_entero=False):
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = int(entrada) if es_entero else float(entrada)
            if valor > 0: return valor
            print("Error: El valor debe ser mayor a 0.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

def leer_fecha_opcional(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if not entrada: return ""
        try:
            datetime.strptime(entrada, "%Y-%m-%d")
            return entrada
        except ValueError:
            print("Error: Formato inválido. Use YYYY-MM-DD.")

def confirmar(mensaje):
    while True:
        resp = input(f"{mensaje} (s/n): ").strip().lower()
        if resp in ['s', 'n']: return resp == 's'
        print("Error: Responda con 's' o 'n'.")

def mostrar_mensaje(mensaje):
    print(f"\n>> {mensaje}")

def mostrar_error(mensaje):
    print(f"\n[X] ERROR: {mensaje}")

def mostrar_menu_principal():
    print("\n" + "="*50)
    print(" DISTRIBUIDORA INDUSTRIAL DEL PACÍFICO S.A.")
    print("="*50)
    print("1. Registrar nuevo producto en bodega")
    print("2. Actualizar stock de mercancía")
    print("3. Realizar venta en caja")
    print("4. Generar y consultar alertas")
    print("5. Consultar catálogo de inventario (Filtros)")
    print("6. Consultar resumen de ventas del día")
    print("7. Generar reportes gráficos")
    print("8. Salir del sistema")
    print("="*50)
    return input("Seleccione una opción (1-8): ").strip()

def mostrar_menu_filtros():
    print("\nOpciones de visualización:")
    print("1. Ordenar por nombre (Ascendente)")
    print("2. Ordenar por stock (Descendente)")
    print("3. Filtrar solo productos con stock crítico")
    print("4. Filtrar por categoría")
    print("5. Mostrar todos sin filtro")
    return input("Seleccione una opción (1-5): ").strip()

def mostrar_inventario_lista(lista_productos):
    if not lista_productos:
        mostrar_error("No hay productos que coincidan con la búsqueda.")
        return
    print("\n" + "="*85)
    print(f"{'CÓDIGO':<8} | {'NOMBRE':<20} | {'CATEGORÍA':<15} | {'STOCK':<8} | {'PRECIO V.':<10} | {'VENCE'}")
    print("-" * 85)
    for prod in lista_productos:
        alerta_stock = "*" if prod['stock'] <= prod['stock_minimo'] else " "
        stock_str = f"{prod['stock']} {alerta_stock}"
        vence = prod['fecha_vencimiento'] if prod['fecha_vencimiento'] else "N/A"
        print(f"{prod['codigo']:<8} | {prod['nombre']:<20} | {prod['categoria']:<15} | {stock_str:<8} | ₡{prod['precio_venta']:<9.2f} | {vence}")
    print("-" * 85)

def mostrar_ventas(ventas):
    if not ventas:
        mostrar_error("No hay ventas registradas.")
        return
    print("\n" + "="*60)
    print(f"{'FACTURA':<10} | {'FECHA':<20} | {'IMPUESTOS':<10} | {'TOTAL'}")
    print("-" * 60)
    for v in ventas:
        print(f"#{v['numero_factura']:<9} | {v['fecha']:<20} | ₡{v['total_impuestos']:<9.2f} | ₡{v['total_general']:.2f}")
    print("=" * 60)

def mostrar_alertas(alertas):
    if not alertas:
        mostrar_mensaje("No hay alertas activas. Todo está en orden.")
        return
    print("\n" + "!"*60)
    print(" CENTRO DE ALERTAS")
    print("!"*60)
    for a in alertas:
        tipo = "[STOCK BAJO]" if a['tipo_alerta'] == "stock_bajo" else "[VENCIMIENTO]"
        print(f"{tipo:<15} Código: {a['codigo_producto']:<6} -> {a['mensaje']}")
    print("!"*60)