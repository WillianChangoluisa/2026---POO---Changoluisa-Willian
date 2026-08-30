from __future__ import annotations

from typing import Optional

from ..modelos.producto import Producto
from ..modelos.usuario import Usuario
from ..modelos.venta import Venta
from .archivo_servicio import ArchivoServicio


class Restaurante:
    """Administra el restaurante y aplica las reglas de negocio."""

    def __init__(
        self,
        archivo_servicio: ArchivoServicio | None = None,
        data_dir: str | None = None,
        ruta_archivo: str | None = None,
    ) -> None:
        if data_dir is not None:
            archivo_servicio = ArchivoServicio(data_dir)
        elif ruta_archivo is not None:
            archivo_servicio = ArchivoServicio(ruta_archivo)

        self.archivo_servicio = archivo_servicio or ArchivoServicio()
        self._productos: list[Producto] = self.archivo_servicio.cargar_productos()
        self._usuarios: list[Usuario] = self.archivo_servicio.cargar_usuarios()
        self._ventas: list[Venta] = self.archivo_servicio.cargar_ventas()
        self.OPCIONES = (
            "Registrar producto",
            "Buscar producto",
            "Actualizar producto",
            "Eliminar producto",
            "Listar productos",
            "Registrar usuario",
            "Buscar usuario",
            "Listar usuarios",
            "Vender producto",
            "Consultar ventas por usuario",
            "Listar ventas",
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

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        return self.buscar_producto_por_codigo(codigo)

    def actualizar_producto(
        self,
        codigo: str,
        nombre: Optional[str] = None,
        categoria: Optional[str] = None,
        precio: Optional[float] = None,
        stock: Optional[int] = None,
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
        if stock is not None:
            producto.stock = Producto._validar_stock(stock)

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
        if self.buscar_usuario(usuario.identificacion) is not None:
            return False
        self._usuarios.append(usuario)
        self.guardar_usuarios()
        return True

    def registrar_cliente(self, usuario: Usuario) -> bool:
        return self.registrar_usuario(usuario)

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None

    def actualizar_usuario(
        self,
        identificacion: str,
        nombre: Optional[str] = None,
        correo: Optional[str] = None,
        cedula: Optional[str] = None,
        celular: Optional[str] = None,
    ) -> bool:
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            return False

        if nombre is not None:
            usuario.nombre = Usuario._validar_texto(nombre, "El nombre")
        if correo is not None:
            if not isinstance(correo, str) or "@" not in correo.strip():
                raise ValueError("El correo debe ser una dirección válida")
            usuario.correo = correo.strip()
        if cedula is not None:
            usuario.cedula = Usuario._validar_cedula(cedula)
        if celular is not None:
            usuario.celular = Usuario._validar_celular(celular)

        self.guardar_usuarios()
        return True

    def eliminar_usuario(self, identificacion: str) -> bool:
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            return False
        self._usuarios.remove(usuario)
        self.guardar_usuarios()
        return True

    def listar_usuarios(self) -> list[Usuario]:
        return list(self._usuarios)

    def listar_clientes(self) -> list[Usuario]:
        return self.listar_usuarios()

    def guardar_usuarios(self) -> None:
        self.archivo_servicio.guardar_usuarios(self._usuarios)

    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto_por_codigo(codigo_producto)

        if usuario is None or producto is None:
            return False

        try:
            cantidad_valida = int(cantidad)
        except (TypeError, ValueError):
            return False

        if cantidad_valida <= 0:
            return False
        if producto.stock < cantidad_valida:
            return False

        venta = Venta(usuario_id=usuario.identificacion, producto_codigo=producto.codigo, cantidad=cantidad_valida)
        self._ventas.append(venta)
        producto.vender(cantidad_valida)
        self.guardar_ventas()
        self.guardar_productos()
        return True

    def consultar_ventas_por_usuario(self, identificacion_usuario: str) -> list[Venta]:
        ventas_usuario: list[Venta] = []
        for venta in self._ventas:
            if venta.usuario_id == identificacion_usuario:
                ventas_usuario.append(venta)
        return ventas_usuario

    def listar_ventas(self) -> list[Venta]:
        return list(self._ventas)

    def guardar_ventas(self) -> None:
        self.archivo_servicio.guardar_ventas(self._ventas)
