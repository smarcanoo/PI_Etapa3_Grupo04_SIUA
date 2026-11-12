from modelo import persistencia

catalogo_productos = {}
reporte_calidad = {}
lista_alertas = []

def inicializar_catalogo():
    """Carga los datos del CSV al arrancar el programa y guarda el reporte de limpieza."""
    global catalogo_productos, reporte_calidad
    catalogo_productos, reporte_calidad = persistencia.cargar_inventario()
    return reporte_calidad

def agregar_producto(codigo, nombre, categoria, stock, stock_minimo, precio_compra, precio_venta, fecha_vencimiento):
    """Agrega a memoria y ordena a persistencia que sobrescriba el CSV."""
    catalogo_productos[codigo] = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "stock": stock,
        "stock_minimo": stock_minimo,
        "precio_compra": precio_compra,
        "precio_venta": precio_venta,
        "fecha_vencimiento": fecha_vencimiento
    }
    persistencia.guardar_inventario(catalogo_productos)

def buscar_producto(codigo):
    return catalogo_productos.get(codigo, None)

def actualizar_stock(codigo, cantidad):
    """Actualiza stock en memoria y guarda el cambio en el CSV automáticamente."""
    if codigo in catalogo_productos:
        catalogo_productos[codigo]["stock"] += cantidad
        persistencia.guardar_inventario(catalogo_productos)
        return True
    return False

def obtener_catalogo():
    return catalogo_productos

def limpiar_alertas():
    lista_alertas.clear()

def agregar_alerta(codigo_producto, tipo_alerta, mensaje):
    lista_alertas.append({
        "codigo_producto": codigo_producto,
        "tipo_alerta": tipo_alerta,
        "mensaje": mensaje
    })

def obtener_alertas():
    return lista_alertas