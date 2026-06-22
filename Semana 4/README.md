Willian Paul Changoluisa Chicaiza

Sistema básico de gestión de restaurante (POO - Python)

Descripción
-----------
Proyecto sencillo que modela un restaurante con productos (platos/bebidas) y clientes.
Permite registrar productos y clientes, crear pedidos y mostrar la información en consola.

Estructura del proyecto
-----------------------
restaurante_app/
├── modelos/
│   ├── producto.py    # Clase Producto
│   └── cliente.py     # Clase Cliente
├── servicios/
│   └── restaurante.py # Clase Restaurante que administra el sistema
└── main.py            # Punto de entrada: crea objetos y demuestra el uso

Reflexión
---------
La modularización (separar modelos, servicios y punto de entrada) facilita el mantenimiento,
la reutilización y las pruebas. Cada módulo tiene responsabilidades claras: los modelos
representan datos, los servicios gestionan la lógica y main.py orquesta la ejecución.

Instrucciones
------------
Ejecutar desde la raíz del repositorio:
    python restaurante_app\main.py

(El archivo README incluye el nombre del estudiante solicitado.)
