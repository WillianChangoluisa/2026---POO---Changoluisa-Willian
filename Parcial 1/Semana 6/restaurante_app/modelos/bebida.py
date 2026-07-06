# Clase hija: Bebida
# Hereda de Producto y agrega atributos específicos para bebidas
from .producto import Producto


class Bebida(Producto):
    """
    Clase que representa una bebida del restaurante.
    Hereda de Producto y agrega atributos específicos como volumen y tipo.
    """
    
    def __init__(self, nombre, precio, volumen_ml, tipo_bebida, disponibilidad=True):
        """
        Inicializa una bebida con sus atributos heredados y propios.
        
        Args:
            nombre (str): Nombre de la bebida
            precio (float): Precio de la bebida
            volumen_ml (int): Volumen en mililitros
            tipo_bebida (str): Tipo de bebida (ej: "Caliente", "Fría", "Alcohólica")
            disponibilidad (bool): Indica si está disponible
        """
        # Utiliza super() para llamar al constructor de la clase padre
        super().__init__(nombre, precio, disponibilidad)
        self.__volumen_ml = volumen_ml
        self.__tipo_bebida = tipo_bebida
    
    def obtener_volumen(self):
        """Retorna el volumen en mililitros."""
        return self.__volumen_ml
    
    def obtener_tipo_bebida(self):
        """Retorna el tipo de bebida."""
        return self.__tipo_bebida
    
    def cambiar_volumen(self, volumen_ml):
        """Cambia el volumen de la bebida."""
        if volumen_ml > 0:
            self.__volumen_ml = volumen_ml
        else:
            raise ValueError("El volumen debe ser mayor a cero.")
    
    def mostrar_informacion(self):
        """
        Sobrescribe el método de la clase padre para mostrar información
        específica de la bebida (polimorfismo).
        """
        disponible = "Disponible" if self.obtener_disponibilidad() else "No disponible"
        print("=" * 50)
        print(f"BEBIDA: {self.obtener_nombre()}")
        print(f"Tipo: {self.__tipo_bebida}")
        print(f"Precio: ${self.obtener_precio():.2f}")
        print(f"Volumen: {self.__volumen_ml} ml")
        print(f"Estado: {disponible}")
        print("=" * 50)
