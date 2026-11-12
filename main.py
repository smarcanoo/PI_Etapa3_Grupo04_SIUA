from modelo import producto
import vista.consola as consola
import controlador.inventario_ctrl as inv_ctrl
import controlador.ventas_ctrl as ven_ctrl
import controlador.reportes_ctrl as rep_ctrl

def main():
    reporte = producto.inicializar_catalogo()
    
    if reporte['cargados_ok'] > 0:
        consola.mostrar_mensaje(f"Datos cargados. (Limpieza: {reporte['nulos_corregidos']} nulos, {reporte['duplicados_omitidos']} duplicados omitidos, {reporte['atipicos_marcados']} atípicos corregidos).")
    else:
        consola.mostrar_error("El catálogo inició vacío. No se encontraron datos.")

    while True:
        opcion = consola.mostrar_menu_principal()
        
        if opcion == "1":
            inv_ctrl.registrar_producto()
        elif opcion == "2":
            inv_ctrl.actualizar_stock()
        elif opcion == "3":
            ven_ctrl.realizar_venta()
        elif opcion == "4":
            rep_ctrl.generar_alertas()
        elif opcion == "5":
            inv_ctrl.consultar_inventario() # Ahora incluye los filtros
        elif opcion == "6":
            ven_ctrl.consultar_ventas()
        elif opcion == "7":
            rep_ctrl.generar_reportes_graficos() # Opción nueva para Matplotlib
        elif opcion == "8":
            consola.mostrar_mensaje("Cerrando el sistema. ¡Hasta luego!")
            break
        else:
            consola.mostrar_error("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()