from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any


@dataclass
class Usuario:
    """Representa un usuario del sistema de acceso."""

    identificacion: str
    nombre: str
    correo: str
    cedula: str
    celular: str
    password: str = ""

    def __post_init__(self) -> None:
        self.identificacion = self._validar_texto(self.identificacion, "La identificación")
        self.nombre = self._validar_texto(self.nombre, "El nombre")

        if not isinstance(self.correo, str) or "@" not in self.correo.strip():
            raise ValueError("El correo debe tener un formato válido")
        self.correo = self.correo.strip()

        self.cedula = self._validar_cedula(self.cedula)
        self.celular = self._validar_celular(self.celular)

        if isinstance(self.password, str):
            self.password = self.password.strip()

    @staticmethod
    def _validar_texto(valor: Any, mensaje: str) -> str:
        if not isinstance(valor, str):
            raise ValueError(f"{mensaje} debe ser una cadena de texto")

        valor_limpio = valor.strip()
        if not valor_limpio:
            raise ValueError(f"{mensaje} no puede estar vacío")
        return valor_limpio

    @staticmethod
    def _validar_cedula(cedula: Any) -> str:
        cedula_limpia = Usuario._validar_texto(cedula, "La cédula")
        if not cedula_limpia.isdigit() or len(cedula_limpia) != 10:
            raise ValueError("La cédula debe tener exactamente 10 dígitos")
        return cedula_limpia

    @staticmethod
    def _validar_celular(celular: Any) -> str:
        valor = Usuario._validar_texto(celular, "El número de celular")
        if re.fullmatch(r"09\d{8}", valor):
            return valor
        raise ValueError("El celular debe iniciar con 09 y tener 10 dígitos")

    def to_dict(self) -> dict[str, str]:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
            "cedula": self.cedula,
            "celular": self.celular,
            "password": self.password,
        }

    @classmethod
    def from_dict(cls, datos: dict[str, Any]) -> "Usuario":
        if not isinstance(datos, dict):
            raise ValueError("El registro del usuario debe ser un diccionario")

        campos_requeridos = ("identificacion", "nombre", "correo", "cedula", "celular")
        faltantes = [campo for campo in campos_requeridos if campo not in datos]
        if faltantes:
            raise KeyError(f"Faltan campos requeridos: {', '.join(faltantes)}")

        datos_usuario = dict(datos)
        if "password" not in datos_usuario:
            datos_usuario["password"] = ""

        return cls(
            identificacion=datos_usuario["identificacion"],
            nombre=datos_usuario["nombre"],
            correo=datos_usuario["correo"],
            cedula=datos_usuario["cedula"],
            celular=datos_usuario["celular"],
            password=datos_usuario["password"],
        )

    def mostrar_informacion(self) -> str:
        return (
            f"ID: {self.identificacion} | Nombre: {self.nombre} | "
            f"Correo: {self.correo} | Cédula: {self.cedula} | "
            f"Celular: {self.celular}"
        )
