from __future__ import annotations

from ..modelos.producto import Producto
from ..modelos.usuario import Usuario
from .archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """Coordina las operaciones principales del restaurante."""

    def __init__(self, archivo_servicio: ArchivoServicio | None = None) -> None:
        self.archivo_servicio = archivo_servicio or ArchivoServicio()
        self.productos: list[Producto] = self.archivo_servicio.cargar_productos()
        self.usuarios: list[Usuario] = self.archivo_servicio.cargar_usuarios()

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

    def listar_productos(self) -> list[Producto]:
        return list(self.productos)

    def guardar_productos(self) -> None:
        self.archivo_servicio.guardar_productos(self.productos)

    def guardar_usuarios(self) -> None:
        self.archivo_servicio.guardar_usuarios(self.usuarios)

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
