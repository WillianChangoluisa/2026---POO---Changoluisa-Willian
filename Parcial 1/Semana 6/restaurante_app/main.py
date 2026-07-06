# Punto de entrada del sistema: main.py
# Demuestra el uso del sistema de restaurante con POO

from modelos import Producto, Platillo, Bebida
from servicios import Restaurante


def mostrar_separador(caracter="=", cantidad=70):
    """Función auxiliar para mostrar separadores."""
    return caracter * cantidad


def main():
    """
    Función principal que demuestra el funcionamiento del sistema.
    Crea objetos de Platillo y Bebida, los agrega a un Restaurante y muestra su información.
    """
    
    print("\n")
    mostrar_separador()
    print("BIENVENIDO AL SISTEMA DE GESTIÓN DE RESTAURANTE".center(70))
    print("Programación Orientada a Objetos (POO) en Python".center(70))
    mostrar_separador()
    
    # Crear instancia del restaurante
    restaurante = Restaurante("La Buena Mesa")
    
    print(f"\n✓ Restaurante '{restaurante.obtener_nombre()}' creado.\n")
    
    # ========== SECCIÓN 1: CREACIÓN DE PRODUCTOS ==========
    print("\n" + mostrar_separador("-", 70))
    print("SECCIÓN 1: REGISTRANDO PRODUCTOS AL SISTEMA".center(70))
    print(mostrar_separador("-", 70))
    
    # Crear platillos (objetos de tipo Platillo)
    print("\n📍 CREANDO PLATILLOS:\n")
    platillo1 = Platillo(
        nombre="Lomo Saltado",
        precio=25.50,
        tipo_platillo="Plato Principal",
        calorias=650
    )
    print(f"   └─ {platillo1.obtener_nombre()} - ${platillo1.obtener_precio():.2f}")
    
    platillo2 = Platillo(
        nombre="Causa Limeña",
        precio=18.00,
        tipo_platillo="Entrada",
        calorias=280
    )
    print(f"   └─ {platillo2.obtener_nombre()} - ${platillo2.obtener_precio():.2f}")
    
    platillo3 = Platillo(
        nombre="Ají de Gallina",
        precio=22.00,
        tipo_platillo="Plato Principal",
        calorias=520
    )
    print(f"   └─ {platillo3.obtener_nombre()} - ${platillo3.obtener_precio():.2f}")
    
    # Crear bebidas (objetos de tipo Bebida)
    print("\n📍 CREANDO BEBIDAS:\n")
    bebida1 = Bebida(
        nombre="Café Expreso",
        precio=3.50,
        volumen_ml=30,
        tipo_bebida="Caliente"
    )
    print(f"   └─ {bebida1.obtener_nombre()} - ${bebida1.obtener_precio():.2f}")
    
    bebida2 = Bebida(
        nombre="Jugo de Naranja",
        precio=4.75,
        volumen_ml=250,
        tipo_bebida="Fría"
    )
    print(f"   └─ {bebida2.obtener_nombre()} - ${bebida2.obtener_precio():.2f}")
    
    bebida3 = Bebida(
        nombre="Pisco Sour",
        precio=12.00,
        volumen_ml=150,
        tipo_bebida="Alcohólica"
    )
    print(f"   └─ {bebida3.obtener_nombre()} - ${bebida3.obtener_precio():.2f}")
    
    # ========== SECCIÓN 2: AGREGAR PRODUCTOS AL RESTAURANTE ==========
    print("\n" + mostrar_separador("-", 70))
    print("SECCIÓN 2: AGREGANDO PRODUCTOS AL MENÚ".center(70))
    print(mostrar_separador("-", 70))
    print()
    
    restaurante.agregar_producto(platillo1)
    restaurante.agregar_producto(platillo2)
    restaurante.agregar_producto(platillo3)
    restaurante.agregar_producto(bebida1)
    restaurante.agregar_producto(bebida2)
    restaurante.agregar_producto(bebida3)
    
    # ========== SECCIÓN 3: MOSTRAR MENÚ COMPLETO ==========
    print("\n" + mostrar_separador("=", 70))
    print("SECCIÓN 3: MENÚ COMPLETO DEL RESTAURANTE".center(70))
    print(mostrar_separador("=", 70))
    restaurante.mostrar_productos()
    
    # ========== SECCIÓN 4: ACCESO A ATRIBUTOS ENCAPSULADOS ==========
    print("\n" + mostrar_separador("-", 70))
    print("SECCIÓN 4: ACCESO A ATRIBUTOS ENCAPSULADOS (GETTERS)".center(70))
    print(mostrar_separador("-", 70))
    
    print(f"\n📌 INFORMACIÓN DEL PLATILLO: {platillo1.obtener_nombre()}")
    print(f"   ├─ Nombre: {platillo1.obtener_nombre()}")
    print(f"   ├─ Precio: ${platillo1.obtener_precio():.2f}")
    print(f"   ├─ Tipo: {platillo1.obtener_tipo_platillo()}")
    print(f"   ├─ Calorías: {platillo1.obtener_calorias()} kcal")
    print(f"   └─ Disponible: {'Sí' if platillo1.obtener_disponibilidad() else 'No'}")
    
    print(f"\n📌 INFORMACIÓN DE LA BEBIDA: {bebida1.obtener_nombre()}")
    print(f"   ├─ Nombre: {bebida1.obtener_nombre()}")
    print(f"   ├─ Precio: ${bebida1.obtener_precio():.2f}")
    print(f"   ├─ Tipo: {bebida1.obtener_tipo_bebida()}")
    print(f"   ├─ Volumen: {bebida1.obtener_volumen()} ml")
    print(f"   └─ Disponible: {'Sí' if bebida1.obtener_disponibilidad() else 'No'}")
    
    # ========== SECCIÓN 5: ENCAPSULACIÓN Y VALIDACIÓN DE PRECIOS ==========
    print("\n" + mostrar_separador("-", 70))
    print("SECCIÓN 5: ENCAPSULACIÓN Y VALIDACIÓN DE PRECIOS".center(70))
    print(mostrar_separador("-", 70))
    
    print(f"\n🔒 Demostrando encapsulación con el atributo '__precio':")
    print(f"\n   Intento 1: Cambiar precio de '{platillo1.obtener_nombre()}' a $28.00")
    print(f"   Precio actual: ${platillo1.obtener_precio():.2f}")
    
    try:
        platillo1.cambiar_precio(28.00)
        print(f"   ✓ Éxito: Nuevo precio: ${platillo1.obtener_precio():.2f}")
    except ValueError as e:
        print(f"   ✗ Error: {e}")
    
    print(f"\n   Intento 2: Cambiar precio de '{bebida2.obtener_nombre()}' a $5.50")
    print(f"   Precio actual: ${bebida2.obtener_precio():.2f}")
    
    try:
        bebida2.cambiar_precio(5.50)
        print(f"   ✓ Éxito: Nuevo precio: ${bebida2.obtener_precio():.2f}")
    except ValueError as e:
        print(f"   ✗ Error: {e}")
    
    print(f"\n   Intento 3: Intentar asignar precio negativo (-15.00)")
    print(f"   Precio actual: ${platillo2.obtener_precio():.2f}")
    
    try:
        platillo2.cambiar_precio(-15.00)
        print(f"   ✓ Éxito: Nuevo precio: ${platillo2.obtener_precio():.2f}")
    except ValueError as e:
        print(f"   ✗ Error capturado: {e} ← Validación correcta")
    
    print(f"\n   Intento 4: Intentar asignar precio de cero (0.00)")
    print(f"   Precio actual: ${platillo3.obtener_precio():.2f}")
    
    try:
        platillo3.cambiar_precio(0.00)
        print(f"   ✓ Éxito: Nuevo precio: ${platillo3.obtener_precio():.2f}")
    except ValueError as e:
        print(f"   ✗ Error capturado: {e} ← Validación correcta")
    
    # ========== SECCIÓN 6: MODIFICACIÓN DE OTROS ATRIBUTOS ==========
    print("\n" + mostrar_separador("-", 70))
    print("SECCIÓN 6: MODIFICACIÓN DE ATRIBUTOS ESPECÍFICOS".center(70))
    print(mostrar_separador("-", 70))
    
    print(f"\n🔄 Modificando atributos de platillos:")
    print(f"\n   Causa Limeña - Calorías antes: {platillo2.obtener_calorias()} kcal")
    platillo2.cambiar_calorias(300)
    print(f"   Causa Limeña - Calorías después: {platillo2.obtener_calorias()} kcal ✓")
    
    print(f"\n🔄 Modificando atributos de bebidas:")
    print(f"\n   Jugo de Naranja - Volumen antes: {bebida2.obtener_volumen()} ml")
    bebida2.cambiar_volumen(350)
    print(f"   Jugo de Naranja - Volumen después: {bebida2.obtener_volumen()} ml ✓")
    
    # ========== SECCIÓN 7: DISPONIBILIDAD DE PRODUCTOS ==========
    print("\n" + mostrar_separador("-", 70))
    print("SECCIÓN 7: GESTIÓN DE DISPONIBILIDAD".center(70))
    print(mostrar_separador("-", 70))
    
    print(f"\n🔴 Simulando que el Café Expreso se agota:")
    print(f"   Estado antes: {'Disponible' if bebida1.obtener_disponibilidad() else 'No disponible'}")
    bebida1.cambiar_disponibilidad(False)
    print(f"   Estado después: {'Disponible' if bebida1.obtener_disponibilidad() else 'No disponible'} ✓")
    
    print(f"\n🟢 Reabasteciendo el Café Expreso:")
    print(f"   Estado antes: {'Disponible' if bebida1.obtener_disponibilidad() else 'No disponible'}")
    bebida1.cambiar_disponibilidad(True)
    print(f"   Estado después: {'Disponible' if bebida1.obtener_disponibilidad() else 'No disponible'} ✓")
    
    # ========== SECCIÓN 8: POLIMORFISMO EN ACCIÓN ==========
    print("\n" + mostrar_separador("-", 70))
    print("SECCIÓN 8: POLIMORFISMO - LLAMANDO MISMO MÉTODO EN DIFERENTES TIPOS".center(70))
    print(mostrar_separador("-", 70))
    
    print("\n📋 Demostrando polimorfismo al llamar mostrar_informacion():")
    print("   (Cada tipo de producto muestra información diferente)")
    
    productos_demo = [platillo1, bebida1, platillo2, bebida3]
    for i, producto in enumerate(productos_demo, 1):
        print(f"\n   [{i}] Llamando mostrar_informacion() en {tipo_producto(producto)}:")
        print()
        producto.mostrar_informacion()
    
    # ========== SECCIÓN 9: ESTADÍSTICAS FINALES ==========
    print("\n" + mostrar_separador("=", 70))
    print("SECCIÓN 9: ESTADÍSTICAS DEL RESTAURANTE".center(70))
    print(mostrar_separador("=", 70))
    
    total_productos = restaurante.obtener_cantidad_productos()
    productos = restaurante.obtener_productos()
    
    total_precio = sum(p.obtener_precio() for p in productos)
    precio_promedio = total_precio / total_productos if total_productos > 0 else 0
    
    platillos = [p for p in productos if isinstance(p, Platillo)]
    bebidas = [p for p in productos if isinstance(p, Bebida)]
    
    print(f"\n📊 RESUMEN GENERAL:")
    print(f"   ├─ Total de productos en menú: {total_productos}")
    print(f"   ├─ Total de platillos: {len(platillos)}")
    print(f"   ├─ Total de bebidas: {len(bebidas)}")
    print(f"   ├─ Suma total de precios: ${total_precio:.2f}")
    print(f"   └─ Precio promedio: ${precio_promedio:.2f}")
    
    print(f"\n📊 PRODUCTO MÁS CARO:")
    if productos:
        mas_caro = max(productos, key=lambda p: p.obtener_precio())
        print(f"   ├─ Nombre: {mas_caro.obtener_nombre()}")
        print(f"   ├─ Precio: ${mas_caro.obtener_precio():.2f}")
        print(f"   └─ Tipo: {tipo_producto(mas_caro)}")
    
    print(f"\n📊 PRODUCTO MÁS ECONÓMICO:")
    if productos:
        mas_barato = min(productos, key=lambda p: p.obtener_precio())
        print(f"   ├─ Nombre: {mas_barato.obtener_nombre()}")
        print(f"   ├─ Precio: ${mas_barato.obtener_precio():.2f}")
        print(f"   └─ Tipo: {tipo_producto(mas_barato)}")
    
    # ========== SECCIÓN 10: INFORMACIÓN DE CLASES ==========
    print("\n" + mostrar_separador("-", 70))
    print("SECCIÓN 10: INFORMACIÓN SOBRE LA ESTRUCTURA POO".center(70))
    print(mostrar_separador("-", 70))
    
    print(f"\n🏗️  JERARQUÍA DE CLASES:")
    print(f"   Producto (Clase Padre)")
    print(f"   ├─ Platillo (Clase Hija)")
    print(f"   └─ Bebida (Clase Hija)")
    
    print(f"\n🔐 ENCAPSULACIÓN:")
    print(f"   • Atributo privado: __precio")
    print(f"   • Acceso mediante: obtener_precio()")
    print(f"   • Modificación mediante: cambiar_precio(nuevo_precio)")
    print(f"   • Validación: precio > 0")
    
    print(f"\n📌 CLASES Y OBJETOS CREADOS:")
    print(f"   • Platillos creados: {len(platillos)} objetos")
    for platillo in platillos:
        print(f"     └─ {platillo.obtener_nombre()}")
    print(f"   • Bebidas creadas: {len(bebidas)} objetos")
    for bebida in bebidas:
        print(f"     └─ {bebida.obtener_nombre()}")
    
    # Mensaje final
    print("\n" + mostrar_separador("=", 70))
    print("¡EJECUCIÓN DEL PROGRAMA COMPLETADA EXITOSAMENTE!".center(70))
    print(mostrar_separador("=", 70) + "\n")


def tipo_producto(producto):
    """Función auxiliar para obtener el tipo de producto."""
    if isinstance(producto, Platillo):
        return "Platillo"
    elif isinstance(producto, Bebida):
        return "Bebida"
    else:
        return "Producto"


if __name__ == "__main__":
    main()
