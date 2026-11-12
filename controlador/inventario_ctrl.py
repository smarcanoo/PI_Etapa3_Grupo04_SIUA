from modelo import producto
import vista.consola as consola

def registrar_producto():
    consola.mostrar_mensaje("--- REGISTRAR PRODUCTO ---")
    codigo = consola.leer_cadena("Ingrese el código del producto: ")
    
    if producto.buscar_producto(codigo):
        consola.mostrar_error("El código ya existe en el catálogo.")
        return
        
    nombre = consola.leer_cadena("Nombre del producto: ")
    categoria = consola.leer_cadena("Categoría: ")
    stock = consola.leer_numero_positivo("Stock inicial: ", es_entero=True)
    stock_minimo = consola.leer_numero_positivo("Stock mínimo: ", es_entero=True)
    precio_compra = consola.leer_numero_positivo("Precio de compra: ")
    precio_venta = consola.leer_numero_positivo("Precio de venta sugerido: ")
    vencimiento = consola.leer_fecha_opcional("Fecha de vencimiento (YYYY-MM-DD) o [Enter]: ")
    
    producto.agregar_producto(codigo, nombre, categoria, stock, stock_minimo, precio_compra, precio_venta, vencimiento)
    consola.mostrar_mensaje(f"Producto '{nombre}' registrado y guardado exitosamente.")

def actualizar_stock():
    consola.mostrar_mensaje("--- ACTUALIZAR STOCK ---")
    codigo = consola.leer_cadena("Ingrese el código del producto a actualizar: ")
    prod = producto.buscar_producto(codigo)
    
    if not prod:
        consola.mostrar_error("Producto no encontrado.")
        return
        
    consola.mostrar_mensaje(f"Producto: {prod['nombre']} | Stock actual: {prod['stock']}")
    cantidad = consola.leer_numero_positivo("Ingrese la cantidad de unidades a sumar: ", es_entero=True)
    
    if producto.actualizar_stock(codigo, cantidad):
        consola.mostrar_mensaje("Inventario actualizado y guardado correctamente.")

def consultar_inventario():
    catalogo = producto.obtener_catalogo()
    lista_productos = list(catalogo.values())
    
    opcion = consola.mostrar_menu_filtros()
    
    if opcion == "1":
        lista_productos.sort(key=lambda x: x['nombre'].lower())
    elif opcion == "2":
        lista_productos.sort(key=lambda x: x['stock'], reverse=True)
    elif opcion == "3":
        lista_productos = [p for p in lista_productos if p['stock'] <= p['stock_minimo']]
    elif opcion == "4":
        cat = consola.leer_cadena("Ingrese la categoría a buscar: ").lower()
        lista_productos = [p for p in lista_productos if cat in p['categoria'].lower()]
        
    consola.mostrar_inventario_lista(lista_productos)