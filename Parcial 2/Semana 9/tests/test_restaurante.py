import json
from dataclasses import asdict
from pathlib import Path
import pytest

from restaurante_app.servicios.restaurante import Restaurante
from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario


def test_registrar_producto_y_evitar_duplicado(tmp_path: Path):
    data_dir = tmp_path
    r = Restaurante(data_dir=str(data_dir))

    p = Producto(codigo="t1", nombre="Test", categoria="Cat", precio=1.0)
    assert r.registrar_producto(p) is True
    # intentar duplicado
    assert r.registrar_producto(p) is False

    # persisted
    contenido = json.loads((data_dir / "productos.json").read_text(encoding="utf-8"))
    assert any(item["codigo"] == "t1" for item in contenido)


def test_registrar_cliente_y_evitar_duplicado(tmp_path: Path):
    data_dir = tmp_path
    r = Restaurante(data_dir=str(data_dir))

    c = Usuario(identificacion="u1", nombre="Uno", correo="u1@example.com")
    assert r.registrar_cliente(c) is True
    assert r.registrar_cliente(c) is False

    contenido = json.loads((data_dir / "clientes.json").read_text(encoding="utf-8"))
    assert any(item["identificacion"] == "u1" for item in contenido)


def test_update_and_delete_producto(tmp_path: Path):
    data_dir = tmp_path
    r = Restaurante(data_dir=str(data_dir))

    p = Producto(codigo="t2", nombre="T2", categoria="C", precio=5.0)
    r.registrar_producto(p)
    assert r.actualizar_producto("t2", nombre="Nuevo", precio=6.5) is True
    prod = r.buscar_producto_por_codigo("t2")
    assert prod is not None and prod.nombre == "Nuevo" and abs(prod.precio - 6.5) < 1e-6

    assert r.eliminar_producto("t2") is True
    assert r.buscar_producto_por_codigo("t2") is None


def test_categorias_unicas(tmp_path: Path):
    data_dir = tmp_path
    r = Restaurante(data_dir=str(data_dir))
    r.registrar_producto(Producto(codigo="a1", nombre="A", categoria="X", precio=1))
    r.registrar_producto(Producto(codigo="a2", nombre="B", categoria="Y", precio=2))
    r.registrar_producto(Producto(codigo="a3", nombre="C", categoria="X", precio=3))
    cats = r.obtener_categorias_unicas()
    assert cats == {"X", "Y"}


def test_persistencia_reload(tmp_path: Path):
    data_dir = tmp_path
    r1 = Restaurante(data_dir=str(data_dir))
    r1.registrar_producto(Producto(codigo="pA", nombre="PA", categoria="Z", precio=9))
    r1.registrar_cliente(Usuario(identificacion="cA", nombre="CA", correo="ca@example.com"))

    # crear nueva instancia que debe cargar los datos desde disco
    r2 = Restaurante(data_dir=str(data_dir))
    assert r2.buscar_producto_por_codigo("pA") is not None
    assert any(u.identificacion == "cA" for u in r2.listar_clientes())
