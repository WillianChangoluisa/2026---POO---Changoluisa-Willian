"""
Módulo cliente.py
Contiene la clase Cliente que representa un cliente del restaurante.
Implementa la clase utilizando el decorador @dataclass de Python.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Cliente:
    """
    Clase que representa un cliente registrado en el restaurante.

    Implementada con @dataclass para una declaración más limpia y concisa
    de la estructura de datos, con generación automática de __init__, __repr__, etc.

    Atributos:
        - nombre: str - Nombre completo del cliente
        - correo: str - Correo electrónico del cliente
        - id_cliente: str - Identificador único del cliente
        - telefono: str - Número telefónico del cliente (opcional)
        - fecha_registro: datetime - Fecha en que se registró el cliente
    """

    nombre: str
    correo: str
    id_cliente: str
    telefono: str = "No proporcionado"
    fecha_registro: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        """
        Validaciones adicionales después de la inicialización de @dataclass.

        Raises:
            ValueError: Si los datos ingresados no son válidos
        """
        if not self.nombre or not isinstance(self.nombre, str):
            raise ValueError("El nombre del cliente debe ser un texto válido.")
        if len(self.nombre.strip()) == 0:
            raise ValueError("El nombre del cliente no puede estar vacío.")

        if not self.correo or "@" not in self.correo:
            raise ValueError("El correo debe ser válido y contener '@'.")

        if not self.id_cliente or not isinstance(self.id_cliente, str):
            raise ValueError("El ID del cliente debe ser un texto válido.")
        if len(self.id_cliente.strip()) == 0:
            raise ValueError("El ID del cliente no puede estar vacío.")

        # Normalizar espacios en blanco
        self.nombre = self.nombre.strip()
        self.correo = self.correo.strip()
        self.id_cliente = self.id_cliente.strip()

    def mostrar_informacion(self):
        """
        Retorna la información del cliente de forma legible y estructurada.

        Returns:
            str: Representación formateada del cliente
        """
        fecha_str = self.fecha_registro.strftime("%d/%m/%Y - %H:%M:%S")
        return (
            f"┌─────────────────────────────────────┐\n"
            f"│ Nombre: {self.nombre:31}│\n"
            f"│ ID Cliente: {self.id_cliente:27}│\n"
            f"│ Correo: {self.correo:31}│\n"
            f"│ Teléfono: {self.telefono:29}│\n"
            f"│ Registrado: {fecha_str:27}│\n"
            f"└─────────────────────────────────────┘"
        )

    def __str__(self):
        """Representación simple del cliente."""
        return f"{self.nombre} ({self.id_cliente}) - {self.correo}"

    def __repr__(self):
        """Representación técnica del cliente."""
        return (
            f"Cliente(nombre='{self.nombre}', correo='{self.correo}', "
            f"id_cliente='{self.id_cliente}', telefono='{self.telefono}')"
        )

