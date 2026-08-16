from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Producto:
    """Representa un producto del restaurante.

    Atributos:
        codigo: identificador único del producto (str)
        nombre: nombre descriptivo (str)
        categoria: categoría del producto (str)
        precio: precio en unidades monetarias (float)
    """

    codigo: str
    nombre: str
    categoria: str
    precio: float

    def __post_init__(self) -> None:
        if not isinstance(self.codigo, str) or not self.codigo.strip():
            raise ValueError("El código del producto debe ser una cadena no vacía")
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ValueError("El nombre del producto debe ser una cadena no vacía")
        if not isinstance(self.categoria, str) or not self.categoria.strip():
            raise ValueError("La categoría del producto debe ser una cadena no vacía")
        try:
            self.precio = float(self.precio)
        except Exception:
            raise ValueError("El precio debe ser un número")
        if self.precio < 0:
            raise ValueError("El precio no puede ser negativo")

    def mostrar_informacion(self) -> str:
        """Devuelve una representación legible del producto."""
        return (
            f"Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: {self.precio:.2f}"
        )

