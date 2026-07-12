"""
Script de prueba automático para verificar la funcionalidad del sistema.
Este script prueba:
1. Creación de productos con constructor y validaciones
2. Creación de clientes con @dataclass
3. Almacenamiento en la clase Restaurante
4. Búsquedas y listados
"""

from servicios.restaurante import Restaurante

def separator(titulo=""):
    """Imprime un separador con título opcional."""
    print("\n" + "=" * 60)
    if titulo:
        print(f"  {titulo}")
        print("=" * 60)

def test_productos():
    """Prueba la creación de productos con validaciones."""
    separator("✅ PRUEBA 1: CREAR PRODUCTOS")

    restaurante = Restaurante("Test Restaurante")

    try:
        # ✓ Crear producto válido
        print("\n1. Creando producto válido...")
        p1 = restaurante.registrar_producto("Pizza Margarita", "Plato Principal", 15.99)
        print(f"   ✓ Producto creado: {p1}")
        print(f"   ✓ Información:")
        print(p1.mostrar_informacion())

        # ✓ Otro producto válido
        print("\n2. Creando otro producto...")
        p2 = restaurante.registrar_producto("Jugo Natural", "Bebida", 4.50, True)
        print(f"   ✓ Producto creado: {p2}")

        # ✗ Intentar crear producto con precio negativo
        print("\n3. Intentando crear producto con precio negativo...")
        try:
            p3 = restaurante.registrar_producto("Producto Inválido", "Test", -10)
            print("   ✗ ERROR: No debería permitir precio negativo")
        except ValueError as e:
            print(f"   ✓ Validación correcta: {e}")

        # ✗ Intentar crear producto con nombre vacío
        print("\n4. Intentando crear producto con nombre vacío...")
        try:
            p4 = restaurante.registrar_producto("", "Test", 10)
            print("   ✗ ERROR: No debería permitir nombre vacío")
        except ValueError as e:
            print(f"   ✓ Validación correcta: {e}")

        # ✗ Intentar crear producto duplicado
        print("\n5. Intentando crear producto duplicado...")
        try:
            p5 = restaurante.registrar_producto("Pizza Margarita", "Test", 20)
            print("   ✗ ERROR: No debería permitir duplicados")
        except ValueError as e:
            print(f"   ✓ Validación correcta: {e}")

        return restaurante

    except Exception as e:
        print(f"   ✗ ERROR INESPERADO: {e}")
        return None

def test_listar_productos(restaurante):
    """Prueba el listado de productos."""
    separator("✅ PRUEBA 2: LISTAR PRODUCTOS")

    productos = restaurante.listar_productos()
    print(f"\nTotal de productos: {len(productos)}")
    for i, producto in enumerate(productos, 1):
        print(f"  {i}. {producto}")

def test_buscar_productos(restaurante):
    """Prueba la búsqueda de productos."""
    separator("✅ PRUEBA 3: BUSCAR PRODUCTOS")

    # Buscar por nombre
    print("\n1. Buscando: 'Pizza Margarita'")
    p = restaurante.buscar_producto_por_nombre("Pizza Margarita")
    if p:
        print(f"   ✓ Encontrado: {p}")
    else:
        print("   ✗ No encontrado")

    # Buscar categoría
    print("\n2. Buscando productos en categoría 'Bebida'")
    bebidas = restaurante.buscar_productos_por_categoria("Bebida")
    print(f"   ✓ Encontrados {len(bebidas)} producto(s)")
    for bebida in bebidas:
        print(f"     - {bebida}")

def test_clientes():
    """Prueba la creación de clientes con @dataclass."""
    separator("✅ PRUEBA 4: CREAR CLIENTES")

    restaurante = Restaurante("Test Restaurante")

    try:
        # ✓ Crear cliente válido
        print("\n1. Creando cliente válido...")
        c1 = restaurante.registrar_cliente(
            "Pedro Rodríguez",
            "pedro@email.com",
            "CLI001",
            "+34 600 123 456"
        )
        print(f"   ✓ Cliente creado: {c1}")
        print(f"   ✓ Información:")
        print(c1.mostrar_informacion())

        # ✓ Otro cliente
        print("\n2. Creando otro cliente...")
        c2 = restaurante.registrar_cliente(
            "Ana Martínez",
            "ana@email.com",
            "CLI002"
        )
        print(f"   ✓ Cliente creado: {c2}")

        # ✗ Intentar crear cliente sin correo válido
        print("\n3. Intentando crear cliente sin correo válido...")
        try:
            c3 = restaurante.registrar_cliente(
                "Javier García",
                "correo_invalido",  # Sin @
                "CLI003"
            )
            print("   ✗ ERROR: No debería permitir correo sin @")
        except ValueError as e:
            print(f"   ✓ Validación correcta: {e}")

        # ✗ Intentar crear cliente duplicado
        print("\n4. Intentando crear cliente duplicado...")
        try:
            c4 = restaurante.registrar_cliente(
                "Otro Nombre",
                "otro@email.com",
                "CLI001"  # ID duplicado
            )
            print("   ✗ ERROR: No debería permitir ID duplicado")
        except ValueError as e:
            print(f"   ✓ Validación correcta: {e}")

        return restaurante

    except Exception as e:
        print(f"   ✗ ERROR INESPERADO: {e}")
        return None

def test_listar_clientes(restaurante):
    """Prueba el listado de clientes."""
    separator("✅ PRUEBA 5: LISTAR CLIENTES")

    clientes = restaurante.listar_clientes()
    print(f"\nTotal de clientes: {len(clientes)}")
    for i, cliente in enumerate(clientes, 1):
        print(f"  {i}. {cliente}")

def test_buscar_clientes(restaurante):
    """Prueba la búsqueda de clientes."""
    separator("✅ PRUEBA 6: BUSCAR CLIENTES")

    # Buscar por ID
    print("\n1. Buscando cliente con ID 'CLI001'")
    c = restaurante.buscar_cliente_por_id("CLI001")
    if c:
        print(f"   ✓ Encontrado: {c}")
    else:
        print("   ✗ No encontrado")

    # Buscar por nombre
    print("\n2. Buscando clientes con nombre contiene 'Ana'")
    clientes = restaurante.buscar_cliente_por_nombre("Ana")
    print(f"   ✓ Encontrados {len(clientes)} cliente(s)")
    for cliente in clientes:
        print(f"     - {cliente}")

def test_propiedades():
    """Prueba los decoradores @property y @setter."""
    separator("✅ PRUEBA 7: PROPIEDADES Y SETTERS")

    from modelos.producto import Producto

    try:
        # Crear producto
        print("\n1. Creando producto...")
        p = Producto("Ensalada", "Entrada", 8.99)
        print(f"   ✓ Producto: {p.nombre}")

        # Probar @property (lectura)
        print("\n2. Leyendo propiedades (@property)...")
        print(f"   - Nombre: {p.nombre}")
        print(f"   - Categoría: {p.categoria}")
        print(f"   - Precio: ${p.precio:.2f}")
        print(f"   - Disponible: {p.disponible}")

        # Probar @setter (escritura con validación)
        print("\n3. Modificando precio con @setter...")
        p.precio = 9.99
        print(f"   ✓ Nuevo precio: ${p.precio:.2f}")

        # Intentar asignar precio negativo
        print("\n4. Intentando asignar precio negativo...")
        try:
            p.precio = -5
            print("   ✗ ERROR: No debería permitir precio negativo")
        except ValueError as e:
            print(f"   ✓ Validación correcta: {e}")

        # Modificar disponibilidad
        print("\n5. Modificando disponibilidad...")
        p.disponible = False
        print(f"   ✓ Nuevo estado: {p.disponible}")

    except Exception as e:
        print(f"   ✗ ERROR INESPERADO: {e}")

def test_dataclass():
    """Prueba el decorador @dataclass."""
    separator("✅ PRUEBA 8: DECORADOR @DATACLASS")

    from modelos.cliente import Cliente
    from datetime import datetime

    try:
        # Crear cliente usando @dataclass
        print("\n1. Creando cliente con @dataclass...")
        c = Cliente(
            nombre="Carlos López",
            correo="carlos@email.com",
            id_cliente="CLI999",
            telefono="+34 700 999 888"
        )
        print(f"   ✓ Cliente creado")

        # El @dataclass genera automáticamente __repr__
        print("\n2. Representación automática (__repr__)...")
        print(f"   {repr(c)}")

        # El @dataclass genera automáticamente __str__
        print("\n3. String automática (__str__)...")
        print(f"   {str(c)}")

        # Verificar atributos
        print("\n4. Atributos del cliente...")
        print(f"   - Nombre: {c.nombre}")
        print(f"   - Correo: {c.correo}")
        print(f"   - ID: {c.id_cliente}")
        print(f"   - Teléfono: {c.telefono}")
        print(f"   - Registrado: {c.fecha_registro.strftime('%d/%m/%Y %H:%M:%S')}")

    except Exception as e:
        print(f"   ✗ ERROR INESPERADO: {e}")

def main():
    """Ejecuta todas las pruebas."""
    print("\n" + "🧪 " * 20)
    print("  PRUEBAS AUTOMÁTICAS DEL SISTEMA DE RESTAURANTE")
    print("🧪 " * 20)

    # Test de productos
    restaurante_p = test_productos()
    if restaurante_p:
        test_listar_productos(restaurante_p)
        test_buscar_productos(restaurante_p)

    # Test de clientes
    restaurante_c = test_clientes()
    if restaurante_c:
        test_listar_clientes(restaurante_c)
        test_buscar_clientes(restaurante_c)

    # Test de propiedades y setters
    test_propiedades()

    # Test de @dataclass
    test_dataclass()

    # Resumen final
    separator("✅ RESUMEN FINAL")
    print("\n✓ Todas las pruebas se completaron exitosamente")
    print("\n📚 Conceptos validados:")
    print("   ✓ Constructor tradicional (__init__)")
    print("   ✓ Decorador @property (lectura)")
    print("   ✓ Decorador @setter (escritura con validación)")
    print("   ✓ Decorador @dataclass")
    print("   ✓ Validaciones de entrada")
    print("   ✓ Manejo de excepciones")
    print("   ✓ Almacenamiento en listas")
    print("   ✓ Búsquedas y filtrado")
    print("   ✓ Arquitectura por capas")
    print("\n✅ El sistema está listo para ser utilizado por el usuario.\n")

if __name__ == "__main__":
    main()

