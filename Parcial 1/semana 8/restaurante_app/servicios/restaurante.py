"""
Módulo restaurante.py
Contiene la clase Restaurante, responsable de administrar productos y clientes.
"""

from typing import List, Optional
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente


class Restaurante:
    """
    Servicio que administra productos y clientes.

    Mantiene dos listas internas: una para productos (incluye Bebida)
    y otra para clientes. Proporciona métodos para registrar, validar
    y listar entidades.
    """

    def __init__(self) -> None:
        self.productos: List[Producto] = []
        self.clientes: List[Cliente] = []

    # -------------------- PRODUCTOS --------------------
    def _codigo_producto_existe(self, codigo: str) -> bool:
        return any(p.codigo.lower() == codigo.lower() for p in self.productos)

    def registrar_producto(self, producto: Producto) -> Producto:
        """Registra un objeto Producto o Bebida en la colección.

        Lanza ValueError si el código ya existe.
        """
        if self._codigo_producto_existe(producto.codigo):
            raise ValueError(f"El código de producto '{producto.codigo}' ya existe")
        self.productos.append(producto)
        return producto

    def crear_y_registrar_producto(self, codigo: str, nombre: str, categoria: str, precio: float) -> Producto:
        """Crea un Producto y lo registra."""
        producto = Producto(codigo, nombre, categoria, precio)
        return self.registrar_producto(producto)

    def crear_y_registrar_bebida(self, codigo: str, nombre: str, categoria: str, precio: float, tamano: str, tipo_envase: str) -> Bebida:
        """Crea una Bebida y la registra."""
        bebida = Bebida(codigo, nombre, categoria, precio, tamano, tipo_envase)
        return self.registrar_producto(bebida)

    def listar_productos(self) -> List[Producto]:
        """Retorna la lista de productos almacenados."""
        return list(self.productos)

    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        for p in self.productos:
            if p.codigo.lower() == codigo.lower():
                return p
        return None

    def actualizar_producto(self, codigo: str, nombre: str = None, categoria: str = None, precio: float = None) -> Producto:
        """Actualiza los datos de un producto existente.

        Solo actualiza los campos que no sean None.
        Lanza ValueError si el producto no existe.
        """
        producto = self.buscar_producto_por_codigo(codigo)
        if not producto:
            raise ValueError(f"Producto con código '{codigo}' no encontrado")

        if nombre is not None:
            producto.nombre = nombre
        if categoria is not None:
            producto.categoria = categoria
        if precio is not None:
            producto.precio = precio

        return producto

    def actualizar_bebida(self, codigo: str, nombre: str = None, categoria: str = None,
                         precio: float = None, tamano: str = None, tipo_envase: str = None) -> Bebida:
        """Actualiza los datos de una bebida existente.

        Solo actualiza los campos que no sean None.
        Lanza ValueError si la bebida no existe o si el tipo no es Bebida.
        """
        producto = self.buscar_producto_por_codigo(codigo)
        if not producto:
            raise ValueError(f"Bebida con código '{codigo}' no encontrado")
        if not isinstance(producto, Bebida):
            raise ValueError(f"El código '{codigo}' no corresponde a una bebida")

        if nombre is not None:
            producto.nombre = nombre
        if categoria is not None:
            producto.categoria = categoria
        if precio is not None:
            producto.precio = precio
        if tamano is not None:
            producto.tamano = tamano
        if tipo_envase is not None:
            producto.tipo_envase = tipo_envase

        return producto

    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto de la colección.

        Retorna True si se eliminó exitosamente, False si no existe.
        """
        for i, p in enumerate(self.productos):
            if p.codigo.lower() == codigo.lower():
                self.productos.pop(i)
                return True
        return False

    # -------------------- CLIENTES --------------------
    def _cliente_id_existe(self, identificacion: str) -> bool:
        return any(c.identificacion.lower() == identificacion.lower() for c in self.clientes)

    def registrar_cliente(self, cliente: Cliente) -> Cliente:
        """Registra un objeto Cliente.

        Lanza ValueError si la identificación ya existe.
        """
        if self._cliente_id_existe(cliente.identificacion):
            raise ValueError(f"El cliente con identificación '{cliente.identificacion}' ya existe")
        self.clientes.append(cliente)
        return cliente

    def crear_y_registrar_cliente(self, identificacion: str, nombre: str, correo: str, telefono: str = "No proporcionado") -> Cliente:
        cliente = Cliente(identificacion, nombre, correo, telefono)
        return self.registrar_cliente(cliente)

    def listar_clientes(self) -> List[Cliente]:
        return list(self.clientes)

    def buscar_cliente_por_id(self, identificacion: str) -> Optional[Cliente]:
        for c in self.clientes:
            if c.identificacion.lower() == identificacion.lower():
                return c
        return None

    def actualizar_cliente(self, identificacion: str, nombre: str = None, correo: str = None,
                          telefono: str = None) -> Cliente:
        """Actualiza los datos de un cliente existente.

        Solo actualiza los campos que no sean None.
        Lanza ValueError si el cliente no existe.
        """
        cliente = self.buscar_cliente_por_id(identificacion)
        if not cliente:
            raise ValueError(f"Cliente con identificación '{identificacion}' no encontrado")

        if nombre is not None:
            cliente.nombre = nombre
        if correo is not None:
            if "@" not in correo:
                raise ValueError("El correo debe contener '@'")
            cliente.correo = correo
        if telefono is not None:
            cliente.telefono = telefono

        return cliente

    def eliminar_cliente(self, identificacion: str) -> bool:
        """Elimina un cliente de la colección.

        Retorna True si se eliminó exitosamente, False si no existe.
        """
        for i, c in enumerate(self.clientes):
            if c.identificacion.lower() == identificacion.lower():
                self.clientes.pop(i)
                return True
        return False


__all__ = ["Restaurante"]

