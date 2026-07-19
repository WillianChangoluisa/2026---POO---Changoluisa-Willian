"""
Módulo producto.py
Contiene la clase Producto que representa un producto general del restaurante.
Implementa responsabilidad única: representar datos de un producto base.
"""


class Producto:
    """
    Clase que representa un producto base del restaurante.

    Atributos:
        - codigo: str - Código único del producto
        - nombre: str - Nombre del producto
        - categoria: str - Categoría del producto
        - precio: float - Precio del producto

    Principios aplicados:
        - S (Single Responsibility): Solo representa datos de producto
    """

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        """
        Constructor de la clase Producto.

        Args:
            codigo (str): Código único que identifica el producto
            nombre (str): Nombre descriptivo del producto
            categoria (str): Categoría a la que pertenece
            precio (float): Precio unitario (debe ser > 0)

        Raises:
            ValueError: Si algún parámetro es inválido
        """
        # Inicializar con valores por defecto para evitar retornos None
        self._codigo: str = ""
        self._nombre: str = ""
        self._categoria: str = ""
        self._precio: float = 0.0

        # Usar los setters para validar los datos
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    # ======================== PROPIEDAD: CÓDIGO ========================

    @property
    def codigo(self) -> str:
        """Obtiene el código del producto."""
        return self._codigo

    @codigo.setter
    def codigo(self, valor: str) -> None:
        """
        Establece el código del producto con validación.

        Args:
            valor (str): Nuevo código del producto

        Raises:
            ValueError: Si el código está vacío
        """
        if not valor or not isinstance(valor, str):
            raise ValueError("El código del producto no puede estar vacío y debe ser texto.")
        if len(valor.strip()) == 0:
            raise ValueError("El código del producto no puede contener solo espacios.")
        self._codigo = valor.strip()

    # ======================== PROPIEDAD: NOMBRE ========================

    @property
    def nombre(self) -> str:
        """Obtiene el nombre del producto."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        """
        Establece el nombre del producto con validación.

        Args:
            valor (str): Nuevo nombre del producto

        Raises:
            ValueError: Si el nombre está vacío
        """
        if not valor or not isinstance(valor, str):
            raise ValueError("El nombre del producto no puede estar vacío y debe ser texto.")
        if len(valor.strip()) == 0:
            raise ValueError("El nombre del producto no puede contener solo espacios.")
        self._nombre = valor.strip()

    # ======================== PROPIEDAD: CATEGORÍA ========================

    @property
    def categoria(self) -> str:
        """Obtiene la categoría del producto."""
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        """
        Establece la categoría del producto con validación.

        Args:
            valor (str): Nueva categoría del producto

        Raises:
            ValueError: Si la categoría está vacía
        """
        if not valor or not isinstance(valor, str):
            raise ValueError("La categoría del producto no puede estar vacía y debe ser texto.")
        if len(valor.strip()) == 0:
            raise ValueError("La categoría del producto no puede contener solo espacios.")
        self._categoria = valor.strip()

    # ======================== PROPIEDAD: PRECIO ========================

    @property
    def precio(self) -> float:
        """Obtiene el precio del producto."""
        return self._precio

    @precio.setter
    def precio(self, valor) -> None:
        """
        Establece el precio del producto con validación.

        Args:
            valor: Nuevo precio del producto (convertible a float)

        Raises:
            ValueError: Si el precio no es válido o es <= 0
        """
        try:
            precio_numerico = float(valor)
        except (ValueError, TypeError):
            raise ValueError("El precio debe ser un número válido")

        if precio_numerico <= 0:
            raise ValueError("El precio debe ser mayor que cero")

        self._precio = precio_numerico

    # ======================== MÉTODO: MOSTRAR INFORMACIÓN ========================

    def mostrar_informacion(self) -> str:
        """
        Retorna la información del producto de forma legible.

        Este método es polimórfico: puede ser sobrescrito por clases hijas.

        Returns:
            str: Información formateada del producto
        """
        return (
            f"┌────────────────────────────────────────┐\n"
            f"│ 📦 PRODUCTO                            │\n"
            f"│ Código: {self._codigo:31}│\n"
            f"│ Nombre: {self._nombre:31}│\n"
            f"│ Categoría: {self._categoria:28}│\n"
            f"│ Precio: ${self._precio:>28.2f}│\n"
            f"└────────────────────────────────────────┘"
        )

    def __str__(self) -> str:
        """Retorna una representación en string del producto."""
        return f"{self._nombre} ({self._categoria}) - ${self._precio:.2f}"

    def __repr__(self) -> str:
        """Retorna una representación técnica del producto."""
        return f"Producto(codigo='{self._codigo}', nombre='{self._nombre}', categoria='{self._categoria}', precio={self._precio})"

