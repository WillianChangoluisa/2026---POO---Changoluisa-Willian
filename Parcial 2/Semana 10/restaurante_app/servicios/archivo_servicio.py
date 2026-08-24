from __future__ import annotations

import json
from pathlib import Path

from ..modelos.producto import Producto


class ArchivoServicio:
    """Servicio encargado de guardar y cargar productos en formato JSON."""

    def __init__(self, ruta_archivo: str | Path | None = None) -> None:
        if ruta_archivo is None:
            base_dir = Path(__file__).resolve().parent.parent
            self.ruta_archivo = base_dir / "datos" / "productos.json"
        else:
            self.ruta_archivo = Path(ruta_archivo)

        self.ruta_archivo.parent.mkdir(parents=True, exist_ok=True)

    def cargar_productos(self) -> list[Producto]:
        """Lee el archivo JSON, valida cada registro y vuelve a construir objetos Producto."""
        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            self._crear_archivo_vacio()
            return []
        except json.JSONDecodeError as exc:
            print(f"Advertencia: el archivo de productos no tiene un formato JSON válido: {exc}")
            self._crear_archivo_vacio()
            return []
        except PermissionError as exc:
            print(f"No tienes permisos para leer {self.ruta_archivo}: {exc}")
            return []

        if not isinstance(datos, list):
            print("Advertencia: el archivo de productos no contiene una lista válida. Se inicializa vacío.")
            self._crear_archivo_vacio()
            return []

        productos: list[Producto] = []
        for indice, registro in enumerate(datos):
            try:
                productos.append(Producto.from_dict(registro))
            except (KeyError, TypeError, ValueError) as exc:
                print(f"Se ignoró un registro inválido en la posición {indice}: {exc}")

        return productos

    def guardar_productos(self, productos: list[Producto]) -> None:
        """Guarda la colección actual de productos en el archivo JSON."""
        try:
            with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump([producto.to_dict() for producto in productos], archivo, ensure_ascii=False, indent=2)
        except PermissionError as exc:
            raise PermissionError(f"No tienes permisos para escribir en {self.ruta_archivo}: {exc}") from exc
        except OSError as exc:
            raise OSError(f"No se pudo guardar la información de productos: {exc}") from exc

    def _crear_archivo_vacio(self) -> None:
        try:
            with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump([], archivo, ensure_ascii=False, indent=2)
        except PermissionError as exc:
            raise PermissionError(f"No tienes permisos para crear {self.ruta_archivo}: {exc}") from exc
        except OSError as exc:
            raise OSError(f"No se pudo inicializar el archivo de productos: {exc}") from exc
