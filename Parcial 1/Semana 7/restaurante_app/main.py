"""
Sistema de Restaurante - Programa Principal (main.py)
Aplicación didáctica que demuestra los conceptos de POO en Python:
- Constructores (__init__)
- Decoradores (@property y @setter)
- Decoradores (@dataclass)
- Arquitectura modular por capas

Arquitectura:
    modelos/ (Capa de datos) → Producto, Cliente
    servicios/ (Capa de negocio) → Restaurante
    main.py (Capa de presentación) → Menú interactivo
"""

from servicios.restaurante import Restaurante


# ======================== FUNCIONES AUXILIARES ========================

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_encabezado():
    """Muestra el encabezado principal del sistema."""
    print("\n" + "=" * 50)
    print("    🍽️  SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("    Aplicación de Programación Orientada a Objetos")
    print("=" * 50 + "\n")


def mostrar_menu():
    """Muestra el menú interactivo principal."""
    print("\n" + "-" * 50)
    print("MENÚ PRINCIPAL")
    print("-" * 50)
    print("📦 GESTIÓN DE PRODUCTOS")
    print("  1. Registrar producto")
    print("  2. Listar todos los productos")
    print("  3. Buscar producto")
    print("-" * 50)
    print("👥 GESTIÓN DE CLIENTES")
    print("  4. Registrar cliente")
    print("  5. Listar todos los clientes")
    print("  6. Buscar cliente")
    print("-" * 50)
    print("ℹ️  INFORMACIÓN")
    print("  7. Ver resumen del restaurante")
    print("  0. Salir")
    print("-" * 50)


def pausar():
    """Pausa la ejecución esperando que el usuario presione una tecla."""
    input("\n➜ Presiona ENTER para continuar...")


def mostrar_error(mensaje):
    """Muestra un mensaje de error formateado."""
    print(f"\n❌ ERROR: {mensaje}")


def mostrar_exito(mensaje):
    """Muestra un mensaje de éxito formateado."""
    print(f"\n✅ {mensaje}")


# ======================== FUNCIONES DE PRODUCTOS ========================

def registrar_producto(restaurante):
    """
    Solicita datos al usuario y registra un nuevo producto.

    Flujo didáctico:
    input() usuario → validación → constructor Producto → clase Restaurante → almacenamiento

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante
    """
    print("\n" + "=" * 50)
    print("REGISTRAR NUEVO PRODUCTO")
    print("=" * 50)
    print("Información educativa: En este paso, los datos ingresados por el usuario")
    print("serán transformados en un objeto Producto mediante su constructor.")
    print("-" * 50)

    try:
        # Entrada del usuario
        nombre = input("📝 Nombre del producto: ").strip()
        categoria = input("🏷️  Categoría (ej: Entrada, Plato Principal, Bebida): ").strip()
        precio_str = input("💰 Precio en $ (debe ser > 0): ").strip()
        disponible_str = input("✅ ¿Disponible ahora? (S/N, por defecto S): ").strip().upper()

        # Convertir entrada a booleano
        disponible = disponible_str != "N"

        # Llamar al servicio que crea el objeto Producto
        producto = restaurante.registrar_producto(nombre, categoria, precio_str, disponible)

        # Mostrar resultado
        mostrar_exito(f"Producto '{nombre}' registrado correctamente.")
        print("\n📊 Información del producto creado:")
        print(producto.mostrar_informacion())

    except ValueError as e:
        mostrar_error(str(e))


def listar_productos(restaurante):
    """
    Lista todos los productos registrados en el restaurante.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante
    """
    print("\n" + "=" * 50)
    print("LISTA DE PRODUCTOS")
    print("=" * 50)

    productos = restaurante.listar_productos()

    if not productos:
        print("\n📭 No hay productos registrados en este momento.")
        print("Consejo: Registra tu primer producto usando la opción 1.")
    else:
        print(f"\n📦 Total de productos: {len(productos)}\n")
        # Mostrar cada producto en una sola línea incluyendo su estado de disponibilidad
        for i, producto in enumerate(productos, 1):
            estado = "✓ Disponible" if producto.disponible else "✗ No disponible"
            # Mostrar nombre, categoría, precio y estado para facilitar lectura en el listado
            print(f"{i}. {producto.nombre} ({producto.categoria}) - ${producto.precio:.2f} - {estado}")


def buscar_producto(restaurante):
    """
    Busca un producto por nombre y muestra su información detallada.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante
    """
    print("\n" + "=" * 50)
    print("BUSCAR PRODUCTO")
    print("=" * 50)

    nombre = input("🔍 Ingresa el nombre del producto a buscar: ").strip()

    if not nombre:
        mostrar_error("Debes ingresar un nombre para buscar.")
        return

    producto = restaurante.buscar_producto_por_nombre(nombre)

    if producto:
        print(f"\n✅ Producto encontrado:")
        print(producto.mostrar_informacion())
    else:
        print(f"\n❌ No se encontró ningún producto con el nombre '{nombre}'.")


# ======================== FUNCIONES DE CLIENTES ========================

def registrar_cliente(restaurante):
    """
    Solicita datos al usuario y registra un nuevo cliente.

    Flujo didáctico:
    input() usuario → validación → constructor Cliente (dataclass) → clase Restaurante → almacenamiento

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante
    """
    print("\n" + "=" * 50)
    print("REGISTRAR NUEVO CLIENTE")
    print("=" * 50)
    print("Información educativa: En este paso, los datos ingresados por el usuario")
    print("serán transformados en un objeto Cliente mediante @dataclass.")
    print("-" * 50)

    try:
        # Entrada del usuario
        nombre = input("👤 Nombre completo del cliente: ").strip()
        correo = input("📧 Correo electrónico: ").strip()
        id_cliente = input("🔑 ID único del cliente (ej: C001): ").strip()
        telefono = input("📞 Teléfono (opcional): ").strip()

        if not telefono:
            telefono = "No proporcionado"

        # Llamar al servicio que crea el objeto Cliente
        cliente = restaurante.registrar_cliente(nombre, correo, id_cliente, telefono)

        # Mostrar resultado
        mostrar_exito(f"Cliente '{nombre}' registrado correctamente.")
        print("\n📊 Información del cliente creado:")
        print(cliente.mostrar_informacion())

    except ValueError as e:
        mostrar_error(str(e))


def listar_clientes(restaurante):
    """
    Lista todos los clientes registrados en el restaurante.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante
    """
    print("\n" + "=" * 50)
    print("LISTA DE CLIENTES")
    print("=" * 50)

    clientes = restaurante.listar_clientes()

    if not clientes:
        print("\n📭 No hay clientes registrados en este momento.")
        print("Consejo: Registra tu primer cliente usando la opción 4.")
    else:
        print(f"\n👥 Total de clientes: {len(clientes)}\n")
        for i, cliente in enumerate(clientes, 1):
            print(f"{i}. {cliente}")


def buscar_cliente(restaurante):
    """
    Busca un cliente por ID o nombre y muestra su información detallada.

    Args:
        restaurante (Restaurante): Instancia del servicio restaurante
    """
    print("\n" + "=" * 50)
    print("BUSCAR CLIENTE")
    print("=" * 50)
    print("1. Buscar por ID")
    print("2. Buscar por nombre")
    print("-" * 50)

    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        id_cliente = input("🔍 Ingresa el ID del cliente a buscar: ").strip()
        if not id_cliente:
            mostrar_error("Debes ingresar un ID para buscar.")
            return

        cliente = restaurante.buscar_cliente_por_id(id_cliente)
        if cliente:
            print(f"\n✅ Cliente encontrado:")
            print(cliente.mostrar_informacion())
        else:
            print(f"\n❌ No se encontró ningún cliente con ID '{id_cliente}'.")

    elif opcion == "2":
        nombre = input("🔍 Ingresa el nombre del cliente a buscar: ").strip()
        if not nombre:
            mostrar_error("Debes ingresar un nombre para buscar.")
            return

        clientes = restaurante.buscar_cliente_por_nombre(nombre)
        if clientes:
            print(f"\n✅ Se encontraron {len(clientes)} cliente(s):")
            for i, cliente in enumerate(clientes, 1):
                print(f"\n{i}. {cliente}")
                print(cliente.mostrar_informacion())
        else:
            print(f"\n❌ No se encontraron clientes con nombre que contenga '{nombre}'.")
    else:
        mostrar_error("Opción no válida.")


# ======================== FUNCIÓN PRINCIPAL ========================

def main():
    """
    Función principal que ejecuta el bucle del menú interactivo.

    Concepto educativo:
    Este es el punto de entrada del programa (punto de arranque).
    Aquí se:
    1. Crea una instancia del servicio Restaurante
    2. Muestra el menú en bucle
    3. Procesa la selección del usuario
    4. Llama a los métodos del servicio Restaurante
    """

    # Crear instancia del servicio
    restaurante = Restaurante("El Buen Comer")

    # Variables para datos de ejemplo (didácticos)
    ejemplos_cargados = False

    while True:
        limpiar_pantalla()
        mostrar_encabezado()

        # Opcionalmente cargar ejemplos si es la primera iteración
        if not ejemplos_cargados:
            print("💡 SUGERENCIA: ¿Deseas cargar datos de ejemplo para ver cómo funciona?")
            cargar_ej = input("Ingresa 'S' para cargar ejemplos o cualquier otra tecla para empezar vacío: ").strip().upper()

            if cargar_ej == "S":
                try:
                    # Cargar productos de ejemplo
                    restaurante.registrar_producto("Ceviche", "Entrada", 12.50, True)
                    restaurante.registrar_producto("Lomo a la Parrilla", "Plato Principal", 22.00, True)
                    restaurante.registrar_producto("Ojo de Bife", "Plato Principal", 25.50, True)
                    restaurante.registrar_producto("Coca Cola", "Bebida", 3.50, True)
                    restaurante.registrar_producto("Agua Natural", "Bebida", 1.50, True)
                    restaurante.registrar_producto("Helado de Fresa", "Postre", 5.00, True)

                    # Cargar clientes de ejemplo
                    restaurante.registrar_cliente("Juan Pérez", "juan@email.com", "C001", "+34 123 456 789")
                    restaurante.registrar_cliente("María García", "maria@email.com", "C002", "+34 987 654 321")
                    restaurante.registrar_cliente("Carlos López", "carlos@email.com", "C003")

                    print("\n✅ Datos de ejemplo cargados exitosamente.")
                    print(restaurante.obtener_resumen())
                except ValueError as e:
                    print(f"⚠️  {e}")

            ejemplos_cargados = True
            pausar()
            continue

        mostrar_menu()
        print(restaurante.obtener_resumen())

        opcion = input("\n➜ Selecciona una opción (0-7): ").strip()

        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            listar_productos(restaurante)
        elif opcion == "3":
            buscar_producto(restaurante)
        elif opcion == "4":
            registrar_cliente(restaurante)
        elif opcion == "5":
            listar_clientes(restaurante)
        elif opcion == "6":
            buscar_cliente(restaurante)
        elif opcion == "7":
            limpiar_pantalla()
            print("\n" + "=" * 50)
            print("RESUMEN DEL RESTAURANTE")
            print("=" * 50)
            print(restaurante.obtener_resumen())
            print("\n📊 DETALLES:")
            print(f"   Productos registrados: {len(restaurante.productos)}")
            print(f"   Clientes registrados: {len(restaurante.clientes)}")
        elif opcion == "0":
            limpiar_pantalla()
            print("\n" + "=" * 50)
            print("✨ ¡Gracias por usar el Sistema de Restaurante!")
            print("=" * 50)
            print("\n📚 Conceptos educativos aplicados:")
            print("   ✓ Constructores (__init__)")
            print("   ✓ Decoradores (@property y @setter)")
            print("   ✓ Decoradores (@dataclass)")
            print("   ✓ Validaciones en setters")
            print("   ✓ Arquitectura modular por capas")
            print("   ✓ Menú interactivo desde consola")
            print("   ✓ Transformación input → Objeto → Servicio")
            print("\n💡 Próximas mejoras sugeridas:")
            print("   - Agregar persistencia en archivos/base de datos")
            print("   - Implementar más validaciones")
            print("   - Crear reportes detallados")
            print("   - Agregar sistema de pedidos")
            print("\n¡Hasta pronto!\n")
            break
        else:
            mostrar_error("Opción no válida. Por favor, selecciona una opción del menú.")

        pausar()


if __name__ == "__main__":
    """
    Punto de entrada del programa.
    
    En Python, __name__ == "__main__" se ejecuta solo cuando se corre directamente
    el archivo (no cuando se importa como módulo).
    """
    main()

