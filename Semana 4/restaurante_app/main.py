# main.py
# Punto de entrada del programa: crea objetos y demuestra el funcionamiento
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente


def main():
    # Crear el servicio principal
    resto = Restaurante("La Buena Mesa")

    # Crear algunos productos
    p1 = Producto(1, "Lomo saltado", 18.50, "plato")
    p2 = Producto(2, "Ceviche", 16.00, "plato")
    p3 = Producto(3, "Coca Cola", 2.50, "bebida")

    # Registrar productos en el restaurante
    resto.registrar_producto(p1)
    resto.registrar_producto(p2)
    resto.registrar_producto(p3)

    # Crear clientes
    c1 = Cliente(101, "Ana Perez", "987654321")
    c2 = Cliente(102, "Juan Lopez")

    # Registrar clientes
    resto.registrar_cliente(c1)
    resto.registrar_cliente(c2)

    # Mostrar información registrada
    resto.mostrar_productos()
    print()
    resto.mostrar_clientes()

    # Crear un pedido para Ana
    pedido = resto.crear_pedido(101, [1, 3])
    print(f"\nPedido creado para {c1.nombre}, total: ${pedido['total']:.2f}")

    # Mostrar pedidos del cliente
    print(f"\nPedidos de {c1.nombre}:")
    for idx, ped in enumerate(c1.listar_pedidos(), start=1):
        print(f"Pedido {idx} - Total: ${ped['total']:.2f}")
        for prod in ped['productos']:
            print("  -", prod)


if __name__ == '__main__':
    main()
