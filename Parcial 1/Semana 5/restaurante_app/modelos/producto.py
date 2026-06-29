# Clase Producto: representa un plato, bebida o producto disponible en el restaurante

class Producto:
    """Representa un producto disponible en el restaurante con sus características principales."""
    
    def __init__(self, nombre_producto: str, descripcion: str, precio: float, cantidad_disponible: int, es_bebida: bool):
        """
        Inicializa un producto con sus atributos.
        
        Args:
            nombre_producto (str): Nombre del producto
            descripcion (str): Descripción del producto
            precio (float): Precio del producto
            cantidad_disponible (int): Cantidad disponible en stock
            es_bebida (bool): Indica si es una bebida o un plato
        """
        self.nombre_producto: str = nombre_producto
        self.descripcion: str = descripcion
        self.precio: float = precio
        self.cantidad_disponible: int = cantidad_disponible
        self.es_bebida: bool = es_bebida
    
    def obtener_tipo_producto(self) -> str:
        """Retorna el tipo de producto: Bebida o Plato."""
        return "Bebida" if self.es_bebida else "Plato"
    
    def actualizar_cantidad(self, cantidad_vendida: int) -> None:
        """Reduce la cantidad disponible cuando se vende un producto."""
        if cantidad_vendida <= self.cantidad_disponible:
            self.cantidad_disponible -= cantidad_vendida
        else:
            print(f"No hay suficiente cantidad disponible. Stock actual: {self.cantidad_disponible}")
    
    def __str__(self) -> str:
        """Retorna una representación en texto del producto."""
        return (
            f"Producto: {self.nombre_producto}\n"
            f"  Descripción: {self.descripcion}\n"
            f"  Tipo: {self.obtener_tipo_producto()}\n"
            f"  Precio: ${self.precio:.2f}\n"
            f"  Stock disponible: {self.cantidad_disponible} unidades"
        )
