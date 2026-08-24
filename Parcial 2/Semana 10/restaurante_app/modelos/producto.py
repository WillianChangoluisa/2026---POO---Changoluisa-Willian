from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Producto:
    """Representa un producto del restaurante."""

    codigo: str
    nombre: str
    categoria: str
    precio: float

    def __post_init__(self) -> None:
        self.codigo = self._validar_texto(self.codigo, "El código del producto")
        self.nombre = self._validar_texto(self.nombre, "El nombre del producto")
        self.categoria = self._validar_texto(self.categoria, "La categoría del producto")

        try:
            self.precio = float(self.precio)
        except (TypeError, ValueError) as exc:
            raise ValueError("El precio debe ser un número válido") from exc

        if self.precio < 0:
            raise ValueError("El precio no puede ser negativo")

    @staticmethod
    def _validar_texto(valor: str, mensaje: str) -> str:
        if not isinstance(valor, str):
            raise ValueError(f"{mensaje} debe ser una cadena de texto")
        valor_limpio = valor.strip()
        if not valor_limpio:
            raise ValueError(f"{mensaje} no puede estar vacío")
        return valor_limpio

    def to_dict(self) -> dict[str, str | float]:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": float(self.precio),
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Producto":
        if not isinstance(datos, dict):
            raise ValueError("El registro del producto debe ser un diccionario")

        campos_requeridos = ("codigo", "nombre", "categoria", "precio")
        campos_faltantes = [campo for campo in campos_requeridos if campo not in datos]
        if campos_faltantes:
            raise KeyError(f"Faltan campos requeridos: {', '.join(campos_faltantes)}")

        return cls(
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            categoria=datos["categoria"],
            precio=datos["precio"],
        )

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: {self.precio:.2f}"
        )
