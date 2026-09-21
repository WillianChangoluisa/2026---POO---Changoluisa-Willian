from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import Any


class LoginView:
    """Pantalla de autenticación de la aplicación."""

    def __init__(self, parent: tk.Misc, controlador: Any, servicio: Any) -> None:
        self.parent = parent
        self.controlador = controlador
        self.servicio = servicio

        self.frame = ttk.Frame(parent, padding=30)
        self.frame.pack(fill="both", expand=True)

        self.panel = ttk.Frame(self.frame, padding=25)
        self.panel.pack(expand=True)

        ttk.Label(self.panel, text="Restaurante App", font=("Arial", 20, "bold")).pack(pady=(0, 10))
        ttk.Label(self.panel, text="Ingreso al sistema", font=("Arial", 11, "bold")).pack(pady=(0, 15))

        ttk.Label(self.panel, text="Usuario:").pack(anchor="w")
        self.usuario_var = tk.StringVar()
        self.usuario_entry = ttk.Entry(self.panel, textvariable=self.usuario_var, width=35)
        self.usuario_entry.pack(fill="x", pady=(0, 10))

        ttk.Label(self.panel, text="Contraseña:").pack(anchor="w")
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(self.panel, textvariable=self.password_var, show="*", width=35)
        self.password_entry.pack(fill="x", pady=(0, 15))

        self.boton_ingresar = ttk.Button(self.panel, text="Ingresar", command=self.iniciar_sesion)
        self.boton_ingresar.pack(pady=(0, 10))

        self.mensaje_var = tk.StringVar(value="")
        ttk.Label(self.panel, textvariable=self.mensaje_var, foreground="red").pack()

        self.usuario_entry.focus_set()
        self.password_entry.bind("<Return>", lambda event: self.iniciar_sesion())

    def mostrar(self) -> None:
        self.frame.pack(fill="both", expand=True)
        self.usuario_entry.focus_set()

    def ocultar(self) -> None:
        self.frame.pack_forget()

    def iniciar_sesion(self) -> None:
        identificacion = self.usuario_var.get().strip()
        contrasena = self.password_var.get().strip()

        if not identificacion or not contrasena:
            self.mensaje_var.set("Debe ingresar usuario y contraseña.")
            return

        if self.servicio.validar_acceso(identificacion, contrasena):
            self.mensaje_var.set("")
            self.controlador.mostrar_main()
            self.usuario_var.set("")
            self.password_var.set("")
            return

        self.mensaje_var.set("Credenciales incorrectas. Intente nuevamente.")
