from __future__ import annotations

import tkinter as tk
from typing import Any


class LoginView:
    """Pantalla de autenticación de la aplicación."""

    def __init__(self, parent: tk.Misc, controlador: Any, servicio: Any) -> None:
        self.parent = parent
        self.controlador = controlador
        self.servicio = servicio

        self.frame = tk.Frame(parent, bg="#f2f2f2", padx=30, pady=30)
        self.frame.pack(fill="both", expand=True)

        self.panel = tk.Frame(self.frame, bg="white", bd=2, relief="groove", padx=20, pady=20)
        self.panel.pack(expand=True)

        tk.Label(self.panel, text="Restaurante App", font=("Arial", 20, "bold"), bg="white").pack(pady=(0, 15))
        tk.Label(self.panel, text="Ingreso al sistema", font=("Arial", 12), bg="white").pack(pady=(0, 20))

        tk.Label(self.panel, text="Usuario:", bg="white").pack(anchor="w")
        self.usuario_var = tk.StringVar()
        self.usuario_entry = tk.Entry(self.panel, textvariable=self.usuario_var, width=30)
        self.usuario_entry.pack(fill="x", pady=(0, 10))

        tk.Label(self.panel, text="Contraseña:", bg="white").pack(anchor="w")
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(self.panel, textvariable=self.password_var, show="*", width=30)
        self.password_entry.pack(fill="x", pady=(0, 15))

        self.boton_ingresar = tk.Button(
            self.panel,
            text="Ingresar",
            width=20,
            command=self.iniciar_sesion,
            bg="#2e7d32",
            fg="white",
            font=("Arial", 10, "bold"),
        )
        self.boton_ingresar.pack(pady=(0, 10))

        self.mensaje_var = tk.StringVar(value="")
        tk.Label(self.panel, textvariable=self.mensaje_var, fg="red", bg="white", wraplength=260).pack()

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
