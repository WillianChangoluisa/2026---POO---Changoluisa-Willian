from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Venta:
    """Representa la relación entre un usuario y un producto vendido."""

    usuario_id: str
    producto_codigo: str
    cantidad: int

    def __post_init__(self) -> None:
        self.usuario_id = self._validar_texto(self.usuario_id, "La identificación del usuario")
        self.producto_codigo = self._validar_texto(self.producto_codigo, "El código del producto")

        try:
            self.cantidad = int(self.cantidad)
        except (TypeError, ValueError) as exc:
            raise ValueError("La cantidad vendida debe ser un número entero válido") from exc

        if self.cantidad <= 0:
            raise ValueError("La cantidad vendida debe ser mayor que cero")

    @staticmethod
    def _validar_texto(valor: str, mensaje: str) -> str:
        if not isinstance(valor, str):
            raise ValueError(f"{mensaje} debe ser una cadena de texto")

        valor_limpio = valor.strip()
        if not valor_limpio:
            raise ValueError(f"{mensaje} no puede estar vacío")
        return valor_limpio

    def to_dict(self) -> dict[str, str | int]:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Venta":
        if not isinstance(datos, dict):
            raise ValueError("El registro de la venta debe ser un diccionario")

        campos_requeridos = ("usuario_id", "producto_codigo", "cantidad")
        campos_faltantes = [campo for campo in campos_requeridos if campo not in datos]
        if campos_faltantes:
            raise KeyError(f"Faltan campos requeridos: {', '.join(campos_faltantes)}")

        return cls(
            usuario_id=datos["usuario_id"],
            producto_codigo=datos["producto_codigo"],
            cantidad=datos["cantidad"],
        )

    def mostrar_informacion(self) -> str:
        return (
            f"Usuario: {self.usuario_id} | Producto: {self.producto_codigo} | "
            f"Cantidad: {self.cantidad}"
        )
