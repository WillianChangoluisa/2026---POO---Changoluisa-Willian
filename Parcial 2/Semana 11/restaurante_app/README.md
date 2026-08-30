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
