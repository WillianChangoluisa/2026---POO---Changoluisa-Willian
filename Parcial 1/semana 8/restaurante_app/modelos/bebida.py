"""
Módulo bebida.py
Contiene la clase Bebida que extiende Producto.
Demuestra el principio OCP (Open/Closed): abierto a extensión, cerrado a modificación.
"""

from .producto import Producto


class Bebida(Producto):
    """
    Clase que representa una bebida del restaurante.
    Hereda de Producto e incorpora atributos específicos de bebidas.

    Atributos heredados:
        - codigo: str - Código único del producto
        - nombre: str - Nombre de la bebida
        - categoria: str - Categoría de la bebida
        - precio: float - Precio de la bebida

    Atributos propios:
        - tamaño: str - Tamaño de la bebida (pequeño, mediano, grande)
        - tipo_envase: str - Tipo de envase (lata, botella, vaso, etc.)

    Principios aplicados:
        - O (Open/Closed): Extiende sin modificar la lógica de Producto
        - L (Liskov Substitution): Puede usarse donde se espera Producto
    """

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float,
                 tamano: str, tipo_envase: str) -> None:
        """
        Constructor de la clase Bebida.

        Args:
            codigo (str): Código único de la bebida
            nombre (str): Nombre de la bebida
            categoria (str): Categoría (debe ser "Bebida")
            precio (float): Precio de la bebida
            tamaño (str): Tamaño (pequeño, mediano, grande)
            tipo_envase (str): Tipo de envase (lata, botella, vaso, etc.)

        Raises:
            ValueError: Si algún parámetro es inválido
        """
        # Llamar al constructor de la clase padre
        super().__init__(codigo, nombre, categoria, precio)

        self._tamano: str | None = None
        self._tipo_envase: str | None = None

        # Validar los atributos específicos de Bebida
        self.tamano = tamano
        self.tipo_envase = tipo_envase

    # ======================== PROPIEDAD: TAMAÑO ========================

    @property
    def tamano(self) -> str:
        """Obtiene el tamano de la bebida."""
        return self._tamano

    @tamano.setter
    def tamano(self, valor: str) -> None:
        """
        Establece el tamaño de la bebida con validación.

        Args:
            valor (str): Nuevo tamaño (pequeño, mediano, grande)

        Raises:
            ValueError: Si el tamaño es inválido
        """
        tamanos_validos = ["pequeno", "mediano", "grande"]
        if not valor or not isinstance(valor, str):
            raise ValueError("El tamaño debe ser texto válido")

        valor_lower = valor.strip().lower()
        if valor_lower not in tamanos_validos:
            raise ValueError(f"El tamano debe ser uno de: {', '.join(tamanos_validos)}")

        self._tamano = valor_lower

    # ======================== PROPIEDAD: TIPO ENVASE ========================

    @property
    def tipo_envase(self) -> str:
        """Obtiene el tipo de envase de la bebida."""
        return self._tipo_envase

    @tipo_envase.setter
    def tipo_envase(self, valor: str) -> None:
        """
        Establece el tipo de envase con validación.

        Args:
            valor (str): Nuevo tipo de envase

        Raises:
            ValueError: Si el tipo de envase está vacío
        """
        if not valor or not isinstance(valor, str):
            raise ValueError("El tipo de envase debe ser texto válido")
        if len(valor.strip()) == 0:
            raise ValueError("El tipo de envase no puede estar vacío")

        self._tipo_envase = valor.strip()

    # ======================== MÉTODO: MOSTRAR INFORMACIÓN (Sobrescrito) ========================

    def mostrar_informacion(self) -> str:
        """
        Sobrescribe el método de la clase padre para mostrar información específica de bebida.

        Demuestra polimorfismo: el mismo método tiene comportamiento diferente según el tipo.

        Returns:
            str: Información formateada de la bebida
        """
        return (
            f"┌────────────────────────────────────────┐\n"
            f"│ 🥤 BEBIDA                              │\n"
            f"│ Código: {self._codigo:31}│\n"
            f"│ Nombre: {self._nombre:31}│\n"
            f"│ Categoría: {self._categoria:28}│\n"
            f"│ Precio: ${self._precio:>28.2f}│\n"
            f"│ Tamano: {self._tamano:31}│\n"
            f"│ Envase: {self._tipo_envase:31}│\n"
            f"└────────────────────────────────────────┘"
        )

    def __str__(self) -> str:
        """Retorna una representación en string de la bebida."""
        return f"{self._nombre} ({self._tamano}, {self._tipo_envase}) - ${self._precio:.2f}"

    def __repr__(self) -> str:
        """Retorna una representación técnica de la bebida."""
        return (f"Bebida(codigo='{self._codigo}', nombre='{self._nombre}', "
                f"categoria='{self._categoria}', precio={self._precio}, "
                f"tamano='{self._tamano}', tipo_envase='{self._tipo_envase}')")

