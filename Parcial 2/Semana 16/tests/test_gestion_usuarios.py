from pathlib import Path

from restaurante_app.modelos.usuario import Usuario
from restaurante_app.servicios.archivo_servicio import ArchivoServicio
from restaurante_app.servicios.restaurante_servicio import RestauranteServicio


def crear_servicio(ruta: Path) -> RestauranteServicio:
    archivos = ArchivoServicio(ruta)
    archivos.guardar_usuarios(
        [
            Usuario(
                "admin",
                "Administrador",
                "admin@restaurante.com",
                "1712345678",
                "0998765432",
                "1234",
                "Administrador",
            ),
            Usuario(
                "cajero",
                "Cajero",
                "cajero@restaurante.com",
                "1712345679",
                "0998765433",
                "5678",
                "Empleado",
            ),
        ]
    )
    return RestauranteServicio(archivos)


def test_registra_actualiza_y_elimina_usuario_con_persistencia(tmp_path: Path) -> None:
    servicio = crear_servicio(tmp_path)

    ok, _ = servicio.registrar_usuario(
        "ana",
        "Ana López",
        "ana@example.com",
        "1720000001",
        "0991000001",
        "secreto",
        "Cliente",
        "admin",
    )
    assert ok

    ok, _ = servicio.actualizar_usuario(
        "ana",
        "Ana Torres",
        "ana@example.com",
        "1720000001",
        "0991000001",
        "",
        "Empleado",
        "admin",
    )
    assert ok
    assert servicio.cargar_usuario("ana").password == "secreto"
    assert servicio.cargar_usuario("ana").rol == "Empleado"

    servicio = RestauranteServicio(ArchivoServicio(tmp_path))
    assert servicio.cargar_usuario("ana").nombre == "Ana Torres"
    assert servicio.cargar_usuario("ana").rol == "Empleado"
    assert servicio.eliminar_usuario("ana", "admin")[0]
    assert servicio.cargar_usuario("ana") is None


def test_rechaza_gestion_de_usuario_no_administrador(tmp_path: Path) -> None:
    servicio = crear_servicio(tmp_path)

    ok, mensaje = servicio.registrar_usuario(
        "otro",
        "Otro Usuario",
        "otro@example.com",
        "1720000002",
        "0991000002",
        "secreto",
        "Cliente",
        "cajero",
    )

    assert not ok
    assert "Administrador" in mensaje


def test_protege_cuenta_administrativa_autenticada(tmp_path: Path) -> None:
    servicio = crear_servicio(tmp_path)

    ok, mensaje = servicio.eliminar_usuario("admin", "admin")

    assert not ok
    assert "eliminar" in mensaje.lower()
    assert servicio.cargar_usuario("admin") is not None


def test_rechaza_correo_duplicado(tmp_path: Path) -> None:
    servicio = crear_servicio(tmp_path)

    ok, mensaje = servicio.registrar_usuario(
        "nuevo",
        "Nuevo Usuario",
        "cajero@restaurante.com",
        "1720000002",
        "0991000002",
        "secreto",
        "Cliente",
        "admin",
    )

    assert not ok
    assert "correo ya está registrado" in mensaje


def test_asigna_roles_a_registros_anteriores() -> None:
    usuario = Usuario.from_dict(
        {
            "identificacion": "admin",
            "nombre": "Administrador",
            "correo": "admin@restaurante.com",
            "cedula": "1712345678",
            "celular": "0998765432",
            "password": "1234",
        }
    )

    assert usuario.rol == "Administrador"
