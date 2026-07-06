# Clase padre: Producto
# Representa un producto general del restaurante
class Producto:
    """Clase padre que define un producto general del restaurante."""
    
    def __init__(self, nombre, precio, disponibilidad=True):
        """
        Inicializa un producto con sus atributos básicos.
        
        Args:
            nombre (str): Nombre del producto
            precio (float): Precio del producto (debe ser > 0)
            disponibilidad (bool): Indica si el producto está disponible
        """
        self.__nombre = nombre
        self.__precio = 0  # Inicializa en 0
        self.__disponibilidad = disponibilidad
        
        # Valida y asigna el precio
        if precio > 0:
            self.__precio = precio
        else:
            raise ValueError("El precio debe ser mayor a cero.")
    
    def obtener_nombre(self):
        """Retorna el nombre del producto."""
        return self.__nombre
    
    def obtener_precio(self):
        """Retorna el precio del producto."""
        return self.__precio
    
    def cambiar_precio(self, nuevo_precio):
        """
        Cambia el precio del producto con validación.
        
        Args:
            nuevo_precio (float): El nuevo precio (debe ser > 0)
        
        Raises:
            ValueError: Si el precio no es válido
        """
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser mayor a cero.")
    
    def obtener_disponibilidad(self):
        """Retorna si el producto está disponible."""
        return self.__disponibilidad
    
    def cambiar_disponibilidad(self, disponibilidad):
        """Cambia la disponibilidad del producto."""
        self.__disponibilidad = disponibilidad
    
    def mostrar_informacion(self):
        """
        Muestra la información del producto.
        Este método será sobrescrito en las clases hijas (polimorfismo).
        """
        disponible = "Disponible" if self.__disponibilidad else "No disponible"
        print(f"Producto: {self.__nombre}")
        print(f"Precio: ${self.__precio:.2f}")
        print(f"Estado: {disponible}")
