# Actividad Semana 8 — restaurante_app

Actividad de la Semana 8: mejorar el proyecto `restaurante_app` aplicando los principios SOLID (S, O y L) manteniendo la estructura modular modelos/ — servicios/ — main.py.

Estructura requerida:

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
```

Descripción breve:
- `Producto` (modelo): clase base con `codigo`, `nombre`, `categoria`, `precio` y método `mostrar_informacion()`.
- `Bebida` (modelo): hereda de `Producto`, añade atributos específicos (tamaño, tipo de envase) y sobrescribe `mostrar_informacion()`.
- `Cliente` (modelo): representa un cliente, implementado con `@dataclass` y método `mostrar_informacion()`.
- `Restaurante` (servicio): administra colecciones de productos (incluye bebidas) y clientes; contiene validaciones para evitar duplicados y métodos para registrar/listar/buscar.
- `main.py`: punto de entrada con menú interactivo que usa solo `input()` y llama a los métodos del servicio.

Requisitos mínimos:
- Usar una única lista `productos` que pueda contener `Producto` y `Bebida`.
- No hacer condicionales que distingan Producto/Bebida durante el listado; usar polimorfismo (`mostrar_informacion()`).
- Validar códigos de productos y identificaciones de clientes para evitar duplicados.
- Mantener responsabilidades separadas: modelos <-> servicios <-> main.
- Usar anotaciones de tipos en constructores y métodos.

Ejecución:

Desde PowerShell, situarse en la carpeta `restaurante_app` y ejecutar:

```powershell
cd "C:\Users\William.Changoluisa\PycharmProjects\2026---POO---Changoluisa-Willian\Parcial 1\semana 8\restaurante_app"
python main.py
```

Entrega:
- Repositorio público con la estructura solicitada.
- Archivo `README.md` que explique las responsabilidades y la relación Producto/Bebida, y los principios SOLID aplicados.

Autor: Estudiante — Semana 8
Fecha: 2026

