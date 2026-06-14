"""
main.py
Ejemplo de uso de la clase Mascota: crea objetos y ejecuta sus métodos.
"""

# Hacer la importación robusta para que funcione al ejecutar desde
# la raíz del proyecto o desde dentro de esta carpeta.
import os
import sys
script_dir = os.path.dirname(__file__) or '.'
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

from mascota import Mascota


def main():
    # Crear al menos dos objetos de la clase Mascota
    mascota1 = Mascota(nombre='Fido', especie='Perro', edad=4)
    mascota2 = Mascota(nombre='Misu', especie='Gato', edad=2)

    # Mostrar información y hacer sonido de cada mascota
    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()

    mascota2.mostrar_informacion()
    mascota2.hacer_sonido()

    # Ejemplo adicional (opcional): otra mascota
    mascota3 = Mascota(nombre='Lola', especie='Loro', edad=1)
    mascota3.mostrar_informacion()
    mascota3.hacer_sonido()


if __name__ == '__main__':
    main()

