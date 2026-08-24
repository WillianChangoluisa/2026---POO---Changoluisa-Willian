# Semana 10 - Persistencia de productos con JSON

Estudiante: William Changoluisa

## Descripción
Este proyecto continúa con la evolución de la aplicación de restaurante, incorporando la persistencia de productos mediante un archivo JSON. La información ya no queda limitada a la memoria temporal del programa, sino que se guarda en el disco para recuperarse al iniciar la aplicación nuevamente.

## Estructura del proyecto

restaurante_app/
├── datos/
│   └── productos.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── __init__.py
├── main.py
└── README.md

## Componentes

### modelos/producto.py
Define la clase Producto y sus validaciones. Además, incluye el método to_dict() para convertir un producto a un diccionario compatible con JSON y from_dict() para reconstruirlo al leer el archivo.

### modelos/usuario.py
Mantiene la entidad Usuario con validaciones para identificación, nombre y correo. En esta semana no se persiste, pero sigue integrado con el sistema.

### servicios/archivo_servicio.py
Responsable de la lectura y escritura de `datos/productos.json`. Usa `with open()` y `encoding="utf-8"`, además controla `FileNotFoundError`, `json.JSONDecodeError` y `PermissionError`.

### servicios/restaurante.py
Administra la colección de productos, sus operaciones básicas y la interacción con el servicio de archivo para guardar la información después de cada modificación.

### main.py
Coordina el menú interactivo, inicializa el sistema, carga los productos al inicio y ejecuta las operaciones del restaurante sin manipular directamente la colección interna.

## Flujo de carga y guardado

1. Al iniciar, `main.py` crea una instancia de `Restaurante`.
2. `Restaurante` llama a `ArchivoServicio.cargar_productos()`.
3. El servicio verifica si el archivo existe.
4. Si existe, usa `json.load()` para leer la información.
5. Cada registro válido se convierte en un objeto `Producto` mediante `Producto.from_dict()`.
6. La colección se trabaja en memoria con objetos.
7. Cuando un producto se registra, actualiza o elimina, `Restaurante` solicita guardar la colección en el archivo con `json.dump()`.

## Manejo de excepciones

Se controlan situaciones específicas para evitar que la aplicación termine abruptamente:

- FileNotFoundError: si el archivo no existe, se crea un archivo vacío y se inicia con la colección vacía.
- json.JSONDecodeError: si el contenido no es JSON válido, se advierte al usuario y se reinicia el archivo con contenido vacío.
- PermissionError: si no hay permisos para leer o escribir, se informa de forma clara.
- KeyError: cuando un registro JSON no tiene todas las claves esperadas, se descarta ese registro y continúa.
- ValueError: se utiliza para las validaciones de Producto y de los datos ingresados por el usuario.

## Instrucciones de ejecución

1. Abrir la terminal en la carpeta `Parcial 2/Semana 10`.
2. Ejecutar:
   python restaurante_app/main.py
3. Desde el menú podrá registrar, buscar, actualizar, eliminar y listar productos.

## Verificación de persistencia

Para comprobar la persistencia real, se realizó la siguiente prueba:

1. Se ejecutó el programa y se registró uno o más productos.
2. Se verificó que `restaurante_app/datos/productos.json` contuviera la información.
3. Se cerró el programa.
4. Se volvió a ejecutar la aplicación y se listó la colección.
5. Los productos anteriores aparecieron correctamente, confirmando que se recuperan desde el archivo JSON.

Esto demuestra que los datos permanecen guardados aunque la sesión del programa termine.
