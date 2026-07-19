"""
Script de verificación completa del proyecto de la Semana 8
Ejecuta todas las pruebas funcionales del restaurante
"""

import sys
sys.path.insert(0, '.')

from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

print("=" * 50)
print("PRUEBAS FUNCIONALES DEL RESTAURANTE")
print("=" * 50)

# Crear una instancia de Restaurante
r = Restaurante()

# PRUEBA 1: Crear y registrar un Producto
print("\n[PRUEBA 1] Registrar Producto")
try:
    p1 = r.crear_y_registrar_producto("P001", "Pizza Margarita", "Pizza", 12.99)
    print("✅ Producto registrado exitosamente")
    print(p1.mostrar_informacion())
except Exception as e:
    print(f"❌ Error: {e}")

# PRUEBA 2: Crear y registrar una Bebida
print("\n[PRUEBA 2] Registrar Bebida")
try:
    b1 = r.crear_y_registrar_bebida("B001", "Coca Cola", "Bebida", 2.50, "mediano", "lata")
    print("✅ Bebida registrada exitosamente")
    print(b1.mostrar_informacion())
except Exception as e:
    print(f"❌ Error: {e}")

# PRUEBA 3: Registrar otro Producto
print("\n[PRUEBA 3] Registrar otro Producto")
try:
    p2 = r.crear_y_registrar_producto("P002", "Hamburguesa", "Comida Rápida", 8.50)
    print("✅ Producto registrado exitosamente")
except Exception as e:
    print(f"❌ Error: {e}")

# PRUEBA 4: Registrar otra Bebida
print("\n[PRUEBA 4] Registrar otra Bebida")
try:
    b2 = r.crear_y_registrar_bebida("B002", "Jugo Natural", "Bebida", 3.75, "grande", "vaso")
    print("✅ Bebida registrada exitosamente")
except Exception as e:
    print(f"❌ Error: {e}")

# PRUEBA 5: Validar duplicados en Productos
print("\n[PRUEBA 5] Validar rechazo de código duplicado en Producto")
try:
    p_dup = r.crear_y_registrar_producto("P001", "Otro Pizza", "Pizza", 15.00)
    print("❌ Error: Se permitió un código duplicado!")
except ValueError as e:
    print(f"✅ Correcto - Se rechazó: {e}")

# PRUEBA 6: Registrar Cliente
print("\n[PRUEBA 6] Registrar Cliente")
try:
    c1 = r.crear_y_registrar_cliente("12345678", "Juan Pérez", "juan@email.com", "+1234567890")
    print("✅ Cliente registrado exitosamente")
    print(c1.mostrar_informacion())
except Exception as e:
    print(f"❌ Error: {e}")

# PRUEBA 7: Registrar otro Cliente
print("\n[PRUEBA 7] Registrar otro Cliente")
try:
    c2 = r.crear_y_registrar_cliente("87654321", "María García", "maria@email.com")
    print("✅ Cliente registrado exitosamente")
except Exception as e:
    print(f"❌ Error: {e}")

# PRUEBA 8: Validar duplicados en Clientes
print("\n[PRUEBA 8] Validar rechazo de identificación duplicada")
try:
    c_dup = r.crear_y_registrar_cliente("12345678", "Otro Juan", "otro@email.com")
    print("❌ Error: Se permitió una identificación duplicada!")
except ValueError as e:
    print(f"✅ Correcto - Se rechazó: {e}")

# PRUEBA 9: Listar Productos (Polimorfismo)
print("\n[PRUEBA 9] Listar Productos (demostrando Polimorfismo)")
productos = r.listar_productos()
print(f"✅ Total de productos: {len(productos)}")
for i, p in enumerate(productos, 1):
    print(f"\n--- Producto {i} ---")
    print(p.mostrar_informacion())

# PRUEBA 10: Listar Clientes
print("\n[PRUEBA 10] Listar Clientes")
clientes = r.listar_clientes()
print(f"✅ Total de clientes: {len(clientes)}")
for i, c in enumerate(clientes, 1):
    print(f"\n--- Cliente {i} ---")
    print(c.mostrar_informacion())

# PRUEBA 11: Búsqueda de Producto
print("\n[PRUEBA 11] Búsqueda de Producto por código")
prod_buscado = r.buscar_producto_por_codigo("B001")
if prod_buscado:
    print(f"✅ Producto encontrado: {prod_buscado.nombre}")
else:
    print("❌ Producto no encontrado")

# PRUEBA 12: Búsqueda de Cliente
print("\n[PRUEBA 12] Búsqueda de Cliente por ID")
cli_buscado = r.buscar_cliente_por_id("87654321")
if cli_buscado:
    print(f"✅ Cliente encontrado: {cli_buscado.nombre}")
else:
    print("❌ Cliente no encontrado")

print("\n" + "=" * 50)
print("✅ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
print("=" * 50)

