from __future__ import annotations

from typing import Optional

from ..modelos.producto import Producto
from ..modelos.usuario import Usuario
from .archivo_servicio import ArchivoServicio


class Restaurante:
    """Administra productos y usuarios del restaurante."""

    def __init__(self, archivo_servicio: ArchivoServicio | None = None) -> None:
        self.archivo_servicio = archivo_servicio or ArchivoServicio()
        self._productos: list[Producto] = self.archivo_servicio.cargar_productos()
        self._usuarios: list[Usuario] = [
            Usuario("U001", "Ana Torres", "ana.torres@restaurante.com", "1712345678", "0998765432"),
            Usuario("U002", "Luis Gómez", "luis.gomez@restaurante.com", "1723456789", "0912345678"),
            Usuario("U003", "María Pérez", "maria.perez@restaurante.com", "1734567890", "0923456789"),
            Usuario("U004", "Carlos Ruiz", "carlos.ruiz@restaurante.com", "1745678901", "0934567890"),
            Usuario("U005", "Sofía López", "sofia.lopez@restaurante.com", "1756789012", "0945678901"),
            Usuario("U006", "Diego Vargas", "diego.vargas@restaurante.com", "1767890123", "0956789012"),
            Usuario("U007", "Valeria Castro", "valeria.castro@restaurante.com", "1778901234", "0967890123"),
            Usuario("U008", "José Morales", "jose.morales@restaurante.com", "1789012345", "0978901234"),
            Usuario("U009", "Camila Rojas", "camila.rojas@restaurante.com", "1790123456", "0989012345"),
            Usuario("U010", "Andrés Silva", "andres.silva@restaurante.com", "1701234567", "0990123456"),
        ]
        self.OPCIONES = (
            "Registrar producto",
            "Buscar producto",
            "Actualizar producto",
            "Eliminar producto",
            "Listar productos",
            "Registrar usuario",
            "Listar usuarios",
            "Mostrar categorías",
            "Salir",
        )

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto_por_codigo(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        self.guardar_productos()
        return True

    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: Optional[str] = None,
        categoria: Optional[str] = None,
        precio: Optional[float] = None,
    ) -> bool:
        producto = self.buscar_producto_por_codigo(codigo)
        if producto is None:
            return False

        if nombre is not None:
            producto.nombre = Producto._validar_texto(nombre, "El nombre del producto")
        if categoria is not None:
            producto.categoria = Producto._validar_texto(categoria, "La categoría del producto")
        if precio is not None:
            producto.precio = float(precio)
            if producto.precio < 0:
                raise ValueError("El precio no puede ser negativo")

        self.guardar_productos()
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto_por_codigo(codigo)
        if producto is None:
            return False
        self._productos.remove(producto)
        self.guardar_productos()
        return True

    def listar_productos(self) -> list[Producto]:
        return list(self._productos)

    def obtener_categorias_unicas(self) -> set[str]:
        return {producto.categoria for producto in self._productos}

    def guardar_productos(self) -> None:
        self.archivo_servicio.guardar_productos(self._productos)

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if any(u.identificacion == usuario.identificacion for u in self._usuarios):
            return False
        self._usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> list[Usuario]:
        return list(self._usuarios)
