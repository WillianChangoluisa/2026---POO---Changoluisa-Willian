from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Producto:
    """Representa un producto del restaurante."""

    codigo: str
    nombre: str
    categoria: str
    precio: float
    stock: int = 0

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

        self.stock = self._validar_stock(self.stock)

    @staticmethod
    def _validar_texto(valor: str, mensaje: str) -> str:
        if not isinstance(valor, str):
            raise ValueError(f"{mensaje} debe ser una cadena de texto")

        valor_limpio = valor.strip()
        if not valor_limpio:
            raise ValueError(f"{mensaje} no puede estar vacío")
        return valor_limpio

    @staticmethod
    def _validar_stock(valor: int) -> int:
        try:
            stock = int(valor)
        except (TypeError, ValueError) as exc:
            raise ValueError("El stock debe ser un número entero válido") from exc

        if stock < 0:
            raise ValueError("El stock no puede ser negativo")
        return stock

    def vender(self, cantidad: int) -> None:
        cantidad_valida = self._validar_stock(cantidad)
        if cantidad_valida <= 0:
            raise ValueError("La cantidad vendida debe ser mayor que cero")
        if self.stock < cantidad_valida:
            raise ValueError("No existe stock suficiente para realizar la venta")
        self.stock -= cantidad_valida

    def to_dict(self) -> dict[str, str | float | int]:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": float(self.precio),
            "stock": self.stock,
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Producto":
        if not isinstance(datos, dict):
            raise ValueError("El registro del producto debe ser un diccionario")

        campos_requeridos = ("codigo", "nombre", "categoria", "precio", "stock")
        campos_faltantes = [campo for campo in campos_requeridos if campo not in datos]
        if campos_faltantes:
            raise KeyError(f"Faltan campos requeridos: {', '.join(campos_faltantes)}")

        return cls(
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            categoria=datos["categoria"],
            precio=datos["precio"],
            stock=datos["stock"],
        )

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: {self.precio:.2f} | "
            f"Stock: {self.stock}"
        )
