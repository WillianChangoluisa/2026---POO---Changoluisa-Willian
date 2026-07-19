"""
Punto de entrada para el restaurante_app (Semana 8).
Menú interactivo por consola para registrar/listar productos, bebidas y clientes.
"""

from servicios.restaurante import Restaurante


def input_no_vacio(prompt: str) -> str:
    while True:
        valor = input(prompt).strip()
        if valor:
            return valor
        print("Entrada inválida: no puede estar vacía.")


def solicitar_float(prompt: str) -> float:
    while True:
        valor = input(prompt).strip()
        try:
            f = float(valor)
            if f <= 0:
                print("El valor debe ser mayor que cero.")
                continue
            return f
        except ValueError:
            print("Entrada inválida: ingrese un número válido.")


def registrar_producto_interactivo(restaurante: Restaurante) -> None:
    print("\n=== Registrar Producto ===")
    codigo = input_no_vacio("Código único: ")
    nombre = input_no_vacio("Nombre: ")
    categoria = input_no_vacio("Categoría: ")
    precio = solicitar_float("Precio: ")
    try:
        restaurante.crear_y_registrar_producto(codigo, nombre, categoria, precio)
        print(f"✅ Producto '{nombre}' registrado con código {codigo}.")
    except ValueError as e:
        print(f"Error: {e}")


def registrar_bebida_interactivo(restaurante: Restaurante) -> None:
    print("\n=== Registrar Bebida ===")
    codigo = input_no_vacio("Código único: ")
    nombre = input_no_vacio("Nombre: ")
    categoria = "Bebida"
    precio = solicitar_float("Precio: ")
    tamano = input_no_vacio("Tamaño (pequeno/mediano/grande): ")
    tipo_envase = input_no_vacio("Tipo de envase (lata/botella/vaso): ")
    try:
        restaurante.crear_y_registrar_bebida(codigo, nombre, categoria, precio, tamano, tipo_envase)
        print(f"✅ Bebida '{nombre}' registrada con código {codigo}.")
    except ValueError as e:
        print(f"Error: {e}")


def registrar_cliente_interactivo(restaurante: Restaurante) -> None:
    print("\n=== Registrar Cliente ===")
    identificacion = input_no_vacio("Identificación única: ")
    nombre = input_no_vacio("Nombre completo: ")
    correo = input_no_vacio("Correo: ")
    telefono = input("Teléfono (opcional): ").strip() or "No proporcionado"
    try:
        restaurante.crear_y_registrar_cliente(identificacion, nombre, correo, telefono)
        print(f"✅ Cliente '{nombre}' registrado con ID {identificacion}.")
    except ValueError as e:
        print(f"Error: {e}")


def listar_productos_interactivo(restaurante: Restaurante) -> None:
    print("\n=== Lista de Productos ===")
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    for i, p in enumerate(productos, start=1):
        print(f"\n[{i}] \n{p.mostrar_informacion()}")


def listar_clientes_interactivo(restaurante: Restaurante) -> None:
    print("\n=== Lista de Clientes ===")
    clientes = restaurante.listar_clientes()
    if not clientes:
        print("No hay clientes registrados.")
        return
    for i, c in enumerate(clientes, start=1):
        print(f"\n[{i}] \n{c.mostrar_informacion()}")


def actualizar_producto_interactivo(restaurante: Restaurante) -> None:
    print("\n=== Actualizar Producto ===")
    codigo = input_no_vacio("Código del producto a actualizar: ")
    producto = restaurante.buscar_producto_por_codigo(codigo)

    if not producto:
        print(f"❌ Producto con código '{codigo}' no encontrado.")
        return

    print(f"\nProducto actual: {producto.nombre}")
    print("(Dejar vacío para no cambiar)")

    nombre = input("Nuevo nombre (opcional): ").strip() or None
    categoria = input("Nueva categoría (opcional): ").strip() or None
    precio_str = input("Nuevo precio (opcional): ").strip()
    precio = None

    if precio_str:
        try:
            precio = float(precio_str)
            if precio <= 0:
                print("❌ El precio debe ser mayor que cero.")
                return
        except ValueError:
            print("❌ Precio inválido.")
            return

    try:
        restaurante.actualizar_producto(codigo, nombre, categoria, precio)
        print(f"✅ Producto '{codigo}' actualizado exitosamente.")
    except ValueError as e:
        print(f"❌ Error: {e}")


def actualizar_bebida_interactivo(restaurante: Restaurante) -> None:
    print("\n=== Actualizar Bebida ===")
    codigo = input_no_vacio("Código de la bebida a actualizar: ")
    producto = restaurante.buscar_producto_por_codigo(codigo)

    if not producto:
        print(f"❌ Bebida con código '{codigo}' no encontrado.")
        return

    from modelos.bebida import Bebida
    if not isinstance(producto, Bebida):
        print(f"❌ El código '{codigo}' no corresponde a una bebida.")
        return

    print(f"\nBebida actual: {producto.nombre}")
    print("(Dejar vacío para no cambiar)")

    nombre = input("Nuevo nombre (opcional): ").strip() or None
    categoria = input("Nueva categoría (opcional): ").strip() or None
    precio_str = input("Nuevo precio (opcional): ").strip()
    tamano = input("Nuevo tamaño (pequeno/mediano/grande, opcional): ").strip() or None
    tipo_envase = input("Nuevo tipo de envase (opcional): ").strip() or None

    precio = None
    if precio_str:
        try:
            precio = float(precio_str)
            if precio <= 0:
                print("❌ El precio debe ser mayor que cero.")
                return
        except ValueError:
            print("❌ Precio inválido.")
            return

    try:
        restaurante.actualizar_bebida(codigo, nombre, categoria, precio, tamano, tipo_envase)
        print(f"✅ Bebida '{codigo}' actualizada exitosamente.")
    except ValueError as e:
        print(f"❌ Error: {e}")


def eliminar_producto_interactivo(restaurante: Restaurante) -> None:
    print("\n=== Eliminar Producto ===")
    codigo = input_no_vacio("Código del producto a eliminar: ")

    producto = restaurante.buscar_producto_por_codigo(codigo)
    if not producto:
        print(f"❌ Producto con código '{codigo}' no encontrado.")
        return

    print(f"\nProducto a eliminar: {producto.nombre}")
    confirmacion = input("¿Está seguro? (s/n): ").strip().lower()

    if confirmacion == "s":
        if restaurante.eliminar_producto(codigo):
            print(f"✅ Producto '{codigo}' eliminado exitosamente.")
        else:
            print(f"❌ Error al eliminar el producto.")
    else:
        print("❌ Eliminación cancelada.")


def actualizar_cliente_interactivo(restaurante: Restaurante) -> None:
    print("\n=== Actualizar Cliente ===")
    identificacion = input_no_vacio("Identificación del cliente a actualizar: ")
    cliente = restaurante.buscar_cliente_por_id(identificacion)

    if not cliente:
        print(f"❌ Cliente con identificación '{identificacion}' no encontrado.")
        return

    print(f"\nCliente actual: {cliente.nombre}")
    print("(Dejar vacío para no cambiar)")

    nombre = input("Nuevo nombre (opcional): ").strip() or None
    correo = input("Nuevo correo (opcional): ").strip() or None
    telefono = input("Nuevo teléfono (opcional): ").strip() or None

    try:
        restaurante.actualizar_cliente(identificacion, nombre, correo, telefono)
        print(f"✅ Cliente '{identificacion}' actualizado exitosamente.")
    except ValueError as e:
        print(f"❌ Error: {e}")


def eliminar_cliente_interactivo(restaurante: Restaurante) -> None:
    print("\n=== Eliminar Cliente ===")
    identificacion = input_no_vacio("Identificación del cliente a eliminar: ")

    cliente = restaurante.buscar_cliente_por_id(identificacion)
    if not cliente:
        print(f"❌ Cliente con identificación '{identificacion}' no encontrado.")
        return

    print(f"\nCliente a eliminar: {cliente.nombre}")
    confirmacion = input("¿Está seguro? (s/n): ").strip().lower()

    if confirmacion == "s":
        if restaurante.eliminar_cliente(identificacion):
            print(f"✅ Cliente '{identificacion}' eliminado exitosamente.")
        else:
            print(f"❌ Error al eliminar el cliente.")
    else:
        print("❌ Eliminación cancelada.")


def mostrar_menu() -> None:
    print("\n" + "=" * 50)
    print("     SISTEMA DE RESTAURANTE - Semana 8")
    print("=" * 50)
    print("PRODUCTOS:")
    print("  1. Registrar producto")
    print("  2. Registrar bebida")
    print("  3. Actualizar producto")
    print("  4. Actualizar bebida")
    print("  5. Eliminar producto")
    print("  6. Listar productos")
    print("-" * 50)
    print("CLIENTES:")
    print("  7. Registrar cliente")
    print("  8. Actualizar cliente")
    print("  9. Eliminar cliente")
    print(" 10. Listar clientes")
    print("-" * 50)
    print(" 11. Salir")
    print("=" * 50)


def main() -> None:
    restaurante = Restaurante()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-11): ").strip()

        if opcion == "1":
            registrar_producto_interactivo(restaurante)
        elif opcion == "2":
            registrar_bebida_interactivo(restaurante)
        elif opcion == "3":
            actualizar_producto_interactivo(restaurante)
        elif opcion == "4":
            actualizar_bebida_interactivo(restaurante)
        elif opcion == "5":
            eliminar_producto_interactivo(restaurante)
        elif opcion == "6":
            listar_productos_interactivo(restaurante)
        elif opcion == "7":
            registrar_cliente_interactivo(restaurante)
        elif opcion == "8":
            actualizar_cliente_interactivo(restaurante)
        elif opcion == "9":
            eliminar_cliente_interactivo(restaurante)
        elif opcion == "10":
            listar_clientes_interactivo(restaurante)
        elif opcion == "11":
            print("Saliendo. ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()

