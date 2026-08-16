Proyecto: restaurante_app - Semana 9
=================================

Estudiante: William Changoluisa

Breve descripción:
Este proyecto es una evolución del trabajo de semanas anteriores. Implementa
un sistema básico para administrar productos y usuarios de un restaurante,
utilizando estructuras de datos de Python (list, tuple, dict, set) de manera
funcional dentro del servicio.

Estructura del proyecto:

restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
├── main.py
└── README.md

Responsabilidad de los componentes:
- `modelos/producto.py`: Clase Producto (codigo, nombre, categoria, precio).
- `modelos/usuario.py`: Clase Usuario (identificacion, nombre, correo).
- `servicios/restaurante.py`: Clase Restaurante que administra las colecciones
  internas y expone métodos para registrar, buscar, actualizar, eliminar y
  listar productos, además de registrar y listar usuarios.
- `main.py`: Interfaz por consola; presenta el menú, solicita datos y llama al
  servicio para realizar las operaciones.

Estructuras de datos utilizadas y propósito:
- list: Se usan listas (`self._productos`, `self._usuarios`) para almacenar
  las colecciones dinámicas de objetos (registro, listado, CRUD).
- tuple: La tupla `OPCIONES` en `Restaurante` contiene las opciones del menú
  y se mantiene inmutable durante la ejecución.
- dict: En `main.py` se utiliza un diccionario para mapear números de opción
  del menú a funciones manejadoras (relación clave → valor funcional).
- set: El método `obtener_categorias_unicas` devuelve un conjunto con las
  categorías únicas de los productos (elimina duplicados automáticamente).

Ejecución:
1) Abra una terminal en la carpeta raíz del proyecto (donde se encuentra `main.py`).
2) Ejecute:

```bash
python -m restaurante_app.main
```

Instrucciones de uso:
- Seleccione la opción del menú por número.
- Para registrar productos y clientes, ingrese los datos solicitados.
- El sistema evita códigos de productos repetidos y identificaciones de
  clientes duplicadas.

Persistencia opcional:
El proyecto incluye una carpeta `data/` en el nivel de `Semana 9` con los
archivos `productos.json` y `clientes.json`. El servicio `Restaurante` carga
estos archivos al iniciar y guarda automáticamente los cambios (registro,
actualización y eliminación de productos; registro de clientes). Esto facilita
seguir trabajando en memoria pero con una opción sencilla de persistencia.

Reflexión:
Seleccionar la estructura de datos adecuada mejora la claridad y rendimiento
del código: las listas permiten colecciones dinámicas y ordenadas, las tuplas
aseguran valores constantes, los diccionarios facilitan mapeos rápidos y los
conjuntos eliminan duplicados de forma eficiente.

