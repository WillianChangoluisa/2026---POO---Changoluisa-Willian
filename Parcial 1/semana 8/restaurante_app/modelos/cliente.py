"""
Módulo cliente.py
Contiene la clase Cliente implementada con @dataclass.
Representa un cliente registrado en el sistema de restaurante.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Cliente:
    """
    Clase que representa un cliente del restaurante usando @dataclass.

    Atributos:
        - identificacion: str - Número de identificación único del cliente
        - nombre: str - Nombre completo del cliente
        - correo: str - Correo electrónico del cliente
        - telefono: str - Teléfono de contacto (opcional)
        - fecha_registro: datetime - Fecha y hora de registro

    Ventajas del @dataclass:
        - Genera automáticamente __init__(), __repr__(), __eq__()
        - Menos código boilerplate
        - Validación automática en __post_init__()

    Principios aplicados:
        - S (Single Responsibility): Solo representa datos de cliente
    """

    identificacion: str
    nombre: str
    correo: str
    telefono: str = "No proporcionado"
    fecha_registro: datetime = field(default_factory=datetime.now)

    def __post_init__(self) -> None:
        """
        Validaciones después de que @dataclass crea el objeto.

        Raises:
            ValueError: Si algún parámetro es inválido
        """
        if not self.identificacion or not isinstance(self.identificacion, str):
            raise ValueError("La identificación debe ser texto válido")
        if len(self.identificacion.strip()) == 0:
            raise ValueError("La identificación no puede estar vacía")
        self.identificacion = self.identificacion.strip()

        if not self.nombre or not isinstance(self.nombre, str):
            raise ValueError("El nombre debe ser texto válido")
        if len(self.nombre.strip()) == 0:
            raise ValueError("El nombre no puede estar vacío")
        self.nombre = self.nombre.strip()

        if not self.correo or not isinstance(self.correo, str):
            raise ValueError("El correo debe ser texto válido")
        if "@" not in self.correo:
            raise ValueError("El correo debe contener '@'")
        self.correo = self.correo.strip()

        if not isinstance(self.telefono, str):
            raise ValueError("El teléfono debe ser texto")
        self.telefono = self.telefono.strip()

    # ======================== MÉTODO: MOSTRAR INFORMACIÓN ========================

    def mostrar_informacion(self) -> str:
        """
        Retorna la información del cliente de forma legible.

        Returns:
            str: Información formateada del cliente
        """
        fecha_str = self.fecha_registro.strftime("%d/%m/%Y - %H:%M:%S")
        return (
            f"┌────────────────────────────────────────┐\n"
            f"│ 👥 CLIENTE                             │\n"
            f"│ Identificación: {self.identificacion:25}│\n"
            f"│ Nombre: {self.nombre:31}│\n"
            f"│ Correo: {self.correo:31}│\n"
            f"│ Teléfono: {self.telefono:29}│\n"
            f"│ Registrado: {fecha_str:27}│\n"
            f"└────────────────────────────────────────┘"
        )

    def __str__(self) -> str:
        """Retorna una representación en string del cliente."""
        return f"{self.nombre} ({self.identificacion}) - {self.correo}"

