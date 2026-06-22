# main.py
# Punto de entrada del sistema de gestion de restaurante
# Demuestra la funcionalidad del sistema creando productos, clientes y pedidos

from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente


def main():
    # ===== CREAR EL RESTAURANTE =====
    mi_restaurante = Restaurante("La Casa del Sabor de tu Amigo Willian")
    
    # ===== CREAR PRODUCTOS =====
    print("\n[*] Registrando productos...")
    p1 = Producto("P001", "Lomo a la parrilla", 25.50, "plato principal")
    p2 = Producto("P002", "Ceviche fresco", 22.00, "plato principal")
    p3 = Producto("P003", "Ensalada mixta", 12.50, "entrada")
    p4 = Producto("P004", "Limonada natural", 5.00, "bebida")
    p5 = Producto("P005", "Flan casero", 8.00, "postre")
    
    # Registrar productos en el restaurante
    mi_restaurante.registrar_producto(p1)
    mi_restaurante.registrar_producto(p2)
    mi_restaurante.registrar_producto(p3)
    mi_restaurante.registrar_producto(p4)
    mi_restaurante.registrar_producto(p5)
    print("[OK] Productos registrados exitosamente, gracias")
    
    # ===== CREAR CLIENTES =====
    print("\n[*] Registrando clientes...")
    c1 = Cliente(1, "Carlos Martinez", "555-1234")
    c2 = Cliente(2, "Ana Rodriguez", "555-5678")
    c3 = Cliente(3, "Jorge Fernandez")
    
    # Registrar clientes en el restaurante
    mi_restaurante.registrar_cliente(c1)
    mi_restaurante.registrar_cliente(c2)
    mi_restaurante.registrar_cliente(c3)
    print("[OK] Clientes registrados exitosamente")
    
    # ===== MOSTRAR MENU Y CLIENTES =====
    mi_restaurante.listar_productos()
    mi_restaurante.listar_clientes()
    
    # ===== CREAR PEDIDOS =====
    print("\n\n[*] Procesando pedidos...")
    
    # Pedido 1: Carlos pide lomo y limonada
    try:
        pedido1 = mi_restaurante.crear_pedido(1, ["P001", "P004"])
        print(f"\n[OK] Pedido creado para {pedido1['cliente']}")
        print(f"     Productos: {len(pedido1['productos'])} articulos")
        print(f"     Total: ${pedido1['total']:.2f}")
    except Exception as e:
        print(f"[ERROR] {e}")
    
    # Pedido 2: Ana pide ceviche, ensalada y flan
    try:
        pedido2 = mi_restaurante.crear_pedido(2, ["P002", "P003", "P005"])
        print(f"\n[OK] Pedido creado para {pedido2['cliente']}")
        print(f"     Productos: {len(pedido2['productos'])} articulos")
        print(f"     Total: ${pedido2['total']:.2f}")
    except Exception as e:
        print(f"[ERROR] {e}")
    
    # Pedido 3: Jorge pide ensalada y limonada
    try:
        pedido3 = mi_restaurante.crear_pedido(3, ["P003", "P004"])
        print(f"\n[OK] Pedido creado para {pedido3['cliente']}")
        print(f"     Productos: {len(pedido3['productos'])} articulos")
        print(f"     Total: ${pedido3['total']:.2f}")
    except Exception as e:
        print(f"[ERROR] {e}")
    
    # ===== MOSTRAR HISTORIAL DE UN CLIENTE =====
    print("\n\n===== HISTORIAL DE PEDIDOS - CARLOS =====")
    historial = c1.obtener_historial()
    if historial:
        for i, pedido in enumerate(historial, 1):
            print(f"\nPedido {i}:")
            for producto in pedido['productos']:
                print(f"  - {producto}")
            print(f"  Total: ${pedido['total']:.2f}")
    
    # ===== MOSTRAR GASTO TOTAL DE UN CLIENTE =====
    print(f"\nGasto total de {c1.nombre}: ${c1.obtener_total_gastado():.2f}")
    
    # ===== MOSTRAR RESUMEN =====
    mi_restaurante.mostrar_resumen()
    
    print("\n[COMPLETADO] Demostracion finalizada exitosamente\n")


if __name__ == "__main__":
    main()
