# Archivo principal: punto de entrada del sistema de gestión de restaurante

import sys
sys.path.append('.')

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():
    """Función principal que demuestra el funcionamiento del sistema de restaurante."""
    
    # Crear instancia del restaurante
    restaurante_central = Restaurante("El Sabor Tradicional", "Calle Principal 123")
    
    print(f"\n{'='*60}")
    print("SISTEMA DE GESTIÓN DE RESTAURANTE")
    print(f"{'='*60}\n")
    print(restaurante_central)
    print()
    
    # ========== CREAR PRODUCTOS ==========
    # Producto 1: Plato principal
    plato_ceviche = Producto(
        nombre_producto="Ceviche de Camarones",
        descripcion="Camarones frescos marinados en limón con vegetales",
        precio=18.50,
        cantidad_disponible=25,
        es_bebida=False
    )
    
    # Producto 2: Plato principal
    plato_lomo = Producto(
        nombre_producto="Lomo Saltado",
        descripcion="Carne de res salteada con papas y cebolla",
        precio=22.00,
        cantidad_disponible=20,
        es_bebida=False
    )
    
    # Producto 3: Bebida
    bebida_chicha = Producto(
        nombre_producto="Chicha Morada",
        descripcion="Bebida tradicional hecha de maíz morado",
        precio=4.50,
        cantidad_disponible=50,
        es_bebida=True
    )
    
    # Producto 4: Bebida
    bebida_jugo = Producto(
        nombre_producto="Jugo de Naranja Fresco",
        descripcion="Jugo recién exprimido de naranja",
        precio=5.00,
        cantidad_disponible=40,
        es_bebida=True
    )
    
    # Agregar productos al restaurante
    restaurante_central.agregar_producto(plato_ceviche)
    restaurante_central.agregar_producto(plato_lomo)
    restaurante_central.agregar_producto(bebida_chicha)
    restaurante_central.agregar_producto(bebida_jugo)
    
    # ========== CREAR CLIENTES ==========
    # Cliente 1: Regular
    cliente_juan = Cliente(
        nombre_cliente="Juan García López",
        correo_electronico="juan.garcia@email.com",
        numero_telefono="987-654-3210",
        es_cliente_frecuente=False
    )
    
    # Cliente 2: Frecuente
    cliente_maria = Cliente(
        nombre_cliente="María Rodríguez Pérez",
        correo_electronico="maria.rodriguez@email.com",
        numero_telefono="985-123-4567",
        es_cliente_frecuente=True
    )
    
    # Cliente 3: Regular
    cliente_carlos = Cliente(
        nombre_cliente="Carlos Hernández Flores",
        correo_electronico="carlos.hernandez@email.com",
        numero_telefono="980-111-2222",
        es_cliente_frecuente=False
    )
    
    # Cliente 4: Frecuente
    cliente_ana = Cliente(
        nombre_cliente="Ana Martínez Sánchez",
        correo_electronico="ana.martinez@email.com",
        numero_telefono="975-999-8888",
        es_cliente_frecuente=True
    )
    
    # Agregar clientes al restaurante
    restaurante_central.agregar_cliente(cliente_juan)
    restaurante_central.agregar_cliente(cliente_maria)
    restaurante_central.agregar_cliente(cliente_carlos)
    restaurante_central.agregar_cliente(cliente_ana)
    
    # ========== MOSTRAR INFORMACIÓN REGISTRADA ==========
    # Mostrar todos los productos
    restaurante_central.mostrar_todos_productos()
    
    # Mostrar todos los clientes
    restaurante_central.mostrar_todos_clientes()
    
    # ========== DEMOSTRACIÓN DE MÉTODOS ==========
    print(f"\n{'='*60}")
    print("DEMOSTRACIONES DE FUNCIONALIDADES")
    print(f"{'='*60}\n")
    
    # Demostración: Actualizar cantidad de productos
    print("1. Realizando venta de productos:")
    print(f"   - Vendiendo 5 unidades de '{plato_ceviche.nombre_producto}'")
    plato_ceviche.actualizar_cantidad(5)
    print(f"     Stock actualizado: {plato_ceviche.cantidad_disponible} unidades\n")
    
    print(f"   - Vendiendo 3 unidades de '{bebida_chicha.nombre_producto}'")
    bebida_chicha.actualizar_cantidad(3)
    print(f"     Stock actualizado: {bebida_chicha.cantidad_disponible} unidades\n")
    
    # Demostración: Promover cliente regular a frecuente
    print(f"2. Promoviendo cliente regular a frecuente:")
    cliente_juan.actualizar_estado_frecuente(True)
    print(f"   Nuevo estado: {cliente_juan.obtener_estado_cliente()}\n")
    
    # Resumen final
    print(f"\n{'='*60}")
    print("RESUMEN FINAL DEL RESTAURANTE")
    print(f"{'='*60}\n")
    print(restaurante_central)
    print()


if __name__ == "__main__":
    main()
