from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import Any


class MainView:
    """Pantalla principal con navegación, formulario de productos y consulta de usuarios."""

    def __init__(self, parent: tk.Misc, controlador: Any, servicio: Any) -> None:
        self.parent = parent
        self.controlador = controlador
        self.servicio = servicio

        self.frame = ttk.Frame(parent)

        self.header = ttk.Frame(self.frame, padding=(20, 16))
        self.header.pack(fill="x")
        ttk.Label(
            self.header,
            text="Panel principal del restaurante",
            font=("Arial", 16, "bold"),
        ).pack(anchor="w")

        self.sidebar = ttk.Frame(self.frame, padding=(20, 10))
        self.sidebar.pack(side="left", fill="y")

        self.boton_productos = ttk.Button(self.sidebar, text="Productos", command=self.mostrar_productos)
        self.boton_productos.pack(fill="x", pady=(0, 12))

        self.boton_usuarios = ttk.Button(self.sidebar, text="Usuarios", command=self.mostrar_usuarios)
        self.boton_usuarios.pack(fill="x", pady=(0, 12))

        self.boton_cerrar = ttk.Button(self.sidebar, text="Cerrar sesión", command=self.controlador.mostrar_login)
        self.boton_cerrar.pack(fill="x", pady=(30, 0))

        self.content = ttk.Frame(self.frame, padding=(20, 10))
        self.content.pack(fill="both", expand=True, side="right")

        self.seccion_productos = ttk.Frame(self.content)
        self.seccion_usuarios = ttk.Frame(self.content)

        self._crear_seccion_productos()
        self._crear_seccion_usuarios()

    def mostrar(self) -> None:
        self.frame.pack(fill="both", expand=True)
        self.mostrar_productos()

    def ocultar(self) -> None:
        self.frame.pack_forget()

    def _crear_seccion_productos(self) -> None:
        self.productos_frame = ttk.Frame(self.seccion_productos, padding=(10, 10))
        self.productos_frame.pack(fill="both", expand=True)

        ttk.Label(self.productos_frame, text="Gestión de productos", font=("Arial", 13, "bold")).pack(anchor="w", pady=(0, 10))

        form = ttk.Frame(self.productos_frame)
        form.pack(fill="x")

        self.codigo_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.categoria_var = tk.StringVar()
        self.precio_var = tk.StringVar()
        self.stock_var = tk.StringVar()

        campos = [
            ("Código:", self.codigo_var),
            ("Nombre:", self.nombre_var),
            ("Categoría:", self.categoria_var),
            ("Precio:", self.precio_var),
            ("Stock:", self.stock_var),
        ]

        for index, (label_text, variable) in enumerate(campos):
            fila = ttk.Frame(form, padding=(0, 4))
            fila.grid(row=index, column=0, sticky="ew", padx=(0, 12), pady=2)
            ttk.Label(fila, text=label_text, width=12).pack(side="left")
            ttk.Entry(fila, textvariable=variable, width=28).pack(side="left", fill="x", expand=True)

        self.mensaje_var = tk.StringVar(value="")
        self.mensaje_label = tk.Label(self.productos_frame, textvariable=self.mensaje_var, fg="green", wraplength=500, justify="left")
        self.mensaje_label.pack(anchor="w", pady=(12, 10))

        botones = ttk.Frame(self.productos_frame)
        botones.pack(fill="x", pady=(0, 10))
        ttk.Button(botones, text="Registrar", command=self.registrar_producto).pack(side="left", padx=(0, 8))
        ttk.Button(botones, text="Cargar", command=self.cargar_producto).pack(side="left", padx=(0, 8))
        ttk.Button(botones, text="Actualizar", command=self.actualizar_producto).pack(side="left", padx=(0, 8))
        ttk.Button(botones, text="Eliminar", command=self.eliminar_producto).pack(side="left", padx=(0, 8))
        ttk.Button(botones, text="Limpiar", command=self.limpiar_formulario_producto).pack(side="left")

        self.tabla_productos = ttk.Treeview(
            self.productos_frame,
            columns=("codigo", "nombre", "categoria", "precio", "stock"),
            show="headings",
            height=12,
        )
        self.tabla_productos.heading("codigo", text="Código")
        self.tabla_productos.heading("nombre", text="Nombre")
        self.tabla_productos.heading("categoria", text="Categoría")
        self.tabla_productos.heading("precio", text="Precio")
        self.tabla_productos.heading("stock", text="Stock")

        self.tabla_productos.column("codigo", width=90, anchor="center")
        self.tabla_productos.column("nombre", width=220, anchor="w")
        self.tabla_productos.column("categoria", width=160, anchor="w")
        self.tabla_productos.column("precio", width=100, anchor="center")
        self.tabla_productos.column("stock", width=80, anchor="center")
        self.tabla_productos.pack(fill="both", expand=True)

    def _crear_seccion_usuarios(self) -> None:
        self.usuarios_frame = ttk.Frame(self.seccion_usuarios, padding=(10, 10))
        self.usuarios_frame.pack(fill="both", expand=True)

        ttk.Label(self.usuarios_frame, text="Consulta de usuarios", font=("Arial", 13, "bold")).pack(anchor="w", pady=(0, 10))

        self.usuarios_text = tk.Text(self.usuarios_frame, wrap="word", height=18, font=("Arial", 10))
        self.usuarios_text.pack(fill="both", expand=True)
        self.usuarios_text.config(state="disabled")

    def mostrar_productos(self) -> None:
        self._mostrar_panel(self.seccion_productos)
        self._actualizar_lista_productos()

    def mostrar_usuarios(self) -> None:
        self._mostrar_panel(self.seccion_usuarios)
        self._mostrar_usuarios()

    def _mostrar_panel(self, panel: ttk.Frame) -> None:
        for seccion in (self.seccion_productos, self.seccion_usuarios):
            seccion.pack_forget()
        panel.pack(fill="both", expand=True)

    def _actualizar_lista_productos(self) -> None:
        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)

        for producto in self.servicio.listar_productos():
            self.tabla_productos.insert(
                "",
                "end",
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    f"${producto.precio:.2f}",
                    producto.stock,
                ),
            )

    def _mostrar_usuarios(self) -> None:
        usuarios = self.servicio.listar_usuarios()
        self.usuarios_text.config(state="normal")
        self.usuarios_text.delete("1.0", tk.END)

        if not usuarios:
            self.usuarios_text.insert(tk.END, "No hay usuarios registrados.")
        else:
            for usuario in usuarios:
                self.usuarios_text.insert(tk.END, usuario.mostrar_informacion() + "\n\n")

        self.usuarios_text.config(state="disabled")

    def _mostrar_estado(self, mensaje: str, exitoso: bool) -> None:
        self.mensaje_var.set(mensaje)
        self.mensaje_label.config(fg="green" if exitoso else "red")

    def _leer_producto_formulario(self) -> tuple[str, str, str, float, int] | None:
        codigo = self.codigo_var.get().strip()
        nombre = self.nombre_var.get().strip()
        categoria = self.categoria_var.get().strip()
        precio = self.precio_var.get().strip()
        stock = self.stock_var.get().strip()

        if not codigo or not nombre or not categoria or not precio or not stock:
            self._mostrar_estado("Complete todos los campos del formulario.", False)
            return None

        try:
            precio_real = float(precio)
            stock_real = int(stock)
        except ValueError:
            self._mostrar_estado("Precio debe ser numérico y stock debe ser un entero válido.", False)
            return None

        return codigo, nombre, categoria, precio_real, stock_real

    def limpiar_formulario_producto(self, mensaje: str | None = "Formulario limpio.") -> None:
        self.codigo_var.set("")
        self.nombre_var.set("")
        self.categoria_var.set("")
        self.precio_var.set("")
        self.stock_var.set("")
        if mensaje is not None:
            self._mostrar_estado(mensaje, True)

    def registrar_producto(self) -> None:
        datos = self._leer_producto_formulario()
        if datos is None:
            return

        codigo, nombre, categoria, precio, stock = datos
        ok, mensaje = self.servicio.registrar_producto(codigo, nombre, categoria, precio, stock)
        if ok:
            self.limpiar_formulario_producto(None)
            self._actualizar_lista_productos()
        self._mostrar_estado(mensaje, ok)


    def cargar_producto(self) -> None:
        codigo = self.codigo_var.get().strip()
        if not codigo:
            self._mostrar_estado("Ingrese el código del producto a consultar.", False)
            return

        producto = self.servicio.cargar_producto(codigo)
        if producto is None:
            self._mostrar_estado(f"No existe un producto con código {codigo}.", False)
            return

        self.codigo_var.set(producto.codigo)
        self.nombre_var.set(producto.nombre)
        self.categoria_var.set(producto.categoria)
        self.precio_var.set(str(producto.precio))
        self.stock_var.set(str(producto.stock))
        self._mostrar_estado(f"Producto {producto.codigo} cargado correctamente.", True)

    def actualizar_producto(self) -> None:
        datos = self._leer_producto_formulario()
        if datos is None:
            return

        codigo, nombre, categoria, precio, stock = datos
        ok, mensaje = self.servicio.actualizar_producto(codigo, nombre, categoria, precio, stock)
        self._mostrar_estado(mensaje, ok)

        if ok:
            self._actualizar_lista_productos()

    def eliminar_producto(self) -> None:
        codigo = self.codigo_var.get().strip()
        if not codigo:
            self._mostrar_estado("Ingrese el código del producto a eliminar.", False)
            return

        ok, mensaje = self.servicio.eliminar_producto(codigo)
        if ok:
            self.limpiar_formulario_producto(None)
            self._actualizar_lista_productos()
        self._mostrar_estado(mensaje, ok)
