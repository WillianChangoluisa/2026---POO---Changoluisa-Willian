# servicios/restaurante.py
# Clase que gestiona los productos y clientes del restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = {}  # id -> Producto
        self.clientes = {}   # id -> Cliente

    def registrar_producto(self, producto):
        """Registra un producto (objeto Producto)."""
        if not isinstance(producto, Producto):
            raise TypeError("Se esperaba un Producto")
        self.productos[producto.id] = producto

    def registrar_cliente(self, cliente):
        """Registra un cliente (objeto Cliente)."""
        if not isinstance(cliente, Cliente):
            raise TypeError("Se esperaba un Cliente")
        self.clientes[cliente.id] = cliente

    def mostrar_productos(self):
        print(f"--- Productos en {self.nombre} ---")
        if not self.productos:
            print("(sin productos)")
            return
        for p in self.productos.values():
            print(p)

    def mostrar_clientes(self):
        print(f"--- Clientes registrados en {self.nombre} ---")
        if not self.clientes:
            print("(sin clientes)")
            return
        for c in self.clientes.values():
            print(c)

    def buscar_producto(self, id):
        return self.productos.get(id)

    def crear_pedido(self, cliente_id, lista_productos_ids):
        """Crea un pedido para el cliente con los ids de productos indicados.
        Devuelve el total del pedido y añade el pedido al cliente.
        """
        cliente = self.clientes.get(cliente_id)
        if cliente is None:
            raise ValueError("Cliente no encontrado")
        pedido_productos = []
        total = 0.0
        for pid in lista_productos_ids:
            prod = self.productos.get(pid)
            if prod is None:
                # Producto inexistente se omite
                continue
            pedido_productos.append(prod)
            total += prod.precio
        pedido = {"productos": pedido_productos, "total": round(total, 2)}
        cliente.agregar_pedido(pedido)
        return pedido
