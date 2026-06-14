"""
mascota.py
Definición de la clase Mascota para el ejercicio de Programación Orientada a Objetos.
"""

class Mascota:
    """Clase que representa una mascota con atributos simples y métodos.

    Atributos:
        nombre (str): nombre de la mascota
        especie (str): especie (por ejemplo: perro, gato, loro)
        edad (int | str): edad de la mascota
    """

    def __init__(self, nombre: str, especie: str, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        """Muestra de forma organizada la información de la mascota."""
        print("\n" + "-"*40)
        print(f"Nombre:  {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad:    {self.edad}")
        print("-"*40)

    def hacer_sonido(self):
        """Imprime un sonido característico según la especie (abstracción simple)."""
        especie_normalizada = str(self.especie).strip().lower()
        sonidos = {
            'perro': 'Guau! 🐶',
            'gato': 'Miau! 😺',
            'loro': '¡Hola! 🦜',
            'pajaro': 'Pío pío! 🐦',
            'conejo': '... (silencioso) 🐰',
            'hamster': 'Chirp chirp 🐹'
        }
        sonido = sonidos.get(especie_normalizada, 'Sonido característico no disponible.')
        print(f"{self.nombre} dice: {sonido}")

