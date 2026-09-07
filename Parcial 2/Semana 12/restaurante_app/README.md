# Semana 11 - Restaurante con ventas y persistencia JSON

Estudiante: William Changoluisa

## Descripción
Este proyecto evoluciona la aplicación de restaurante desarrollada en semanas anteriores para incorporar la relación entre usuarios y productos mediante ventas, validación del stock y persistencia completa de productos, usuarios y ventas en archivos JSON.

La lógica de negocio se mantiene separada de la capa de acceso a archivos. La aplicación conserva sus funcionalidades previas y añade la operación principal de la semana: vender un producto validando usuario, producto, cantidad y stock disponible.

## Estructura

restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── __init__.py
├── main.py
└── README.md

## Operación principal
La venta se procesa solo si:

- el usuario existe,
- el producto existe,
- la cantidad es mayor que cero,
- el stock es suficiente.

Cuando la venta es válida, se crea un objeto `Venta`, se guarda en la colección de ventas y se descuenta la cantidad del producto asociado.

## Persistencia JSON
Los archivos JSON se guardan con `json.dump()` y se leen con `json.load()`. El sistema reconstruye objetos `Producto`, `Usuario` y `Venta` cada vez que se inicia la aplicación.

## Ejecución
```bash
python restaurante_app/main.py
```

---

# Semana 12 - Mejoras de rendimiento con índices en memoria

## Descripción de las mejoras
Se conservaron las colecciones principales (listas) de productos, usuarios y ventas para almacenamiento y persistencia JSON. Se añadieron índices en memoria para optimizar búsquedas frecuentes:

- _producto_por_codigo: dict[codigo -> Producto] para búsquedas de producto por código (O(1)).
- _usuario_por_id: dict[id -> Usuario] para búsquedas de usuario por identificación (O(1)).
- _ventas_por_usuario: dict[id -> list[Venta]] para consultar rápidamente las ventas asociadas a un usuario sin recorrer toda la lista de ventas.

Los índices se reconstruyen al iniciar el programa a partir de los JSON y se mantienen sincronizados al registrar, eliminar o actualizar datos relevantes (registro de producto/usuario, venta, eliminación).

## Pruebas principales realizadas
- Búsqueda de producto por código (rápida usando dict).
- Búsqueda de usuario por identificación (rápida usando dict).
- Consulta de ventas de un usuario (usa _ventas_por_usuario, evita recorrer todas las ventas).
- Registro de venta: actualiza stock y mantiene coherencia en índices.
- Reinicio: los índices se reconstruyen correctamente desde los archivos JSON.
