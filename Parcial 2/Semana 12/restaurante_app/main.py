from __future__ import annotations

import os
import sys
from typing import Callable, Dict

if __package__ is None or __package__ == "":
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)
    from restaurante_app.modelos.producto import Producto
    from restaurante_app.modelos.usuario import Usuario
    from restaurante_app.servicios.restaurante import Restaurante
else:
    from .modelos.producto import Producto
    from .modelos.usuario import Usuario
    from .servicios.restaurante import Restaurante


def solicitar_producto_desde_input() -> Producto:
    codigo = input("Código del producto: ").strip()
    nombre = input("Nombre del producto: ").strip()
    categoria = input("Categoría: ").strip()

    while True:
        precio_texto = input("Precio: ").strip()
        try:
            precio = float(precio_texto)
            break
        except ValueError:
            print("Precio inválido. Ingrese un número válido.")

    while True:
        stock_texto = input("Stock inicial: ").strip()
        try:
            stock = int(stock_texto)
            if stock < 0:
                print("El stock no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Stock inválido. Ingrese un número entero válido.")

    return Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio, stock=stock)


def solicitar_usuario_desde_input() -> Usuario:
    identificacion = input("Identificación: ").strip()
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    cedula = input("Cédula (10 dígitos): ").strip()
    celular = input("Celular (10 dígitos, ejemplo: 0998765432): ").strip()
    return Usuario(
        identificacion=identificacion,
        nombre=nombre,
        correo=correo,
        cedula=cedula,
        celular=celular,
    )


def mostrar_menu() -> None:
    print("=" * 50)
    print("SISTEMA DE RESTAURANTE - SEMANA 11")
    print("=" * 50)


def main() -> None:
    restaurante = Restaurante()

    def registrar_producto() -> None:
        try:
            producto = solicitar_producto_desde_input()
            if restaurante.registrar_producto(producto):
                print("Producto registrado correctamente.")
            else:
                print("Ya existe un producto con ese código.")
        except ValueError as exc:
            print(f"Error al registrar el producto: {exc}")
        except PermissionError as exc:
            print(f"No se pudo guardar el producto: {exc}")

    def buscar_producto() -> None:
        codigo = input("Ingrese el código a buscar: ").strip()
        producto = restaurante.buscar_producto(codigo)
        if producto is None:
            print("Producto no encontrado.")
            return
        print(producto.mostrar_informacion())

    def actualizar_producto() -> None:
        codigo = input("Código del producto a actualizar: ").strip()
        producto = restaurante.buscar_producto(codigo)
        if producto is None:
            print("Producto no encontrado.")
            return

        nombre = input("Nuevo nombre (enter para omitir): ").strip() or None
        categoria = input("Nueva categoría (enter para omitir): ").strip() or None
        precio = None
        precio_texto = input("Nuevo precio (enter para omitir): ").strip()
        if precio_texto:
            try:
                precio = float(precio_texto)
            except ValueError:
                print("Precio inválido. Se omitirá el cambio de precio.")
                precio = None

        stock = None
        stock_texto = input("Nuevo stock (enter para omitir): ").strip()
        if stock_texto:
            try:
                stock = int(stock_texto)
                if stock < 0:
                    print("El stock no puede ser negativo. Se omitirá el cambio.")
                    stock = None
            except ValueError:
                print("Stock inválido. Se omitirá el cambio de stock.")
                stock = None

        try:
            if restaurante.actualizar_producto(codigo, nombre=nombre, categoria=categoria, precio=precio, stock=stock):
                print("Producto actualizado correctamente.")
        except ValueError as exc:
            print(f"No se pudo actualizar el producto: {exc}")

    def eliminar_producto() -> None:
        codigo = input("Código del producto a eliminar: ").strip()
        if restaurante.eliminar_producto(codigo):
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    def listar_productos() -> None:
        productos = restaurante.listar_productos()
        if not productos:
            print("No hay productos registrados.")
            return
        for producto in productos:
            print(producto.mostrar_informacion())

    def registrar_usuario() -> None:
        try:
            usuario = solicitar_usuario_desde_input()
            if restaurante.registrar_usuario(usuario):
                print("Usuario registrado correctamente.")
            else:
                print("Ya existe un usuario con esa identificación.")
        except ValueError as exc:
            print(f"Error al registrar usuario: {exc}")

    def buscar_usuario() -> None:
        identificacion = input("Ingrese la identificación a buscar: ").strip()
        usuario = restaurante.buscar_usuario(identificacion)
        if usuario is None:
            print("Usuario no encontrado.")
            return
        print(usuario.mostrar_informacion())

    def listar_usuarios() -> None:
        usuarios = restaurante.listar_usuarios()
        if not usuarios:
            print("No hay usuarios registrados.")
            return
        for usuario in usuarios:
            print(usuario.mostrar_informacion())

    def vender_producto() -> None:
        identificacion = input("Identificación del usuario: ").strip()
        codigo = input("Código del producto: ").strip()

        while True:
            cantidad_texto = input("Cantidad a vender: ").strip()
            try:
                cantidad = int(cantidad_texto)
                break
            except ValueError:
                print("Cantidad inválida. Ingrese un número entero.")

        if restaurante.vender_producto(codigo, identificacion, cantidad):
            print("Venta registrada correctamente.")
        else:
            print("La venta no pudo realizarse. Verifique usuario, producto, cantidad y stock.")

    def consultar_ventas_por_usuario() -> None:
        identificacion = input("Identificación del usuario: ").strip()
        ventas = restaurante.consultar_ventas_por_usuario(identificacion)
        if not ventas:
            print("Este usuario no tiene ventas registradas.")
            return
        for venta in ventas:
            producto = restaurante.buscar_producto(venta.producto_codigo)
            nombre_producto = producto.nombre if producto is not None else "Producto no disponible"
            print(f"Usuario: {venta.usuario_id} | Producto: {nombre_producto} | Cantidad: {venta.cantidad}")

    def listar_ventas() -> None:
        ventas = restaurante.listar_ventas()
        if not ventas:
            print("No hay ventas registradas.")
            return
        for venta in ventas:
            print(venta.mostrar_informacion())

    def mostrar_categorias() -> None:
        categorias = restaurante.obtener_categorias_unicas()
        if not categorias:
            print("No hay categorías registradas.")
            return
        for categoria in sorted(categorias):
            print(f"- {categoria}")

    acciones: Dict[int, Callable[[], None]] = {
        1: registrar_producto,
        2: buscar_producto,
        3: actualizar_producto,
        4: eliminar_producto,
        5: listar_productos,
        6: registrar_usuario,
        7: buscar_usuario,
        8: listar_usuarios,
        9: vender_producto,
        10: consultar_ventas_por_usuario,
        11: listar_ventas,
        12: mostrar_categorias,
        13: lambda: None,
    }

    while True:
        mostrar_menu()
        for indice, descripcion in enumerate(restaurante.OPCIONES, start=1):
            print(f"{indice}. {descripcion}")

        try:
            opcion = int(input("Seleccione una opción: ").strip())
        except EOFError:
            print("\nEntrada finalizada. Saliendo...")
            break
        except ValueError:
            print("Opción inválida. Debe ingresar un número.")
            continue

        if opcion == len(restaurante.OPCIONES):
            print("Saliendo del sistema...")
            break

        accion = acciones.get(opcion)
        if accion is None:
            print("Opción no válida.")
            continue

        try:
            accion()
        except EOFError:
            print("\nEntrada finalizada durante la acción. Saliendo...")
            break
        except PermissionError as exc:
            print(f"Error de permisos: {exc}")
        except OSError as exc:
            print(f"Error de archivo: {exc}")
        except Exception as exc:
            print(f"Ocurrió un error inesperado: {exc}")


if __name__ == "__main__":
    main()
