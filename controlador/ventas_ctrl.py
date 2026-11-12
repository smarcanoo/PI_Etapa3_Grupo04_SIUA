from modelo import producto
from modelo import venta
import vista.consola as consola
from datetime import datetime

def realizar_venta():
    consola.mostrar_mensaje("--- NUEVA VENTA ---")
    venta_activa = True
    productos_vendidos = []
    subtotal_venta = 0.0
    
    while venta_activa:
        codigo = consola.leer_cadena("Ingrese el código del producto: ")
        prod = producto.buscar_producto(codigo)
        
        if not prod:
            consola.mostrar_error("El código no existe.")
        else:
            cantidad = consola.leer_numero_positivo(f"Cantidad a vender de '{prod['nombre']}': ", es_entero=True)
            if cantidad <= prod['stock']:
                subtotal_prod = cantidad * prod['precio_venta']
                subtotal_venta += subtotal_prod
                
                productos_vendidos.append({
                    "codigo": codigo,
                    "cantidad": cantidad,
                    "subtotal": subtotal_prod
                })
                producto.actualizar_stock(codigo, -cantidad)
                consola.mostrar_mensaje(f"Agregado. Subtotal parcial: ₡{subtotal_venta:.2f}")
            else:
                consola.mostrar_error(f"Stock insuficiente. Solo quedan {prod['stock']} unidades.")
                
        if not consola.confirmar("¿Desea agregar otro producto a esta factura?"):
            venta_activa = False
            
    if productos_vendidos:
        impuestos = subtotal_venta * 0.13
        total = subtotal_venta + impuestos
        num_factura = len(venta.obtener_ventas()) + 1
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        venta.registrar_venta(num_factura, fecha_actual, productos_vendidos, impuestos, total)
        consola.mostrar_mensaje("Venta procesada y respaldada en archivo con éxito.")
        consola.mostrar_mensaje(f"Subtotal: ₡{subtotal_venta:.2f} | Impuestos: ₡{impuestos:.2f} | TOTAL: ₡{total:.2f}")

def consultar_ventas():
    consola.mostrar_ventas(venta.obtener_ventas())