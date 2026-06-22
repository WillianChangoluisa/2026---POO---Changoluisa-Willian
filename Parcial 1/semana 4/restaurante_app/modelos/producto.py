# modelos/producto.py
# Clase que representa un producto (plato o bebida) disponible en el restaurante

class Producto:
    """Representa un producto del restaurante con sus caracteristicas basicas."""
    
    def __init__(self, codigo, nombre, precio, categoria):
        """
        Inicializa un producto con:
        - codigo: identificador unico del producto
        - nombre: nombre del plato o bebida
        - precio: precio unitario (float)
        - categoria: tipo de producto ('plato principal', 'bebida', 'postre', etc.)
        """
        self.codigo = codigo
        self.nombre = nombre
        self.precio = float(precio)
        self.categoria = categoria
    
    def __str__(self):
        """Retorna una representacion legible del producto."""
        return f"[{self.codigo}] {self.nombre} ({self.categoria}) - ${self.precio:.2f}"
    
    def obtener_precio(self):
        """Retorna el precio del producto."""
        return self.precio
    
    def aplicar_descuento(self, porcentaje):
        """Aplica un descuento porcentual al precio del producto."""
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100")
        descuento = self.precio * (porcentaje / 100)
        self.precio = self.precio - descuento
        return self.precio
