import csv
import os

RUTA_INVENTARIO = "datos/inventario.csv"
RUTA_VENTAS = "datos/ventas.csv"

def inicializar_archivos():
    """Crea la carpeta datos/ y los archivos CSV con sus encabezados si no existen."""
    if not os.path.exists("datos"):
        os.makedirs("datos")
        
    if not os.path.exists(RUTA_INVENTARIO):
        with open(RUTA_INVENTARIO, mode='w', encoding='utf-8', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["codigo", "nombre", "categoria", "stock", "stock_minimo", "precio_compra", "precio_venta", "fecha_vencimiento"])
            
    if not os.path.exists(RUTA_VENTAS):
        with open(RUTA_VENTAS, mode='w', encoding='utf-8', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["numero_factura", "fecha", "codigo_producto", "cantidad", "subtotal", "impuestos", "total"])

def cargar_inventario():
    """Lee el CSV, limpia los datos (nulos, duplicados, atípicos) y devuelve el catálogo y un reporte de calidad."""
    inicializar_archivos()
    catalogo = {}
    reporte = {
        "cargados_ok": 0,
        "nulos_corregidos": 0,
        "duplicados_omitidos": 0,
        "atipicos_marcados": 0
    }
    
    with open(RUTA_INVENTARIO, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            codigo = fila.get("codigo", "").strip()
            
            if not codigo:
                continue 
                
            nombre = fila.get("nombre", "").strip()
            if not nombre:
                nombre = "Sin Nombre"
                reporte["nulos_corregidos"] += 1
                
            categoria = fila.get("categoria", "").strip()
            if not categoria:
                categoria = "General"
                reporte["nulos_corregidos"] += 1
            
            if codigo in catalogo:
                reporte["duplicados_omitidos"] += 1
                continue
            
            try:
                stock = int(fila.get("stock", 0))
                stock_min = int(fila.get("stock_minimo", 0))
                p_compra = float(fila.get("precio_compra", 0.0))
                p_venta = float(fila.get("precio_venta", 0.0))
            except ValueError:
                stock, stock_min, p_compra, p_venta = 0, 0, 0.0, 0.0
                reporte["nulos_corregidos"] += 1
            
            if stock < 0 or p_venta < p_compra:
                reporte["atipicos_marcados"] += 1
                stock = max(0, stock) 
                p_venta = max(p_venta, p_compra) 
            
            catalogo[codigo] = {
                "codigo": codigo,
                "nombre": nombre,
                "categoria": categoria,
                "stock": stock,
                "stock_minimo": stock_min,
                "precio_compra": p_compra,
                "precio_venta": p_venta,
                "fecha_vencimiento": fila.get("fecha_vencimiento", "")
            }
            reporte["cargados_ok"] += 1
            
    return catalogo, reporte

def guardar_inventario(catalogo):
    """Sobrescribe el archivo CSV para guardar cambios (cuando se registra un producto o se actualiza stock)."""
    with open(RUTA_INVENTARIO, mode='w', encoding='utf-8', newline='') as archivo:
        campos = ["codigo", "nombre", "categoria", "stock", "stock_minimo", "precio_compra", "precio_venta", "fecha_vencimiento"]
        writer = csv.DictWriter(archivo, fieldnames=campos, extrasaction='ignore')
        writer.writeheader()
        for producto in catalogo.values():
            writer.writerow(producto)

def guardar_linea_venta(numero_factura, fecha, codigo_producto, cantidad, subtotal, impuestos, total):
    """Añade una sola línea al archivo ventas.csv sin borrar el historial anterior."""
    with open(RUTA_VENTAS, mode='a', encoding='utf-8', newline='') as archivo:
        campos = ["numero_factura", "fecha", "codigo_producto", "cantidad", "subtotal", "impuestos", "total"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writerow({
            "numero_factura": numero_factura,
            "fecha": fecha,
            "codigo_producto": codigo_producto,
            "cantidad": cantidad,
            "subtotal": subtotal,
            "impuestos": impuestos,
            "total": total
        })