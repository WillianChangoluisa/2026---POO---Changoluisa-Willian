# servicios/restaurante.py
# Clase principal que gestiona los productos, clientes y operaciones del restaurante

from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    """Gestiona los productos y clientes del restaurante."""
    
    def __init__(self, nombre_restaurante):
        """
        Inicializa el restaurante con:
        - nombre_restaurante: nombre del establecimiento
        """
        self.nombre = nombre_restaurante
        self.productos = {}  # diccionario: codigo -> Producto
        self.clientes = {}   # diccionario: id_cliente -> Cliente
    
    def registrar_producto(self, producto):
        """Registra un nuevo producto en el restaurante."""
        if not isinstance(producto, Producto):
            raise TypeError("Se debe proporcionar un objeto de tipo Producto")
        self.productos[producto.codigo] = producto
    
    def registrar_cliente(self, cliente):
        """Registra un nuevo cliente en el restaurante."""
        if not isinstance(cliente, Cliente):
            raise TypeError("Se debe proporcionar un objeto de tipo Cliente")
        self.clientes[cliente.id_cliente] = cliente
    
    def listar_productos(self):
        """Muestra en consola todos los productos disponibles."""
        print(f"\n===== MENU DE PRODUCTOS - {self.nombre} =====")
        if not self.productos:
            print("(No hay productos registrados)")
            return
        for producto in self.productos.values():
            print(producto)
    
    def listar_clientes(self):
        """Muestra en consola todos los clientes registrados."""
        print(f"\n===== CLIENTES REGISTRADOS - {self.nombre} =====")
        if not self.clientes:
            print("(No hay clientes registrados)")
            return
        for cliente in self.clientes.values():
            print(cliente)
    
    def buscar_producto(self, codigo):
        """Busca un producto por su codigo."""
        return self.productos.get(codigo)
    
    def buscar_cliente(self, id_cliente):
        """Busca un cliente por su id."""
        return self.clientes.get(id_cliente)
    
    def crear_pedido(self, id_cliente, codigos_productos):
        """
        Crea un pedido para un cliente con los productos especificados.
        Retorna un diccionario con los detalles del pedido.
        """
        cliente = self.buscar_cliente(id_cliente)
        if cliente is None:
            raise ValueError(f"Cliente con ID {id_cliente} no encontrado")
        
        productos_pedido = []
        total_pedido = 0
        
        for codigo in codigos_productos:
            producto = self.buscar_producto(codigo)
            if producto:
                productos_pedido.append(producto)
                total_pedido += producto.obtener_precio()
        
        if not productos_pedido:
            raise ValueError("No se encontraron productos validos para el pedido")
        
        pedido = {
            'id_cliente': id_cliente,
            'cliente': cliente.nombre,
            'productos': productos_pedido,
            'total': round(total_pedido, 2)
        }
        
        # Agregar el pedido al historial del cliente
        cliente.agregar_pedido(pedido)
        
        return pedido
    
    def mostrar_resumen(self):
        """Muestra un resumen del restaurante."""
        print(f"\n===== RESUMEN - {self.nombre} =====")
        print(f"Total de productos: {len(self.productos)}")
        print(f"Total de clientes: {len(self.clientes)}")
