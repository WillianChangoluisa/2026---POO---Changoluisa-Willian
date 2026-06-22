# modelos/producto.py
# Clase que representa un producto disponible en el restaurante

class Producto:
    def __init__(self, id, nombre, precio, tipo):
        """id: identificador único
        nombre: nombre del plato o bebida
        precio: precio unitario (float)
        tipo: categoría ('plato', 'bebida', 'postre', ...)
        """
        self.id = id
        self.nombre = nombre
        self.precio = float(precio)
        self.tipo = tipo

    def __str__(self):
        return f"{self.id} - {self.nombre} ({self.tipo}) - ${self.precio:.2f}"

    def aplicar_descuento(self, porcentaje):
        """Aplica un descuento porcentual sobre el precio."""
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("Porcentaje inválido")
        self.precio = round(self.precio * (1 - porcentaje / 100), 2)
