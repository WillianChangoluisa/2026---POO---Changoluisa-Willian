"""
Módulo restaurante.py
Contiene la clase Restaurante que administra productos y clientes.
Esta clase implementa la arquitectura por capas (capa de servicios).
"""

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Clase de servicio encargada de administrar los registros de products y clientes.

    Responsabilidades:
        - Mantener listas de productos y clientes registrados
        - Proporcionar métodos para registrar, listar y buscar productos
        - Proporcionar métodos para registrar, listar y buscar clientes
        - Validar la información antes de crear registros
    """

    def __init__(self, nombre_negocio="Mi Restaurante"):
        """
        Constructor de la clase Restaurante.

        Args:
            nombre_negocio (str): Nombre del restaurante
        """
        self.nombre_negocio = nombre_negocio
        self.productos = []  # Lista para almacenar objetos Producto
        self.clientes = []   # Lista para almacenar objetos Cliente

    # ======================== MÉTODOS PARA PRODUCTOS ========================

    def registrar_producto(self, nombre, categoria, precio, disponible=True):
        """
        Registra un nuevo producto en el restaurante.

        Crea un objeto Producto a partir de los parámetros ingresados y lo almacena
        en la lista de productos. Utiliza el constructor de la clase Producto.

        Args:
            nombre (str): Nombre del producto
            categoria (str): Categoría del producto
            precio (float): Precio unitario del producto
            disponible (bool): Estado de disponibilidad (por defecto True)

        Returns:
            Producto: El objeto producto creado

        Raises:
            ValueError: Si el producto ya existe o los datos son inválidos
        """
        # Validar que el producto no exista ya
        if self._producto_existe(nombre):
            raise ValueError(f"El producto '{nombre}' ya está registrado.")

        try:
            # Crear el objeto Producto usando su constructor
            producto = Producto(nombre, categoria, precio, disponible)
            self.productos.append(producto)
            return producto
        except ValueError as e:
            raise ValueError(f"Error al registrar producto: {str(e)}")

    def listar_productos(self):
        """
        Retorna la lista completa de productos registrados.

        Returns:
            list: Lista de objetos Producto
        """
        return self.productos

    def buscar_producto_por_nombre(self, nombre):
        """
        Busca un producto por su nombre (búsqueda exacta).

        Args:
            nombre (str): Nombre del producto a buscar

        Returns:
            Producto: El objeto Producto si se encuentra, None en caso contrario
        """
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def buscar_productos_por_categoria(self, categoria):
        """
        Busca todos los productos que pertenecen a una categoría.

        Args:
            categoria (str): Categoría a buscar

        Returns:
            list: Lista de productos que coinciden con la categoría
        """
        resultados = []
        for producto in self.productos:
            if producto.categoria.lower() == categoria.lower():
                resultados.append(producto)
        return resultados

    def _producto_existe(self, nombre):
        """
        Verifica si un producto con ese nombre ya está registrado.

        Args:
            nombre (str): Nombre del producto a verificar

        Returns:
            bool: True si el producto existe, False en caso contrario
        """
        return self.buscar_producto_por_nombre(nombre) is not None

    # ======================== MÉTODOS PARA CLIENTES ========================

    def registrar_cliente(self, nombre, correo, id_cliente, telefono="No proporcionado"):
        """
        Registra un nuevo cliente en el restaurante.

        Crea un objeto Cliente a partir de los parámetros ingresados y lo almacena
        en la lista de clientes. Utiliza el constructor de la clase Cliente (dataclass).

        Args:
            nombre (str): Nombre completo del cliente
            correo (str): Correo electrónico del cliente
            id_cliente (str): ID único del cliente
            telefono (str): Número telefónico (opcional)

        Returns:
            Cliente: El objeto cliente creado

        Raises:
            ValueError: Si el cliente ya existe o los datos son inválidos
        """
        # Validar que el cliente no exista ya
        if self._cliente_existe(id_cliente):
            raise ValueError(f"El cliente con ID '{id_cliente}' ya está registrado.")

        try:
            # Crear el objeto Cliente usando su constructor (dataclass)
            cliente = Cliente(nombre, correo, id_cliente, telefono)
            self.clientes.append(cliente)
            return cliente
        except ValueError as e:
            raise ValueError(f"Error al registrar cliente: {str(e)}")

    def listar_clientes(self):
        """
        Retorna la lista completa de clientes registrados.

        Returns:
            list: Lista de objetos Cliente
        """
        return self.clientes

    def buscar_cliente_por_id(self, id_cliente):
        """
        Busca un cliente por su ID.

        Args:
            id_cliente (str): ID del cliente a buscar

        Returns:
            Cliente: El objeto Cliente si se encuentra, None en caso contrario
        """
        for cliente in self.clientes:
            if cliente.id_cliente.lower() == id_cliente.lower():
                return cliente
        return None

    def buscar_cliente_por_nombre(self, nombre):
        """
        Busca clientes por nombre (búsqueda parcial, contiene).

        Args:
            nombre (str): Nombre o parte del nombre a buscar

        Returns:
            list: Lista de clientes que coinciden con el criterio
        """
        resultados = []
        for cliente in self.clientes:
            if nombre.lower() in cliente.nombre.lower():
                resultados.append(cliente)
        return resultados

    def _cliente_existe(self, id_cliente):
        """
        Verifica si un cliente con ese ID ya está registrado.

        Args:
            id_cliente (str): ID del cliente a verificar

        Returns:
            bool: True si el cliente existe, False en caso contrario
        """
        return self.buscar_cliente_por_id(id_cliente) is not None

    # ======================== MÉTODOS INFORMATIVOS ========================

    def obtener_resumen(self):
        """
        Retorna un resumen del estado actual del restaurante.

        Returns:
            str: Información sobre la cantidad de productos y clientes registrados
        """
        return (
            f"{'=' * 40}\n"
            f"Restaurante: {self.nombre_negocio}\n"
            f"Productos registrados: {len(self.productos)}\n"
            f"Clientes registrados: {len(self.clientes)}\n"
            f"{'=' * 40}"
        )

