# Semana 11 - Restaurante con ventas y persistencia JSON

Estudiante: William Changoluisa

## Descripción
Este proyecto evoluciona la aplicación de restaurante desarrollada en semanas anteriores para incorporar la relación entre usuarios y productos mediante ventas, validación del stock y persistencia completa de productos, usuarios y ventas en archivos JSON.

La lógica de negocio se mantiene separada de la capa de acceso a archivos. La aplicación conserva sus funcionalidades previas y añade la operación principal de la semana: vender un producto validando usuario, producto, cantidad y stock disponible.

## Estructura del proyecto

Parcial 2/
└── Semana 11/
    ├── README.md
    └── restaurante_app/
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
        └── main.py

## Componentes

### modelos/producto.py
Representa cada producto del restaurante. Incluye el atributo `stock`, validaciones para el código, nombre, categoría, precio y cantidad disponible. Además, ofrece los métodos `to_dict()` y `from_dict()` para persistencia JSON.

### modelos/usuario.py
Define la entidad `Usuario` con validaciones para identificación, nombre, correo, cédula y celular. También permite serializar y reconstruir los datos desde JSON.

### modelos/venta.py
Representa la relación entre un usuario y un producto vendido. Conserva el identificador del usuario, el código del producto y la cantidad vendida.

### servicios/archivo_servicio.py
Centraliza la lectura y escritura de `productos.json`, `usuarios.json` y `ventas.json` con `json.load()`, `json.dump()`, `with open(..., encoding="utf-8")` y manejo específico de errores.

### servicios/restaurante.py
Administra las colecciones internas de productos, usuarios y ventas. Aquí se aplican las reglas del negocio: validación de existencia, validación del stock, creación de la venta y actualización del stock del producto.

### main.py
Coordina el menú interactivo. Solicita datos con `input()` y llama a los métodos del servicio sin manipular directamente las colecciones internas desde la consola.

## Operación de venta
La venta se realiza a través del método `vender_producto(codigo_producto, identificacion_usuario, cantidad)`.

1. Se comprueba que el usuario exista.
2. Se confirma que el producto exista.
3. Se valida que la cantidad sea mayor que cero.
4. Se verifica que el stock sea suficiente.
5. Se crea una instancia de `Venta`.
6. Se agrega a la colección de ventas.
7. Se disminuye el stock del producto.
8. Se guardan tanto `ventas.json` como `productos.json`.

La consulta `consultar_ventas_por_usuario(identificacion_usuario)` recorre la colección de ventas y devuelve únicamente las relacionadas con ese usuario.

## Persistencia
Las tres colecciones se conservan en archivos JSON:

- `datos/productos.json`: productos y su stock actualizado.
- `datos/usuarios.json`: usuarios registrados.
- `datos/ventas.json`: relaciones entre usuarios y productos vendidos.

Al iniciar la aplicación, las colecciones se reconstruyen desde los archivos JSON con `json.load()` y los métodos `from_dict()` de cada modelo.

## Excepciones controladas
Se manejan errores específicos para evitar fallos inesperados:

- `FileNotFoundError`: si algún archivo aún no existe, se inicializa con una colección vacía.
- `json.JSONDecodeError`: si el contenido del JSON es inválido.
- `PermissionError`: si no hay permisos de lectura o escritura.
- `KeyError`: cuando un registro no contiene las claves esperadas.
- `ValueError`: para validaciones propias de `Producto`, `Usuario` y `Venta`.

## Ejecución
Desde la carpeta `Parcial 2/Semana 11`, ejecute:

```bash
python restaurante_app/main.py
```

## Pruebas realizadas
Se validó el flujo principal del sistema verificando:

1. Registro de producto con stock.
2. Registro de usuario.
3. Venta válida con stock suficiente.
4. Descuento automático del stock del producto.
5. Registro de la venta en `ventas.json`.
6. Rechazo de una venta con cantidad mayor al stock disponible.
7. Cierre del programa y reinicio para comprobar la recuperación de datos desde JSON.

Esto confirma que la aplicación conserva la información entre ejecuciones y que la lógica de ventas responde correctamente a las reglas de negocio.
