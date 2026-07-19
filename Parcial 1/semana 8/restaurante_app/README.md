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

## Funcionalidades Implementadas

### Operaciones CRUD Completas
- ✅ **Create (Crear)**: Registrar productos, bebidas y clientes
- ✅ **Read (Leer)**: Listar y buscar productos y clientes
- ✅ **Update (Actualizar)**: Modificar datos de productos, bebidas y clientes
- ✅ **Delete (Eliminar)**: Eliminar productos y clientes

### Menú Interactivo Completo (11 Opciones)
1. Registrar producto
2. Registrar bebida
3. Actualizar producto
4. Actualizar bebida
5. Eliminar producto
6. Listar productos
7. Registrar cliente
8. Actualizar cliente
9. Eliminar cliente
10. Listar clientes
11. Salir

### Validaciones
- Códigos de producto únicos
- Identificaciones de cliente únicas
- Precios positivos
- Correos válidos (contienen @)
- Tamaños de bebida validados (pequeño, mediano, grande)
- Confirmación antes de eliminar

## Principios SOLID Aplicados

- **S (Single Responsibility)**: Cada clase tiene una única responsabilidad
- **O (Open/Closed)**: Bebida extiende Producto sin modificar su lógica
- **L (Liskov Substitution)**: Bebida se comporta como Producto sin problemas

## Entrega

- Repositorio público con la estructura solicitada
- Archivo `README.md` que explique las responsabilidades y la relación Producto/Bebida, y los principios SOLID aplicados
- Código completamente funcional con CRUD completo

---

**Autor**: Willian Paul Changoluisa Chicaiza  
**Asignatura**: Programación Orientada a Objetos  
**Semana**: 8  
**Fecha**: 19/07/2026  
**Repositorio**: https://github.com/WillianChangoluisa/2026---POO---Changoluisa-Willian

