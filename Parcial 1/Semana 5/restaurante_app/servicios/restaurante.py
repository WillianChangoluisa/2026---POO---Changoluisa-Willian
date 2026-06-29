# Clase Restaurante: administra productos y clientes del sistema

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Clase que gestiona los productos y clientes registrados en el restaurante."""
    
    def __init__(self, nombre_restaurante: str, ubicacion: str):
        """
        Inicializa un restaurante con su información básica.
        
        Args:
            nombre_restaurante (str): Nombre del restaurante
            ubicacion (str): Ubicación del restaurante
        """
        self.nombre_restaurante: str = nombre_restaurante
        self.ubicacion: str = ubicacion
        self.lista_productos: list[Producto] = []
        self.lista_clientes: list[Cliente] = []
    
    def agregar_producto(self, producto: Producto) -> None:
        """Agrega un nuevo producto al catálogo del restaurante."""
        self.lista_productos.append(producto)
        print(f"Producto '{producto.nombre_producto}' agregado al catálogo.")
    
    def agregar_cliente(self, cliente: Cliente) -> None:
        """Registra un nuevo cliente en el sistema."""
        self.lista_clientes.append(cliente)
        print(f"Cliente '{cliente.nombre_cliente}' registrado en el sistema.")
    
    def mostrar_todos_productos(self) -> None:
        """Muestra la información de todos los productos disponibles."""
        if not self.lista_productos:
            print("No hay productos registrados.")
            return
        
        print(f"\n{'='*60}")
        print(f"CATÁLOGO DE PRODUCTOS - {self.nombre_restaurante}")
        print(f"{'='*60}\n")
        
        for indice, producto in enumerate(self.lista_productos, start=1):
            print(f"{indice}. {producto}")
            print()
    
    def mostrar_todos_clientes(self) -> None:
        """Muestra la información de todos los clientes registrados."""
        if not self.lista_clientes:
            print("No hay clientes registrados.")
            return
        
        print(f"\n{'='*60}")
        print(f"BASE DE CLIENTES - {self.nombre_restaurante}")
        print(f"{'='*60}\n")
        
        for indice, cliente in enumerate(self.lista_clientes, start=1):
            print(f"{indice}. {cliente}")
            print()
    
    def obtener_cantidad_productos(self) -> int:
        """Retorna la cantidad total de productos registrados."""
        return len(self.lista_productos)
    
    def obtener_cantidad_clientes(self) -> int:
        """Retorna la cantidad total de clientes registrados."""
        return len(self.lista_clientes)
    
    def __str__(self) -> str:
        """Retorna una representación en texto del restaurante."""
        return (
            f"Restaurante: {self.nombre_restaurante}\n"
            f"Ubicación: {self.ubicacion}\n"
            f"Productos registrados: {self.obtener_cantidad_productos()}\n"
            f"Clientes registrados: {self.obtener_cantidad_clientes()}"
        )
