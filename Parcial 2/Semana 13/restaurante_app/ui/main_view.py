from __future__ import annotations

import tkinter as tk
from typing import Any


class MainView:
    """Pantalla principal desde la que se consultan usuarios y productos."""

    def __init__(self, parent: tk.Misc, controlador: Any, servicio: Any) -> None:
        self.parent = parent
        self.controlador = controlador
        self.servicio = servicio

        self.frame = tk.Frame(parent, bg="#e8f5e9")

        self.header = tk.Frame(self.frame, bg="#1b5e20", padx=20, pady=15)
        self.header.pack(fill="x")
        tk.Label(
            self.header,
            text="Panel principal del restaurante",
            fg="white",
            bg="#1b5e20",
            font=("Arial", 16, "bold"),
        ).pack(anchor="w")

        self.menu = tk.Frame(self.frame, bg="#e8f5e9", padx=20, pady=20)
        self.menu.pack(fill="y", side="left")

        self.boton_productos = tk.Button(self.menu, text="Productos", width=18, command=self.mostrar_productos)
        self.boton_productos.pack(pady=(0, 12), fill="x")

        self.boton_usuarios = tk.Button(self.menu, text="Usuarios", width=18, command=self.mostrar_usuarios)
        self.boton_usuarios.pack(pady=(0, 12), fill="x")

        self.boton_ventas = tk.Button(self.menu, text="Ventas (pendiente)", width=18, command=self.mostrar_pendiente)
        self.boton_ventas.pack(pady=(0, 12), fill="x")

        self.boton_cerrar = tk.Button(self.menu, text="Cerrar sesión", width=18, command=self.controlador.mostrar_login)
        self.boton_cerrar.pack(pady=(20, 0), fill="x")

        self.content = tk.Frame(self.frame, bg="white", padx=20, pady=20)
        self.content.pack(fill="both", expand=True, side="right")

        self.detalle = tk.Text(self.content, wrap="word", width=80, height=20, font=("Arial", 11))
        self.detalle.pack(fill="both", expand=True)
        self.detalle.config(state="disabled")

    def mostrar(self) -> None:
        self.frame.pack(fill="both", expand=True)
        self.mostrar_productos()

    def ocultar(self) -> None:
        self.frame.pack_forget()

    def _mostrar_texto(self, texto: str) -> None:
        self.detalle.config(state="normal")
        self.detalle.delete("1.0", tk.END)
        self.detalle.insert(tk.END, texto)
        self.detalle.config(state="disabled")

    def mostrar_productos(self) -> None:
        productos = self.servicio.listar_productos()
        if not productos:
            self._mostrar_texto("No hay productos registrados.")
            return

        lineas = ["PRODUCTOS REGISTRADOS\n" + "-" * 40]
        for producto in productos:
            lineas.append(producto.mostrar_informacion())
        self._mostrar_texto("\n\n".join(lineas))

    def mostrar_usuarios(self) -> None:
        usuarios = self.servicio.listar_usuarios()
        if not usuarios:
            self._mostrar_texto("No hay usuarios registrados.")
            return

        lineas = ["USUARIOS REGISTRADOS\n" + "-" * 40]
        for usuario in usuarios:
            lineas.append(usuario.mostrar_informacion())
        self._mostrar_texto("\n\n".join(lineas))

    def mostrar_pendiente(self) -> None:
        self._mostrar_texto("Funcionalidad de ventas aún pendiente.\n\nSe incorporará en futuras semanas del proyecto.")
