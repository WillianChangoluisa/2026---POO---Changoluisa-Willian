
"""
Tarea semana 2 - Ejemplo: Clase que representa una cuenta bancaria.

Clase: CuentaBancaria
- atributos: titular, numero_cuenta, saldo
- métodos: depositar, retirar, transferir, __str__

Demostración simple en el bloque `if __name__ == "__main__"`.
"""

from __future__ import annotations
from dataclasses import dataclass, field
import itertools


_account_counter = itertools.count(1001)


@dataclass
class CuentaBancaria:
	"""Representa una cuenta bancaria simple.

	Atributos:
		titular (str): Nombre del propietario.
		numero_cuenta (int): Identificador de la cuenta.
		saldo (float): Saldo actual de la cuenta.
	"""

	titular: str
	saldo: float = 0.0
	numero_cuenta: int = field(default_factory=lambda: next(_account_counter))

	def depositar(self, cantidad: float) -> None:
		"""Agrega `cantidad` al saldo si es positiva."""
		if cantidad <= 0:
			raise ValueError("La cantidad a depositar debe ser positiva")
		self.saldo += cantidad

	def retirar(self, cantidad: float) -> None:
		"""Resta `cantidad` del saldo si hay fondos suficientes."""
		if cantidad <= 0:
			raise ValueError("La cantidad a retirar debe ser positiva")
		if cantidad > self.saldo:
			raise ValueError("Fondos insuficientes")
		self.saldo -= cantidad

	def transferir(self, cantidad: float, destino: "CuentaBancaria") -> None:
		"""Transfiere `cantidad` a otra `destino` si hay fondos suficientes."""
		if not isinstance(destino, CuentaBancaria):
			raise TypeError("El destino debe ser otra CuentaBancaria")
		self.retirar(cantidad)
		destino.depositar(cantidad)

	def __str__(self) -> str:
		return f"Cuenta {self.numero_cuenta} - Titular: {self.titular} - Saldo: ${self.saldo:.2f}"


def _demo() -> None:
	a = CuentaBancaria("Ana Pérez", saldo=500.0)
	b = CuentaBancaria("Luis Gómez", saldo=150.0)

	print("Estados iniciales:")
	print(a)
	print(b)

	print("\nAna deposita $200...")
	a.depositar(200)
	print(a)

	print("\nAna transfiere $300 a Luis...")
	a.transferir(300, b)
	print(a)
	print(b)

	try:
		print("\nLuis intenta retirar $500 (debe fallar)...")
		b.retirar(500)
	except ValueError as e:
		print("Error:", e)


if __name__ == "__main__":
	_demo()

