from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class Venta:
    """Representa la relación entre un usuario y un producto vendido."""

    usuario_id: str
    producto_codigo: str
    fecha: str = ""

    def __post_init__(self) -> None:
        self.usuario_id = self._validar_texto(self.usuario_id, "La identificación del usuario")
        self.producto_codigo = self._validar_texto(self.producto_codigo, "El código del producto")
        self.fecha = self._validar_fecha(self.fecha)

    @staticmethod
    def _validar_texto(valor: Any, mensaje: str) -> str:
        if not isinstance(valor, str):
            raise ValueError(f"{mensaje} debe ser una cadena de texto")

        valor_limpio = valor.strip()
        if not valor_limpio:
            raise ValueError(f"{mensaje} no puede estar vacío")
        return valor_limpio

    @staticmethod
    def _validar_fecha(valor: Any) -> str:
        if valor in (None, ""):
            return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if isinstance(valor, datetime):
            return valor.strftime("%d/%m/%Y %H:%M:%S")
        if not isinstance(valor, str):
            raise ValueError("La fecha debe ser texto o datetime")
        valor_limpio = valor.strip()
        if not valor_limpio:
            return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return valor_limpio

    def to_dict(self) -> dict[str, str]:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "fecha": self.fecha,
        }

    @classmethod
    def from_dict(cls, datos: dict[str, Any]) -> "Venta":
        if not isinstance(datos, dict):
            raise ValueError("El registro de la venta debe ser un diccionario")

        campos_requeridos = ("usuario_id", "producto_codigo")
        faltantes = [campo for campo in campos_requeridos if campo not in datos]
        if faltantes:
            raise KeyError(f"Faltan campos requeridos: {', '.join(faltantes)}")

        return cls(
            usuario_id=datos["usuario_id"],
            producto_codigo=datos["producto_codigo"],
            fecha=datos.get("fecha", ""),
        )

    def mostrar_informacion(self) -> str:
        return f"Usuario: {self.usuario_id} | Producto: {self.producto_codigo} | Fecha: {self.fecha}"
