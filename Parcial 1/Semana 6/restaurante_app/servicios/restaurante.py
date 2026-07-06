# Clase de servicio: Restaurante
# Administra una lista de productos del restaurante
class Restaurante:
    """
    Clase de servicio que administra los productos disponibles en el restaurante.
    Permite agregar productos y mostrar su información.
    """
    
    def __init__(self, nombre_restaurante):
        """
        Inicializa un restaurante con un nombre y una lista vacía de productos.
        
        Args:
            nombre_restaurante (str): Nombre del restaurante
        """
        self.__nombre = nombre_restaurante
        self.__productos = []
    
    def obtener_nombre(self):
        """Retorna el nombre del restaurante."""
        return self.__nombre
    
    def agregar_producto(self, producto):
        """
        Agrega un producto a la lista del restaurante.
        
        Args:
            producto: Objeto de tipo Producto, Platillo o Bebida
        """
        self.__productos.append(producto)
        print(f"✓ Producto '{producto.obtener_nombre()}' agregado al menú.")
    
    def obtener_productos(self):
        """Retorna la lista de productos."""
        return self.__productos
    
    def mostrar_productos(self):
        """
        Muestra todos los productos registrados.
        Demuestra polimorfismo al ejecutar mostrar_informacion() en cada producto,
        mostrando diferente información según el tipo (Platillo, Bebida, etc).
        """
        print(f"\n{'*' * 50}")
        print(f"MENÚ DEL RESTAURANTE: {self.__nombre}")
        print(f"{'*' * 50}\n")
        
        if not self.__productos:
            print("No hay productos registrados.")
            return
        
        # Recorre la lista de productos y ejecuta mostrar_informacion()
        # Cada producto muestra su información de forma específica (polimorfismo)
        for producto in self.__productos:
            producto.mostrar_informacion()
        
        print(f"\nTotal de productos: {len(self.__productos)}\n")
    
    def obtener_cantidad_productos(self):
        """Retorna la cantidad de productos registrados."""
        return len(self.__productos)
