from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..modelos.producto import Producto
from ..modelos.usuario import Usuario


class ArchivoServicio:
    """Lee y escribe productos y usuarios almacenados en archivos JSON."""

    def __init__(self, ruta_base: str | Path | None = None) -> None:
        if ruta_base is None:
            self.ruta_base = Path(__file__).resolve().parent.parent / "datos"
        else:
            self.ruta_base = Path(ruta_base)

        self.ruta_base.mkdir(parents=True, exist_ok=True)
        self.ruta_productos = self.ruta_base / "productos.json"
        self.ruta_usuarios = self.ruta_base / "usuarios.json"

    def cargar_productos(self) -> list[Producto]:
        datos = self._leer_json(self.ruta_productos, "productos")
        productos: list[Producto] = []
        for indice, registro in enumerate(datos):
            try:
                productos.append(Producto.from_dict(registro))
            except (KeyError, TypeError, ValueError) as exc:
                print(f"Se ignoró un registro inválido en productos en la posición {indice}: {exc}")
        return productos

    def guardar_productos(self, productos: list[Producto]) -> None:
        self._guardar_json(self.ruta_productos, [producto.to_dict() for producto in productos], "productos")

    def cargar_usuarios(self) -> list[Usuario]:
        datos = self._leer_json(self.ruta_usuarios, "usuarios")
        usuarios: list[Usuario] = []
        for indice, registro in enumerate(datos):
            try:
                usuarios.append(Usuario.from_dict(registro))
            except (KeyError, TypeError, ValueError) as exc:
                print(f"Se ignoró un registro inválido en usuarios en la posición {indice}: {exc}")
        return usuarios

    def guardar_usuarios(self, usuarios: list[Usuario]) -> None:
        self._guardar_json(self.ruta_usuarios, [usuario.to_dict() for usuario in usuarios], "usuarios")

    def _leer_json(self, ruta: Path, nombre: str) -> list[dict[str, Any]]:
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            self._crear_archivo_vacio(ruta)
            return []
        except json.JSONDecodeError as exc:
            print(f"Advertencia: el archivo de {nombre} no tiene un formato JSON válido: {exc}")
            self._crear_archivo_vacio(ruta)
            return []
        except PermissionError as exc:
            raise PermissionError(f"No tienes permisos para leer {ruta}: {exc}") from exc

        if not isinstance(datos, list):
            print(f"Advertencia: el archivo de {nombre} no contiene una lista válida. Se inicializa vacío.")
            self._crear_archivo_vacio(ruta)
            return []

        return datos

    def _guardar_json(self, ruta: Path, contenido: list[dict[str, Any]], nombre: str) -> None:
        try:
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(contenido, archivo, ensure_ascii=False, indent=2)
        except PermissionError as exc:
            raise PermissionError(f"No tienes permisos para escribir en {ruta}: {exc}") from exc
        except OSError as exc:
            raise OSError(f"No se pudo guardar la información de {nombre}: {exc}") from exc

    def _crear_archivo_vacio(self, ruta: Path) -> None:
        try:
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump([], archivo, ensure_ascii=False, indent=2)
        except PermissionError as exc:
            raise PermissionError(f"No tienes permisos para crear {ruta}: {exc}") from exc
        except OSError as exc:
            raise OSError(f"No se pudo inicializar el archivo {ruta}: {exc}") from exc
