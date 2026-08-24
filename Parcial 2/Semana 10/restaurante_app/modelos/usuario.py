from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class Usuario:
    """Representa un usuario del sistema."""

    identificacion: str
    nombre: str
    correo: str
    cedula: str
    celular: str

    def __post_init__(self) -> None:
        self.identificacion = self._validar_texto(self.identificacion, "La identificación")
        self.nombre = self._validar_texto(self.nombre, "El nombre")
        if not isinstance(self.correo, str) or "@" not in self.correo.strip():
            raise ValueError("El correo debe ser una dirección válida")
        self.correo = self.correo.strip()
        self.cedula = self._validar_cedula(self.cedula)
        self.celular = self._validar_celular(self.celular)

    @staticmethod
    def _validar_texto(valor: str, mensaje: str) -> str:
        if not isinstance(valor, str):
            raise ValueError(f"{mensaje} debe ser una cadena de texto")
        valor_limpio = valor.strip()
        if not valor_limpio:
            raise ValueError(f"{mensaje} no puede estar vacío")
        return valor_limpio

    @staticmethod
    def _validar_cedula(cedula: str) -> str:
        cedula_limpia = Usuario._validar_texto(cedula, "La cédula")
        if not cedula_limpia.isdigit() or len(cedula_limpia) != 10:
            raise ValueError("La cédula debe tener exactamente 10 dígitos")
        return cedula_limpia

    @staticmethod
    def _validar_celular(celular: str) -> str:
        valor = Usuario._validar_texto(celular, "El número de celular")
        if re.fullmatch(r"09\d{8}", valor):
            return valor
        raise ValueError("El celular debe iniciar con 09 y tener 10 dígitos en total")

    def mostrar_informacion(self) -> str:
        return (
            f"ID: {self.identificacion} | Nombre: {self.nombre} | "
            f"Correo: {self.correo} | Cédula: {self.cedula} | "
            f"Celular: {self.celular}"
        )
