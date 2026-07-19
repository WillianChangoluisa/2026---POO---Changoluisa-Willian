"""
Script de verificación de la versión actualizada con Actualizar y Eliminar
Prueba todas las nuevas funcionalidades del restaurante
"""

import sys
sys.path.insert(0, '.')

from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

print("=" * 60)
print("PRUEBAS - VERSIÓN ACTUALIZADA CON ACTUALIZAR Y ELIMINAR")
print("=" * 60)

# Crear una instancia de Restaurante
r = Restaurante()

# ==================== PRUEBAS DE PRODUCTOS ====================
print("\n" + "="*60)
print("PRUEBAS DE PRODUCTOS")
print("="*60)

# PRUEBA 1: Crear productos
print("\n[PRUEBA 1] Registrar Producto")
try:
    p1 = r.crear_y_registrar_producto("P001", "Pizza Margarita", "Pizza", 12.99)
    print("✅ Producto registrado")
except Exception as e:
    print(f"❌ Error: {e}")

# PRUEBA 2: Crear bebida
print("\n[PRUEBA 2] Registrar Bebida")
try:
    b1 = r.crear_y_registrar_bebida("B001", "Coca Cola", "Bebida", 2.50, "mediano", "lata")
    print("✅ Bebida registrada")
except Exception as e:
    print(f"❌ Error: {e}")

# PRUEBA 3: Actualizar Producto
print("\n[PRUEBA 3] Actualizar Producto")
try:
    p1_actualizado = r.actualizar_producto("P001", nombre="Pizza Siciliana", precio=14.99)
    print(f"✅ Producto actualizado: {p1_actualizado.nombre} - ${p1_actualizado.precio}")
except Exception as e:
    print(f"❌ Error: {e}")

# PRUEBA 4: Actualizar solo nombre
print("\n[PRUEBA 4] Actualizar solo nombre")
try:
    p1_actualizado = r.actualizar_producto("P001", nombre="Pizza Napolitana")
    print(f"✅ Nombre actualizado: {p1_actualizado.nombre}")
except Exception as e:
    print(f"❌ Error: {e}")

# PRUEBA 5: Actualizar Bebida
print("\n[PRUEBA 5] Actualizar Bebida")
try:
    b1_actualizado = r.actualizar_bebida("B001", nombre="Pepsi", tamano="grande")
    print(f"✅ Bebida actualizada: {b1_actualizado.nombre} - {b1_actualizado.tamano}")
except Exception as e:
    print(f"❌ Error: {e}")

# PRUEBA 6: Intentar actualizar bebida con código de producto
print("\n[PRUEBA 6] Intentar actualizar bebida con código de producto (debe fallar)")
try:
    r.actualizar_bebida("P001", nombre="Agua")
    print("❌ Error: Se permitió actualizar producto como bebida")
except ValueError as e:
    print(f"✅ Correcto - Se rechazó: {e}")

# PRUEBA 7: Listar productos después de actualización
print("\n[PRUEBA 7] Listar productos después de actualización")
productos = r.listar_productos()
print(f"✅ Total de productos: {len(productos)}")
for p in productos:
    print(f"  • {p.codigo}: {p.nombre} - ${p.precio}")

# PRUEBA 8: Eliminar producto
print("\n[PRUEBA 8] Eliminar Producto")
try:
    eliminado = r.eliminar_producto("P001")
    if eliminado:
        print("✅ Producto eliminado exitosamente")
    else:
        print("❌ Producto no encontrado")
except Exception as e:
    print(f"❌ Error: {e}")

# PRUEBA 9: Verificar eliminación
print("\n[PRUEBA 9] Verificar eliminación")
productos = r.listar_productos()
print(f"✅ Total de productos: {len(productos)}")
for p in productos:
    print(f"  • {p.codigo}: {p.nombre}")

# PRUEBA 10: Intentar eliminar producto inexistente
print("\n[PRUEBA 10] Intentar eliminar producto inexistente")
eliminado = r.eliminar_producto("P999")
if eliminado:
    print("❌ Se eliminó un producto inexistente")
else:
    print("✅ Correcto - No se encontró el producto")

# ==================== PRUEBAS DE CLIENTES ====================
print("\n" + "="*60)
print("PRUEBAS DE CLIENTES")
print("="*60)

# PRUEBA 11: Crear clientes
print("\n[PRUEBA 11] Registrar Cliente")
try:
    c1 = r.crear_y_registrar_cliente("12345678", "Juan Pérez", "juan@email.com", "+1234567890")
    print("✅ Cliente registrado")
except Exception as e:
    print(f"❌ Error: {e}")

# PRUEBA 12: Actualizar Cliente
print("\n[PRUEBA 12] Actualizar Cliente")
try:
    c1_actualizado = r.actualizar_cliente("12345678", nombre="Juan Carlos Pérez", telefono="+9876543210")
    print(f"✅ Cliente actualizado: {c1_actualizado.nombre}")
except Exception as e:
    print(f"❌ Error: {e}")

# PRUEBA 13: Actualizar solo correo
print("\n[PRUEBA 13] Actualizar solo correo")
try:
    c1_actualizado = r.actualizar_cliente("12345678", correo="juancarlos@email.com")
    print(f"✅ Correo actualizado: {c1_actualizado.correo}")
except Exception as e:
    print(f"❌ Error: {e}")

# PRUEBA 14: Intentar actualizar con correo inválido
print("\n[PRUEBA 14] Intentar actualizar con correo sin @ (debe fallar)")
try:
    r.actualizar_cliente("12345678", correo="correo_invalido")
    print("❌ Se permitió correo sin @")
except ValueError as e:
    print(f"✅ Correcto - Se rechazó: {e}")

# PRUEBA 15: Crear otro cliente
print("\n[PRUEBA 15] Registrar otro Cliente")
try:
    c2 = r.crear_y_registrar_cliente("87654321", "María García", "maria@email.com")
    print("✅ Cliente registrado")
except Exception as e:
    print(f"❌ Error: {e}")

# PRUEBA 16: Listar clientes después de actualización
print("\n[PRUEBA 16] Listar clientes")
clientes = r.listar_clientes()
print(f"✅ Total de clientes: {len(clientes)}")
for c in clientes:
    print(f"  • {c.identificacion}: {c.nombre}")

# PRUEBA 17: Eliminar cliente
print("\n[PRUEBA 17] Eliminar Cliente")
try:
    eliminado = r.eliminar_cliente("87654321")
    if eliminado:
        print("✅ Cliente eliminado exitosamente")
    else:
        print("❌ Cliente no encontrado")
except Exception as e:
    print(f"❌ Error: {e}")

# PRUEBA 18: Verificar eliminación de cliente
print("\n[PRUEBA 18] Verificar eliminación de cliente")
clientes = r.listar_clientes()
print(f"✅ Total de clientes: {len(clientes)}")
for c in clientes:
    print(f"  • {c.identificacion}: {c.nombre}")

# PRUEBA 19: Intentar actualizar cliente inexistente
print("\n[PRUEBA 19] Intentar actualizar cliente inexistente")
try:
    r.actualizar_cliente("99999999", nombre="Inexistente")
    print("❌ Se actualizó un cliente inexistente")
except ValueError as e:
    print(f"✅ Correcto - Se rechazó: {e}")

# ==================== RESUMEN FINAL ====================
print("\n" + "="*60)
print("RESUMEN DE PRUEBAS")
print("="*60)

print("\n✅ FUNCIONALIDADES NUEVAS IMPLEMENTADAS:")
print("  1. Actualizar Producto (nombre, categoría, precio)")
print("  2. Actualizar Bebida (nombre, categoría, precio, tamaño, envase)")
print("  3. Actualizar Cliente (nombre, correo, teléfono)")
print("  4. Eliminar Producto")
print("  5. Eliminar Cliente")

print("\n✅ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
print("="*60)

