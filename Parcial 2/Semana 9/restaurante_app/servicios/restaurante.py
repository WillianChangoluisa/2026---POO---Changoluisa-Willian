from __future__ import annotations
from typing import List, Optional, Tuple, Dict, Set
from dataclasses import asdict
import json
import os

from ..modelos.producto import Producto
from ..modelos.usuario import Usuario


class Restaurante:
    """Servicio encargado de administrar productos y usuarios.

    Mantiene internamente listas para productos y usuarios y expone métodos
    para operar sobre ellas sin que main.py las manipule directamente.
    """

    def __init__(self, data_dir: str | None = None) -> None:
        # Listas dinámicas que almacenan objetos
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []

        # Tuple con opciones estables del sistema (ejemplo de tupla usada)
        self.OPCIONES: Tuple[str, ...] = (
            "Registrar producto",
            "Buscar producto",
            "Actualizar producto",
            "Eliminar producto",
            "Listar productos",
            "Registrar cliente",
            "Listar clientes",
            "Mostrar categorías",
            "Recargar datos",
            "Salir",
        )

        # Rutas de persistencia (carpeta data a nivel de Semana 9)
        # Permitir inyectar un directorio de datos (útil para pruebas)
        if data_dir:
            self._data_dir = data_dir
        else:
            package_dir = os.path.dirname(os.path.dirname(__file__))  # restaurante_app
            semana_dir = os.path.dirname(package_dir)
            self._data_dir = os.path.join(semana_dir, "data")
        os.makedirs(self._data_dir, exist_ok=True)
        self._productos_file = os.path.join(self._data_dir, "productos.json")
        self._clientes_file = os.path.join(self._data_dir, "clientes.json")

        # Cargar datos si existen
        self._load_productos()
        self._load_clientes()

    # --- Métodos de productos ---
    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un producto si su código no está duplicado.

        Retorna True si se registra correctamente, False si ya existe.
        """
        if self.buscar_producto_por_codigo(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        self._save_productos()
        return True

    def reload_data(self) -> None:
        """Recargar los datos desde los archivos JSON actuales."""
        self._load_productos()
        self._load_clientes()

    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        for p in self._productos:
            if p.codigo == codigo:
                return p
        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: Optional[str] = None,
        categoria: Optional[str] = None,
        precio: Optional[float] = None,
    ) -> bool:
        p = self.buscar_producto_por_codigo(codigo)
        if p is None:
            return False
        if nombre:
            p.nombre = nombre
        if categoria:
            p.categoria = categoria
        if precio is not None:
            p.precio = float(precio)
        self._save_productos()
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        p = self.buscar_producto_por_codigo(codigo)
        if p is None:
            return False
        self._productos.remove(p)
        self._save_productos()
        return True

    def listar_productos(self) -> List[Producto]:
        # Devolver una copia superficial para evitar que main.py manipule la lista interna
        return list(self._productos)

    # --- Métodos de usuarios ---
    def registrar_usuario(self, usuario: Usuario) -> bool:
        """Mantener compatibilidad con la API original y persistir el cliente.

        Este alias de registro debe comportarse igual que registrar_cliente para
        evitar inconsistencias al trabajar con usuarios/clientes.
        """
        if any(u.identificacion == usuario.identificacion for u in self._usuarios):
            return False
        self._usuarios.append(usuario)
        self._save_clientes()
        return True

    # Nuevos métodos: registrar_cliente / listar_clientes con persistencia en JSON
    def registrar_cliente(self, cliente: Usuario) -> bool:
        if any(u.identificacion == cliente.identificacion for u in self._usuarios):
            return False
        self._usuarios.append(cliente)
        self._save_clientes()
        return True

    def listar_clientes(self) -> List[Usuario]:
        return list(self._usuarios)

    def listar_usuarios(self) -> List[Usuario]:
        # Mantener compatibilidad
        return list(self._usuarios)

    # --- Persistencia JSON ---
    def _load_productos(self) -> None:
        try:
            if os.path.exists(self._productos_file):
                with open(self._productos_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                self._productos = [Producto(**item) for item in data]
            else:
                self._productos = []
        except Exception:
            self._productos = []

    def _save_productos(self) -> None:
        try:
            with open(self._productos_file, "w", encoding="utf-8") as f:
                json.dump([asdict(p) for p in self._productos], f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    def _load_clientes(self) -> None:
        try:
            if os.path.exists(self._clientes_file):
                with open(self._clientes_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                self._usuarios = [Usuario(**item) for item in data]
            else:
                self._usuarios = []
        except Exception:
            self._usuarios = []

    def _save_clientes(self) -> None:
        try:
            with open(self._clientes_file, "w", encoding="utf-8") as f:
                json.dump([asdict(u) for u in self._usuarios], f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    # --- Estructuras adicionales requeridas ---
    def obtener_categorias_unicas(self) -> Set[str]:
        # Uso de conjunto para representar categorías sin duplicados
        return {p.categoria for p in self._productos}

    def obtener_menu_map(self) -> Dict[str, int]:
        """Devuelve un diccionario clave->valor que relaciona la opción textual con su índice.

        Ejemplo de dict usado para mapear nombres a índices o acciones.
        """
        return {nombre: idx + 1 for idx, nombre in enumerate(self.OPCIONES)}

