from modelo import producto
import vista.consola as consola
from datetime import datetime

def generar_alertas():
    producto.limpiar_alertas()
    catalogo = producto.obtener_catalogo()
    hoy = datetime.now()
    
    for prod in catalogo.values():
        if prod['stock'] <= prod['stock_minimo']:
            producto.agregar_alerta(prod['codigo'], "stock_bajo", f"Stock crítico ({prod['stock']} uds).")
            
        if prod['fecha_vencimiento']:
            try:
                fecha_venc = datetime.strptime(prod['fecha_vencimiento'], "%Y-%m-%d")
                dias_restantes = (fecha_venc - hoy).days
                if 0 <= dias_restantes <= 7:
                    producto.agregar_alerta(prod['codigo'], "vencimiento_proximo", f"Vence en {dias_restantes} días.")
                elif dias_restantes < 0:
                    producto.agregar_alerta(prod['codigo'], "vencimiento_proximo", "PRODUCTO VENCIDO.")
            except ValueError:
                pass
                
    consola.mostrar_mensaje("Alertas actualizadas.")
    consola.mostrar_alertas(producto.obtener_alertas())
    
def generar_reportes_graficos():
    consola.mostrar_mensaje("Preparando datos para graficar...")
    import vista.graficos as graficos
    graficos.graficar_ventas_por_categoria()
    graficos.graficar_stock_critico()