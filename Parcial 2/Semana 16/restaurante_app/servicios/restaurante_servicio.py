from __future__ import annotations

from ..modelos.producto import Producto
from ..modelos.usuario import Usuario
from ..modelos.venta import Venta
from .archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """Coordina las operaciones principales del restaurante."""

    def __init__(self, archivo_servicio: ArchivoServicio | None = None) -> None:
        self.archivo_servicio = archivo_servicio or ArchivoServicio()
        self.productos: list[Producto] = self.archivo_servicio.cargar_productos()
        self.usuarios: list[Usuario] = self.archivo_servicio.cargar_usuarios()
        self.ventas: list[Venta] = self.archivo_servicio.cargar_ventas()

    def validar_acceso(self, identificacion: str, contrasena: str) -> bool:
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            return False
        if not contrasena:
            return False
        return usuario.password == contrasena.strip()

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        identificacion_limpia = identificacion.strip()
        for usuario in self.usuarios:
            if usuario.identificacion.lower() == identificacion_limpia.lower():
                return usuario
        return None

    def buscar_producto(self, codigo: str) -> Producto | None:
        codigo_limpio = codigo.strip()
        for producto in self.productos:
            if producto.codigo.lower() == codigo_limpio.lower():
                return producto
        return None

    def listar_usuarios(self) -> list[Usuario]:
        return list(self.usuarios)

    def cargar_usuario(self, identificacion: str) -> Usuario | None:
        return self.buscar_usuario(identificacion)

    def registrar_usuario(
        self,
        identificacion: str,
        nombre: str,
        correo: str,
        cedula: str,
        celular: str,
        password: str,
        rol: str,
        administrador_id: str,
    ) -> tuple[bool, str]:
        permiso = self._validar_administrador(administrador_id)
        if permiso is not None:
            return False, permiso
        if rol not in ("Empleado", "Cliente"):
            return False, "Solo se pueden registrar usuarios Empleado o Cliente."
        if self.buscar_usuario(identificacion) is not None:
            return False, f"El usuario {identificacion.strip()} ya existe."
        if not password.strip():
            return False, "La contraseña es obligatoria para registrar un usuario."

        try:
            usuario = Usuario(
                identificacion=identificacion,
                nombre=nombre,
                correo=correo,
                cedula=cedula,
                celular=celular,
                password=password,
                rol=rol,
            )
        except ValueError as exc:
            return False, str(exc)

        duplicado = self._buscar_usuario_por_dato("cedula", usuario.cedula)
        if duplicado is not None:
            return False, f"La cédula ya está registrada para {duplicado.identificacion}."
        duplicado = self._buscar_usuario_por_dato("correo", usuario.correo)
        if duplicado is not None:
            return False, f"El correo ya está registrado para {duplicado.identificacion}."

        self.usuarios.append(usuario)
        self.guardar_usuarios()
        return True, f"Usuario {usuario.identificacion} registrado correctamente."

    def actualizar_usuario(
        self,
        identificacion: str,
        nombre: str,
        correo: str,
        cedula: str,
        celular: str,
        password: str,
        rol: str,
        administrador_id: str,
    ) -> tuple[bool, str]:
        permiso = self._validar_administrador(administrador_id)
        if permiso is not None:
            return False, permiso

        usuario_actual = self.buscar_usuario(identificacion)
        if usuario_actual is None:
            return False, f"No se encontró el usuario {identificacion}."
        if usuario_actual.rol not in ("Empleado", "Cliente"):
            return False, "Las cuentas Administrador no se pueden modificar desde esta sección."
        if rol not in ("Empleado", "Cliente"):
            return False, "Solo se pueden asignar los roles Empleado o Cliente."

        try:
            usuario_actualizado = Usuario(
                identificacion=usuario_actual.identificacion,
                nombre=nombre,
                correo=correo,
                cedula=cedula,
                celular=celular,
                password=password.strip() or usuario_actual.password,
                rol=rol,
            )
        except ValueError as exc:
            return False, str(exc)

        for campo, valor in (("cedula", usuario_actualizado.cedula), ("correo", usuario_actualizado.correo)):
            duplicado = self._buscar_usuario_por_dato(campo, valor, excluir=usuario_actual.identificacion)
            if duplicado is not None:
                etiqueta = "cédula" if campo == "cedula" else "correo"
                return False, f"El {etiqueta} ya está registrado para {duplicado.identificacion}."

        indice = self.usuarios.index(usuario_actual)
        self.usuarios[indice] = usuario_actualizado
        self.guardar_usuarios()
        return True, f"Usuario {usuario_actual.identificacion} actualizado correctamente."

    def eliminar_usuario(self, identificacion: str, administrador_id: str) -> tuple[bool, str]:
        permiso = self._validar_administrador(administrador_id)
        if permiso is not None:
            return False, permiso

        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            return False, f"No se encontró el usuario {identificacion}."
        if usuario.identificacion.lower() == administrador_id.strip().lower():
            return False, "No puede eliminar la cuenta Administrador con la que inició sesión."
        if usuario.rol not in ("Empleado", "Cliente"):
            return False, "Las cuentas Administrador no se pueden eliminar desde esta sección."

        self.usuarios.remove(usuario)
        self.guardar_usuarios()
        return True, f"Usuario {usuario.identificacion} eliminado correctamente."

    def _validar_administrador(self, identificacion: str) -> str | None:
        administrador = self.buscar_usuario(identificacion)
        if administrador is None or administrador.rol != "Administrador":
            return "La gestión de usuarios está reservada al rol Administrador."
        return None

    def _buscar_usuario_por_dato(
        self,
        campo: str,
        valor: str,
        excluir: str = "",
    ) -> Usuario | None:
        valor_normalizado = valor.strip().casefold()
        for usuario in self.usuarios:
            if usuario.identificacion.casefold() == excluir.casefold():
                continue
            if getattr(usuario, campo).strip().casefold() == valor_normalizado:
                return usuario
        return None

    def listar_productos(self) -> list[Producto]:
        return list(self.productos)

    def listar_ventas(self) -> list[Venta]:
        return list(self.ventas)

    def guardar_productos(self) -> None:
        self.archivo_servicio.guardar_productos(self.productos)

    def guardar_usuarios(self) -> None:
        self.archivo_servicio.guardar_usuarios(self.usuarios)

    def guardar_ventas(self) -> None:
        self.archivo_servicio.guardar_ventas(self.ventas)

    def registrar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> tuple[bool, str]:
        try:
            producto = Producto(
                codigo=codigo,
                nombre=nombre,
                categoria=categoria,
                precio=precio,
                stock=stock,
            )
        except ValueError as exc:
            return False, str(exc)

        if self.buscar_producto(producto.codigo) is not None:
            return False, f"El producto {producto.codigo} ya existe."

        self.productos.append(producto)
        self.guardar_productos()
        return True, f"Producto {producto.codigo} registrado correctamente."

    def cargar_producto(self, codigo: str) -> Producto | None:
        return self.buscar_producto(codigo)

    def actualizar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> tuple[bool, str]:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False, f"No se encontró el producto con código {codigo}."

        try:
            nuevo_producto = Producto(
                codigo=codigo,
                nombre=nombre,
                categoria=categoria,
                precio=precio,
                stock=stock,
            )
        except ValueError as exc:
            return False, str(exc)

        for indice, producto_actual in enumerate(self.productos):
            if producto_actual.codigo.lower() == codigo.strip().lower():
                self.productos[indice] = nuevo_producto
                self.guardar_productos()
                return True, f"Producto {nuevo_producto.codigo} actualizado correctamente."

        return False, f"No se pudo actualizar el producto {codigo}."

    def eliminar_producto(self, codigo: str) -> tuple[bool, str]:
        codigo_limpio = codigo.strip()
        for indice, producto in enumerate(self.productos):
            if producto.codigo.lower() == codigo_limpio.lower():
                del self.productos[indice]
                self.guardar_productos()
                return True, f"Producto {codigo_limpio} eliminado correctamente."
        return False, f"No se encontró el producto con código {codigo_limpio}."

    def registrar_venta(self, identificacion_usuario: str, codigo_producto: str) -> tuple[bool, str]:
        usuario = self.buscar_usuario(identificacion_usuario)
        if usuario is None:
            return False, "Debe seleccionar un usuario registrado."

        producto = self.buscar_producto(codigo_producto)
        if producto is None:
            return False, "Debe seleccionar un producto registrado."

        if producto.stock <= 0:
            return False, f"El producto {producto.codigo} no tiene stock disponible."

        venta = Venta(usuario_id=usuario.identificacion, producto_codigo=producto.codigo)
        self.ventas.append(venta)
        producto.stock -= 1
        self.guardar_ventas()
        self.guardar_productos()
        return True, f"Venta registrada correctamente para {usuario.nombre} ({producto.codigo})."

    def consultar_ventas_por_usuario(self, identificacion_usuario: str) -> list[Venta]:
        ventas_usuario: list[Venta] = []
        for venta in self.ventas:
            if venta.usuario_id.lower() == identificacion_usuario.strip().lower():
                ventas_usuario.append(venta)
        return ventas_usuario
