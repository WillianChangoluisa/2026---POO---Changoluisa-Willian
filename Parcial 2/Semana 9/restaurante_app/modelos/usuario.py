from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Usuario:
    """Representa un usuario registrado en el sistema.

    Atributos:
        identificacion: identificador único (str)
        nombre: nombre completo (str)
        correo: correo electrónico (str)
    """

    identificacion: str
    nombre: str
    correo: str

    def __post_init__(self) -> None:
        if not isinstance(self.identificacion, str) or not self.identificacion.strip():
            raise ValueError("La identificación debe ser una cadena no vacía")
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ValueError("El nombre debe ser una cadena no vacía")
        if not isinstance(self.correo, str) or "@" not in self.correo:
            raise ValueError("El correo debe ser una dirección válida")

    def mostrar_informacion(self) -> str:
        return f"ID: {self.identificacion} | Nombre: {self.nombre} | Correo: {self.correo}"

