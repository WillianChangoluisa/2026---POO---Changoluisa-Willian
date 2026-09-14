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
