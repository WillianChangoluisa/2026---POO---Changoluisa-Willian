"""Punto de entrada del sistema de restaurante (Semana 9).

Presenta un menú interactivo que utiliza Restaurante para administrar
productos y usuarios. main.py solicita datos mediante input() y no
manipula directamente las listas internas del servicio.
"""
from typing import Callable, Dict
# Manejar imports para permitir ejecutar `python main.py` desde dentro del
# directorio `restaurante_app` o ejecutar como módulo `python -m restaurante_app.main`
if __package__ is None or __package__ == "":
    # Ejecutado como script: agregar la carpeta padre al sys.path y usar imports absolutos
    import os
    import sys

    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)
    from restaurante_app.servicios.restaurante import Restaurante
    from restaurante_app.modelos.producto import Producto
    from restaurante_app.modelos.usuario import Usuario
else:
    # Ejecutado como paquete
    from .servicios.restaurante import Restaurante
    from .modelos.producto import Producto
    from .modelos.usuario import Usuario


def solicitar_producto_desde_input() -> Producto:
    codigo = input("Código del producto: ").strip()
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()
    while True:
        precio_str = input("Precio: ").strip()
        try:
            precio = float(precio_str)
            break
        except ValueError:
            print("Precio inválido. Ingrese un número válido.")
    return Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio)


def solicitar_usuario_desde_input() -> Usuario:
    identificacion = input("Identificación: ").strip()
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    return Usuario(identificacion=identificacion, nombre=nombre, correo=correo)


def main() -> None:
    restaurante: Restaurante = Restaurante()

    # Uso de tupla para menu estable
    opciones = restaurante.OPCIONES

    # Diccionario que relaciona la opción numérica con la función manejadora
    acciones: Dict[int, Callable[[], None]] = {}

    def registrar_producto() -> None:
        try:
            producto = solicitar_producto_desde_input()
        except Exception as e:
            print(f"Error al crear producto: {e}")
            return
        if restaurante.registrar_producto(producto):
            print("Producto registrado correctamente.")
        else:
            print("Ya existe un producto con ese código.")

    def buscar_producto() -> None:
        codigo = input("Ingrese código a buscar: ").strip()
        p = restaurante.buscar_producto_por_codigo(codigo)
        if p:
            print("Producto encontrado:")
            print(p.mostrar_informacion())
        else:
            print("Producto no encontrado.")

    def actualizar_producto() -> None:
        codigo = input("Código del producto a actualizar: ").strip()
        if restaurante.buscar_producto_por_codigo(codigo) is None:
            print("Producto no encontrado.")
            return
        nombre = input("Nuevo nombre (enter para omitir): ").strip() or None
        categoria = input("Nueva categoría (enter para omitir): ").strip() or None
        precio = None
        precio_str = input("Nuevo precio (enter para omitir): ").strip()
        if precio_str:
            try:
                precio = float(precio_str)
            except ValueError:
                print("Precio inválido; se omitirá la actualización de precio.")
                precio = None
        ok = restaurante.actualizar_producto(codigo, nombre=nombre, categoria=categoria, precio=precio)
        if ok:
            print("Producto actualizado correctamente.")
        else:
            print("No se pudo actualizar el producto.")

    def eliminar_producto() -> None:
        codigo = input("Código del producto a eliminar: ").strip()
        if restaurante.eliminar_producto(codigo):
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def listar_productos() -> None:
        productos = restaurante.listar_productos()
        if not productos:
            print("No hay productos registrados.")
            return
        print("Productos registrados:")
        for p in productos:
            print(p.mostrar_informacion())

    def registrar_usuario() -> None:
        # Mantener compatibilidad pero usar la nomenclatura cliente
        try:
            cliente = solicitar_usuario_desde_input()
        except Exception as e:
            print(f"Error al crear cliente: {e}")
            return
        if hasattr(restaurante, 'registrar_cliente'):
            ok = restaurante.registrar_cliente(cliente)
        else:
            ok = restaurante.registrar_usuario(cliente)
        if ok:
            print("Cliente registrado correctamente.")
        else:
            print("Ya existe un cliente con esa identificación.")

    def listar_usuarios() -> None:
        # Mostrar clientes
        if hasattr(restaurante, 'listar_clientes'):
            usuarios = restaurante.listar_clientes()
        else:
            usuarios = restaurante.listar_usuarios()
        if not usuarios:
            print("No hay clientes registrados.")
            return
        print("Clientes registrados:")
        for u in usuarios:
            print(u.mostrar_informacion())

    def mostrar_categorias() -> None:
        categorias = restaurante.obtener_categorias_unicas()
        if not categorias:
            print("No hay categorías para mostrar.")
            return
        print("Categorías únicas:")
        for c in sorted(categorias):
            print(f"- {c}")

    def recargar_datos() -> None:
        restaurante.reload_data()
        print("Datos recargados desde los archivos JSON.")

    acciones = {
        1: registrar_producto,
        2: buscar_producto,
        3: actualizar_producto,
        4: eliminar_producto,
        5: listar_productos,
        6: registrar_usuario,
        7: listar_usuarios,
        8: mostrar_categorias,
        9: recargar_datos,
        10: lambda: None,
    }

    while True:
        print("=" * 40)
        print("\tSISTEMA DE RESTAURANTE")
        print("=" * 40)
        for idx, texto in enumerate(opciones, start=1):
            print(f"{idx}. {texto}")
        try:
            opcion_str = input("Seleccione una opción: ").strip()
            opcion = int(opcion_str)
        except ValueError:
            print("Opción inválida. Ingrese un número.")
            continue

        if opcion == len(opciones):  # opción salir
            print("Saliendo...")
            break

        accion = acciones.get(opcion)
        if accion is None:
            print("Opción no válida.")
            continue
        try:
            accion()
        except Exception as e:
            print(f"Ocurrió un error al ejecutar la acción: {e}")


if __name__ == "__main__":
    main()

