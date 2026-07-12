"""
Módulo producto.py
Contiene la clase Producto que representa un producto del restaurante.
Implementa constructor tradicional, decoradores @property y @setter con validaciones.
"""


class Producto:
    """
    Clase que representa un producto del restaurante.

    Atributos:
        - nombre: str - Nombre del producto
        - categoria: str - Categoría del producto (Entrada, Plato Principal, Bebida, Postre, etc.)
        - precio: float - Precio del producto en moneda local
        - disponible: bool - Indica si el producto está disponible para ordenar
    """

    def __init__(self, nombre, categoria, precio, disponible=True):
        """
        Constructor de la clase Producto.

        Args:
            nombre (str): Nombre descriptivo del producto
            categoria (str): Categoría a la que pertenece el producto
            precio (float): Precio unitario del producto (debe ser > 0)
            disponible (bool): Estado de disponibilidad (por defecto True)
        """
        self._nombre = None
        self._categoria = None
        self._precio = None
        self._disponible = disponible

        # Usar los setters para validar los datos de entrada
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    # ======================== PROPIEDADES: NOMBRE ========================

    @property
    def nombre(self):
        """Obtiene el nombre del producto."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        """
        Establece el nombre del producto con validación.

        Args:
            valor (str): Nuevo nombre del producto

        Raises:
            ValueError: Si el nombre está vacío o es inválido
        """
        if not valor or not isinstance(valor, str):
            raise ValueError("El nombre del producto no puede estar vacío y debe ser texto.")
        if len(valor.strip()) == 0:
            raise ValueError("El nombre del producto no puede contener solo espacios.")
        self._nombre = valor.strip()

    # ======================== PROPIEDADES: CATEGORÍA ========================

    @property
    def categoria(self):
        """Obtiene la categoría del producto."""
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        """
        Establece la categoría del producto con validación.

        Args:
            valor (str): Nueva categoría del producto

        Raises:
            ValueError: Si la categoría está vacía o es inválida
        """
        if not valor or not isinstance(valor, str):
            raise ValueError("La categoría del producto no puede estar vacía y debe ser texto.")
        if len(valor.strip()) == 0:
            raise ValueError("La categoría del producto no puede contener solo espacios.")
        self._categoria = valor.strip()

    # ======================== PROPIEDADES: PRECIO ========================

    @property
    def precio(self):
        """Obtiene el precio del producto."""
        return self._precio

    @precio.setter
    def precio(self, valor):
        """
        Establece el precio del producto con validación.

        Args:
            valor (float): Nuevo precio del producto

        Raises:
            ValueError: Si el precio no es válido o es menor o igual que cero
        """
        try:
            precio_numerico = float(valor)
        except (ValueError, TypeError):
            raise ValueError("El precio debe ser un número válido.")

        if precio_numerico <= 0:
            raise ValueError("El precio del producto debe ser mayor que cero.")

        self._precio = precio_numerico

    # ======================== PROPIEDADES: DISPONIBLE ========================

    @property
    def disponible(self):
        """Obtiene el estado de disponibilidad del producto."""
        return self._disponible

    @disponible.setter
    def disponible(self, valor):
        """
        Establece el estado de disponibilidad del producto.

        Args:
            valor (bool): Estado de disponibilidad
        """
        self._disponible = bool(valor)

    # ======================== MÉTODOS ========================

    def mostrar_informacion(self):
        """
        Retorna la información del producto de forma legible y estructurada.

        Returns:
            str: Representación formateada del producto
        """
        estado = "✓ Disponible" if self._disponible else "✗ No disponible"
        return (
            f"┌─────────────────────────────────────┐\n"
            f"│ Producto: {self._nombre:29}│\n"
            f"│ Categoría: {self._categoria:28}│\n"
            f"│ Precio: ${self._precio:>31.2f}│\n"
            f"│ Estado: {estado:30}│\n"
            f"└─────────────────────────────────────┘"
        )

    def __str__(self):
        """Representación en string del producto."""
        return f"{self._nombre} ({self._categoria}) - ${self._precio:.2f}"

    def __repr__(self):
        """Representación técnica del producto."""
        return f"Producto(nombre='{self._nombre}', categoria='{self._categoria}', precio={self._precio}, disponible={self._disponible})"

