import matplotlib.pyplot as plt
from modelo import producto, venta

def graficar_ventas_por_categoria():
    catalogo = producto.obtener_catalogo()
    ventas_historicas = venta.obtener_ventas()
    
    ventas_por_categoria = {}
    
    for v in ventas_historicas:
        for item in v['productos_vendidos']:
            codigo = item['codigo']
            if codigo in catalogo:
                cat = catalogo[codigo]['categoria']
                ventas_por_categoria[cat] = ventas_por_categoria.get(cat, 0) + item['subtotal']
                
    if not ventas_por_categoria:
        print("No hay suficientes datos de ventas para graficar.")
        return

    categorias = list(ventas_por_categoria.keys())
    totales = list(ventas_por_categoria.values())

    plt.figure(figsize=(10, 6))
    plt.bar(categorias, totales, color='skyblue', edgecolor='black')
    plt.title('Ventas Totales por Categoría de Producto', fontsize=14, fontweight='bold')
    plt.xlabel('Categorías', fontsize=12)
    plt.ylabel('Total de Ventas (₡)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.savefig('evidencias/grafico_ventas_categoria.png')
    plt.show()

def graficar_stock_critico():
    catalogo = producto.obtener_catalogo()
    
    productos_criticos = []
    stock_actual = []
    stock_minimo = []
    
    for p in catalogo.values():
        if p['stock'] <= p['stock_minimo']:
            productos_criticos.append(p['nombre'])
            stock_actual.append(p['stock'])
            stock_minimo.append(p['stock_minimo'])
            
    if not productos_criticos:
        print("No hay productos con stock crítico en este momento.")
        return

    x = range(len(productos_criticos))
    ancho = 0.35

    plt.figure(figsize=(10, 6))
    plt.bar([i - ancho/2 for i in x], stock_actual, ancho, label='Stock Actual', color='red')
    plt.bar([i + ancho/2 for i in x], stock_minimo, ancho, label='Stock Mínimo Requerido', color='gray', alpha=0.5)

    plt.title('Evolución de Stock Actual vs Mínimo (Productos Críticos)', fontsize=14, fontweight='bold')
    plt.ylabel('Cantidad de Unidades', fontsize=12)
    plt.xticks(x, productos_criticos, rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    
    plt.savefig('evidencias/grafico_stock_critico.png')
    plt.show()