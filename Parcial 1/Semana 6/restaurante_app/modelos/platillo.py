# Clase hija: Platillo
# Hereda de Producto y agrega atributos específicos para platillos
from .producto import Producto


class Platillo(Producto):
    """
    Clase que representa un platillo (comida) del restaurante.
    Hereda de Producto y agrega atributos específicos como tipo y calorías.
    """
    
    def __init__(self, nombre, precio, tipo_platillo, calorias, disponibilidad=True):
        """
        Inicializa un platillo con sus atributos heredados y propios.
        
        Args:
            nombre (str): Nombre del platillo
            precio (float): Precio del platillo
            tipo_platillo (str): Tipo de platillo (ej: "Entrada", "Plato Principal", "Postre")
            calorias (int): Calorías del platillo
            disponibilidad (bool): Indica si está disponible
        """
        # Utiliza super() para llamar al constructor de la clase padre
        super().__init__(nombre, precio, disponibilidad)
        self.__tipo_platillo = tipo_platillo
        self.__calorias = calorias
    
    def obtener_tipo_platillo(self):
        """Retorna el tipo de platillo."""
        return self.__tipo_platillo
    
    def obtener_calorias(self):
        """Retorna las calorías del platillo."""
        return self.__calorias
    
    def cambiar_calorias(self, calorias):
        """Cambia el valor de calorías del platillo."""
        if calorias >= 0:
            self.__calorias = calorias
        else:
            raise ValueError("Las calorías no pueden ser negativas.")
    
    def mostrar_informacion(self):
        """
        Sobrescribe el método de la clase padre para mostrar información
        específica del platillo (polimorfismo).
        """
        disponible = "Disponible" if self.obtener_disponibilidad() else "No disponible"
        print("-" * 50)
        print(f"PLATILLO: {self.obtener_nombre()}")
        print(f"Tipo: {self.__tipo_platillo}")
        print(f"Precio: ${self.obtener_precio():.2f}")
        print(f"Calorías: {self.__calorias} kcal")
        print(f"Estado: {disponible}")
        print("-" * 50)
