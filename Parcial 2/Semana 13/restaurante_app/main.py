from __future__ import annotations

import sys
from pathlib import Path

import tkinter as tk

if __package__ is None or __package__ == "":
    proyecto = Path(__file__).resolve().parent.parent
    if str(proyecto) not in sys.path:
        sys.path.insert(0, str(proyecto))

    from restaurante_app.servicios.restaurante_servicio import RestauranteServicio
    from restaurante_app.ui.login_view import LoginView
    from restaurante_app.ui.main_view import MainView
else:
    from .servicios.restaurante_servicio import RestauranteServicio
    from .ui.login_view import LoginView
    from .ui.main_view import MainView


class ControladorAplicacion:
    """Controla la navegación entre la ventana de login y la vista principal."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Restaurante App")
        self.root.geometry("900x600")
        self.root.minsize(720, 500)

        self.servicio = RestauranteServicio()
        self.login_view = LoginView(self.root, self, self.servicio)
        self.main_view = MainView(self.root, self, self.servicio)
        self.mostrar_login()

    def mostrar_login(self) -> None:
        self.main_view.ocultar()
        self.login_view.mostrar()
        self.root.title("Restaurante App - Login")

    def mostrar_main(self) -> None:
        self.login_view.ocultar()
        self.main_view.mostrar()
        self.root.title("Restaurante App - Inicio")


def main() -> None:
    root = tk.Tk()
    ControladorAplicacion(root)
    root.mainloop()


if __name__ == "__main__":
    main()
