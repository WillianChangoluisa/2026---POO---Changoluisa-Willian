from __future__ import annotations

import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk
from typing import Any


class MainView:
    """Pantalla principal con navegación, productos, usuarios y ventas."""

    def __init__(self, parent: tk.Misc, controlador: Any, servicio: Any) -> None:
        self.parent = parent
        self.controlador = controlador
        self.servicio = servicio
        self.usuario_actual: Any | None = None
        self.usuario_seleccionado_id = ""

        self.frame = ttk.Frame(parent)

        self.header = ttk.Frame(self.frame, padding=(20, 16))
        self.header.pack(fill="x")

        icono_path = Path(__file__).resolve().parent.parent / "assets" / "logo.png"
        if icono_path.exists():
            self.logo_image = tk.PhotoImage(file=str(icono_path))
            ttk.Label(self.header, image=self.logo_image).pack(side="left")
        ttk.Label(
            self.header,
            text="Panel principal del restaurante",
            font=("Arial", 16, "bold"),
        ).pack(anchor="w", padx=(10, 0))

        self.sidebar = ttk.Frame(self.frame, padding=(20, 10))
        self.sidebar.pack(side="left", fill="y")

        self.boton_productos = ttk.Button(self.sidebar, text="Productos", command=self.mostrar_productos)
        self.boton_productos.pack(fill="x", pady=(0, 12))

        self.boton_usuarios = ttk.Button(self.sidebar, text="Usuarios", command=self.mostrar_usuarios)
        self.boton_usuarios.pack(fill="x", pady=(0, 12))

        self.boton_ventas = ttk.Button(self.sidebar, text="Ventas", command=self.mostrar_ventas)
        self.boton_ventas.pack(fill="x", pady=(0, 12))

        self.boton_usuarios.configure(state="disabled")

        self.boton_cerrar = ttk.Button(self.sidebar, text="Cerrar sesión", command=self.controlador.mostrar_login)
        self.boton_cerrar.pack(fill="x", pady=(30, 0))

        self.content = ttk.Frame(self.frame, padding=(20, 10))
        self.content.pack(fill="both", expand=True, side="right")

        self.seccion_productos = ttk.Frame(self.content)
        self.seccion_usuarios = ttk.Frame(self.content)
        self.seccion_ventas = ttk.Frame(self.content)

        self._crear_seccion_productos()
        self._crear_seccion_usuarios()
        self._crear_seccion_ventas()

    def mostrar(self, usuario: Any) -> None:
        self.usuario_actual = usuario
        self.boton_usuarios.configure(
            state="normal" if usuario.rol == "Administrador" else "disabled"
        )
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

        ttk.Label(
            self.usuarios_frame,
            text="Gestión administrativa de usuarios",
            font=("Arial", 13, "bold"),
        ).pack(anchor="w", pady=(0, 4))
        ttk.Label(
            self.usuarios_frame,
            text="Registre empleados y clientes. La contraseña no se muestra en la tabla.",
        ).pack(anchor="w", pady=(0, 10))

        formulario = ttk.LabelFrame(self.usuarios_frame, text="Datos del usuario", padding=10)
        formulario.pack(fill="x", pady=(0, 8))
        formulario.columnconfigure(1, weight=1)
        formulario.columnconfigure(3, weight=1)

        self.usuario_identificacion_var = tk.StringVar()
        self.usuario_nombre_var = tk.StringVar()
        self.usuario_correo_var = tk.StringVar()
        self.usuario_cedula_var = tk.StringVar()
        self.usuario_celular_var = tk.StringVar()
        self.usuario_password_var = tk.StringVar()
        self.usuario_rol_var = tk.StringVar(value="Cliente")

        campos = (
            ("Usuario:", self.usuario_identificacion_var, 0, 0),
            ("Nombre:", self.usuario_nombre_var, 0, 2),
            ("Correo:", self.usuario_correo_var, 1, 0),
            ("Cédula:", self.usuario_cedula_var, 1, 2),
            ("Celular:", self.usuario_celular_var, 2, 0),
            ("Contraseña:", self.usuario_password_var, 2, 2),
        )
        self.usuario_entries: list[ttk.Entry] = []
        for texto, variable, fila, columna in campos:
            ttk.Label(formulario, text=texto).grid(
                row=fila, column=columna, sticky="w", padx=(0, 8), pady=4
            )
            entrada = ttk.Entry(
                formulario,
                textvariable=variable,
                show="*" if texto == "Contraseña:" else "",
            )
            entrada.grid(row=fila, column=columna + 1, sticky="ew", padx=(0, 16), pady=4)
            self.usuario_entries.append(entrada)

        self.usuario_identificacion_entry = self.usuario_entries[0]
        ttk.Label(formulario, text="Rol:").grid(row=3, column=0, sticky="w", pady=4)
        self.usuario_rol_combo = ttk.Combobox(
            formulario,
            textvariable=self.usuario_rol_var,
            values=("Empleado", "Cliente"),
            state="readonly",
            width=24,
        )
        self.usuario_rol_combo.grid(row=3, column=1, sticky="w", pady=4)

        botones = ttk.Frame(formulario)
        botones.grid(row=3, column=2, columnspan=2, sticky="e", pady=(6, 0))
        self.boton_registrar_usuario = ttk.Button(
            botones, text="Registrar", command=self.registrar_usuario
        )
        self.boton_registrar_usuario.pack(side="left", padx=(0, 6))
        self.boton_actualizar_usuario = ttk.Button(
            botones, text="Actualizar", command=self.actualizar_usuario, state="disabled"
        )
        self.boton_actualizar_usuario.pack(side="left", padx=(0, 6))
        self.boton_eliminar_usuario = ttk.Button(
            botones, text="Eliminar", command=self.eliminar_usuario, state="disabled"
        )
        self.boton_eliminar_usuario.pack(side="left", padx=(0, 6))
        self.boton_limpiar_usuario = ttk.Button(
            botones, text="Limpiar", command=self.limpiar_formulario_usuario
        )
        self.boton_limpiar_usuario.pack(side="left")

        self.usuarios_mensaje_var = tk.StringVar(value="")
        self.usuarios_mensaje_label = tk.Label(
            self.usuarios_frame,
            textvariable=self.usuarios_mensaje_var,
            fg="green",
            anchor="w",
        )
        self.usuarios_mensaje_label.pack(fill="x", pady=(0, 6))

        tabla_con_scroll = ttk.Frame(self.usuarios_frame)
        tabla_con_scroll.pack(fill="both", expand=True)
        self.tabla_usuarios = ttk.Treeview(
            tabla_con_scroll,
            columns=("identificacion", "nombre", "correo", "rol"),
            show="headings",
            height=10,
            selectmode="browse",
        )
        barra_usuarios = ttk.Scrollbar(
            tabla_con_scroll,
            orient="vertical",
            command=self.tabla_usuarios.yview,
        )
        self.tabla_usuarios.configure(yscrollcommand=barra_usuarios.set)
        for columna, titulo, ancho, ancla in (
            ("identificacion", "Usuario", 140, "center"),
            ("nombre", "Nombre", 220, "w"),
            ("correo", "Correo", 260, "w"),
            ("rol", "Rol", 130, "center"),
        ):
            self.tabla_usuarios.heading(columna, text=titulo)
            self.tabla_usuarios.column(columna, width=ancho, anchor=ancla)
        self.tabla_usuarios.pack(side="left", fill="both", expand=True)
        barra_usuarios.pack(side="right", fill="y")
        self.tabla_usuarios.bind("<<TreeviewSelect>>", self._evento_seleccionar_usuario)

        for widget in (
            *self.usuario_entries,
            self.usuario_rol_combo,
            self.tabla_usuarios,
            barra_usuarios,
            self.boton_registrar_usuario,
            self.boton_actualizar_usuario,
            self.boton_eliminar_usuario,
            self.boton_limpiar_usuario,
        ):
            widget.bind("<Escape>", self._evento_limpiar_usuario)
        for widget in (*self.usuario_entries, self.usuario_rol_combo):
            widget.bind("<Return>", self._evento_registrar_usuario)
        self.usuario_rol_combo.bind(
            "<<ComboboxSelected>>", self._evento_cambio_rol
        )

    def _crear_seccion_ventas(self) -> None:
        self.ventas_frame = ttk.Frame(self.seccion_ventas, padding=(10, 10))
        self.ventas_frame.pack(fill="both", expand=True)

        ttk.Label(self.ventas_frame, text="Registro de ventas", font=("Arial", 13, "bold")).pack(anchor="w", pady=(0, 10))

        form = ttk.Frame(self.ventas_frame)
        form.pack(fill="x", pady=(0, 10))

        ttk.Label(form, text="Usuario:", width=12).grid(row=0, column=0, sticky="w", padx=(0, 10), pady=5)
        self.usuario_combo = ttk.Combobox(form, state="readonly", width=32)
        self.usuario_combo.grid(row=0, column=1, sticky="ew", pady=5)

        ttk.Label(form, text="Producto:", width=12).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=5)
        self.producto_combo = ttk.Combobox(form, state="readonly", width=32)
        self.producto_combo.grid(row=1, column=1, sticky="ew", pady=5)

        self.ventas_mensaje_var = tk.StringVar(value="")
        self.ventas_mensaje_label = tk.Label(self.ventas_frame, textvariable=self.ventas_mensaje_var, fg="green", wraplength=500, justify="left")
        self.ventas_mensaje_label.pack(anchor="w", pady=(0, 10))

        self.boton_registrar_venta = ttk.Button(self.ventas_frame, text="Registrar venta", command=self.registrar_venta)
        self.boton_registrar_venta.pack(anchor="w", pady=(0, 10))

        self.tabla_ventas = ttk.Treeview(
            self.ventas_frame,
            columns=("usuario", "producto", "fecha"),
            show="headings",
            height=10,
        )
        self.tabla_ventas.heading("usuario", text="Usuario")
        self.tabla_ventas.heading("producto", text="Producto")
        self.tabla_ventas.heading("fecha", text="Fecha")
        self.tabla_ventas.column("usuario", width=150, anchor="center")
        self.tabla_ventas.column("producto", width=160, anchor="center")
        self.tabla_ventas.column("fecha", width=220, anchor="center")
        self.tabla_ventas.pack(fill="both", expand=True)

    def mostrar_productos(self) -> None:
        self._mostrar_panel(self.seccion_productos)
        self._actualizar_lista_productos()

    def mostrar_usuarios(self) -> None:
        if self.usuario_actual is None or self.usuario_actual.rol != "Administrador":
            messagebox.showwarning(
                "Acceso restringido",
                "Solo el usuario Administrador puede gestionar usuarios.",
                parent=self.parent,
            )
            return
        self._mostrar_panel(self.seccion_usuarios)
        self._actualizar_lista_usuarios()

    def mostrar_ventas(self) -> None:
        self._mostrar_panel(self.seccion_ventas)
        self._actualizar_lista_ventas()
        self._cargar_comboboxes_ventas()

    def _mostrar_panel(self, panel: ttk.Frame) -> None:
        for seccion in (self.seccion_productos, self.seccion_usuarios, self.seccion_ventas):
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

    def _actualizar_lista_usuarios(self) -> None:
        for item in self.tabla_usuarios.get_children():
            self.tabla_usuarios.delete(item)

        for usuario in self.servicio.listar_usuarios():
            self.tabla_usuarios.insert(
                "",
                "end",
                iid=usuario.identificacion,
                values=(
                    usuario.identificacion,
                    usuario.nombre,
                    usuario.correo,
                    usuario.rol,
                ),
            )

    def _evento_seleccionar_usuario(self, event: tk.Event[tk.Misc]) -> None:
        seleccion = event.widget.selection()
        if not seleccion:
            return

        usuario = self.servicio.cargar_usuario(seleccion[0])
        if usuario is None:
            self._mostrar_estado_usuarios("El usuario seleccionado ya no existe.", False)
            self._actualizar_lista_usuarios()
            return

        self.usuario_seleccionado_id = usuario.identificacion
        self.usuario_identificacion_var.set(usuario.identificacion)
        self.usuario_nombre_var.set(usuario.nombre)
        self.usuario_correo_var.set(usuario.correo)
        self.usuario_cedula_var.set(usuario.cedula)
        self.usuario_celular_var.set(usuario.celular)
        self.usuario_password_var.set("")
        self.usuario_rol_var.set(usuario.rol)
        self.usuario_identificacion_entry.configure(state="disabled")
        puede_editar = usuario.rol in ("Empleado", "Cliente")
        self.boton_actualizar_usuario.configure(state="normal" if puede_editar else "disabled")
        self.boton_eliminar_usuario.configure(state="normal" if puede_editar else "disabled")
        self._mostrar_estado_usuarios(
            f"Datos de {usuario.identificacion} cargados. Deje la contraseña vacía para conservarla.",
            True,
        )

    def _evento_registrar_usuario(self, event: tk.Event[tk.Misc]) -> str:
        self.registrar_usuario()
        return "break"

    def _evento_limpiar_usuario(self, event: tk.Event[tk.Misc]) -> str:
        self.limpiar_formulario_usuario()
        return "break"

    def _evento_cambio_rol(self, event: tk.Event[tk.Misc]) -> None:
        rol = self.usuario_rol_var.get()
        self._mostrar_estado_usuarios(f"Rol seleccionado para el nuevo usuario: {rol}.", True)

    def _mostrar_estado_usuarios(self, mensaje: str, exitoso: bool) -> None:
        self.usuarios_mensaje_var.set(mensaje)
        self.usuarios_mensaje_label.config(fg="green" if exitoso else "red")

    def _limpiar_formulario_usuario(self, mensaje: str | None = None) -> None:
        seleccion = self.tabla_usuarios.selection()
        if seleccion:
            self.tabla_usuarios.selection_remove(*seleccion)
        self.usuario_seleccionado_id = ""
        self.usuario_identificacion_entry.configure(state="normal")
        self.usuario_identificacion_var.set("")
        self.usuario_nombre_var.set("")
        self.usuario_correo_var.set("")
        self.usuario_cedula_var.set("")
        self.usuario_celular_var.set("")
        self.usuario_password_var.set("")
        self.usuario_rol_var.set("Cliente")
        self.boton_actualizar_usuario.configure(state="disabled")
        self.boton_eliminar_usuario.configure(state="disabled")
        if mensaje is not None:
            self._mostrar_estado_usuarios(mensaje, True)

    def limpiar_formulario_usuario(self) -> None:
        self._limpiar_formulario_usuario("Formulario y selección limpios.")

    def registrar_usuario(self) -> None:
        if self.usuario_actual is None:
            self._mostrar_estado_usuarios("Debe iniciar sesión para gestionar usuarios.", False)
            return

        ok, mensaje = self.servicio.registrar_usuario(
            identificacion=self.usuario_identificacion_var.get(),
            nombre=self.usuario_nombre_var.get(),
            correo=self.usuario_correo_var.get(),
            cedula=self.usuario_cedula_var.get(),
            celular=self.usuario_celular_var.get(),
            password=self.usuario_password_var.get(),
            rol=self.usuario_rol_var.get(),
            administrador_id=self.usuario_actual.identificacion,
        )
        if ok:
            self._actualizar_lista_usuarios()
            self._limpiar_formulario_usuario()
        self._mostrar_estado_usuarios(mensaje, ok)

    def actualizar_usuario(self) -> None:
        if self.usuario_actual is None or not self.usuario_seleccionado_id:
            self._mostrar_estado_usuarios("Seleccione un usuario para actualizar.", False)
            return

        ok, mensaje = self.servicio.actualizar_usuario(
            identificacion=self.usuario_seleccionado_id,
            nombre=self.usuario_nombre_var.get(),
            correo=self.usuario_correo_var.get(),
            cedula=self.usuario_cedula_var.get(),
            celular=self.usuario_celular_var.get(),
            password=self.usuario_password_var.get(),
            rol=self.usuario_rol_var.get(),
            administrador_id=self.usuario_actual.identificacion,
        )
        if ok:
            self._actualizar_lista_usuarios()
            self._limpiar_formulario_usuario()
        self._mostrar_estado_usuarios(mensaje, ok)

    def eliminar_usuario(self) -> None:
        if self.usuario_actual is None or not self.usuario_seleccionado_id:
            self._mostrar_estado_usuarios("Seleccione un usuario para eliminar.", False)
            return

        identificacion = self.usuario_seleccionado_id
        if not messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Desea eliminar al usuario {identificacion}?",
            parent=self.parent,
        ):
            return

        ok, mensaje = self.servicio.eliminar_usuario(
            identificacion=identificacion,
            administrador_id=self.usuario_actual.identificacion,
        )
        if ok:
            self._actualizar_lista_usuarios()
            self._limpiar_formulario_usuario()
        self._mostrar_estado_usuarios(mensaje, ok)

    def _actualizar_lista_ventas(self) -> None:
        for item in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(item)

        for venta in self.servicio.listar_ventas():
            self.tabla_ventas.insert(
                "",
                "end",
                values=(venta.usuario_id, venta.producto_codigo, venta.fecha),
            )

    def _cargar_comboboxes_ventas(self) -> None:
        usuarios = self.servicio.listar_usuarios()
        self.usuario_combo["values"] = [f"{u.identificacion} - {u.nombre}" for u in usuarios]
        if usuarios:
            self.usuario_combo.current(0)
        else:
            self.usuario_combo.set("")

        productos = self.servicio.listar_productos()
        self.producto_combo["values"] = [f"{p.codigo} - {p.nombre}" for p in productos]
        if productos:
            self.producto_combo.current(0)
        else:
            self.producto_combo.set("")

    def _mostrar_estado(self, mensaje: str, exitoso: bool) -> None:
        self.mensaje_var.set(mensaje)
        self.mensaje_label.config(fg="green" if exitoso else "red")

    def _mostrar_estado_ventas(self, mensaje: str, exitoso: bool) -> None:
        self.ventas_mensaje_var.set(mensaje)
        self.ventas_mensaje_label.config(fg="green" if exitoso else "red")

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
            self._cargar_comboboxes_ventas()
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
            self._cargar_comboboxes_ventas()

    def eliminar_producto(self) -> None:
        codigo = self.codigo_var.get().strip()
        if not codigo:
            self._mostrar_estado("Ingrese el código del producto a eliminar.", False)
            return

        ok, mensaje = self.servicio.eliminar_producto(codigo)
        if ok:
            self.limpiar_formulario_producto(None)
            self._actualizar_lista_productos()
            self._cargar_comboboxes_ventas()
        self._mostrar_estado(mensaje, ok)

    def registrar_venta(self) -> None:
        valor_usuario = self.usuario_combo.get().strip()
        valor_producto = self.producto_combo.get().strip()

        if not valor_usuario or not valor_producto:
            self._mostrar_estado_ventas("Seleccione un usuario y un producto antes de registrar la venta.", False)
            return

        usuario_id = valor_usuario.split(" - ", 1)[0].strip()
        producto_codigo = valor_producto.split(" - ", 1)[0].strip()

        ok, mensaje = self.servicio.registrar_venta(usuario_id, producto_codigo)
        self._mostrar_estado_ventas(mensaje, ok)

        if ok:
            self._actualizar_lista_ventas()
            self._cargar_comboboxes_ventas()
