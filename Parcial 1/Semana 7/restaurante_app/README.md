# 🍽️ Sistema de Gestión de Restaurante - Programación Orientada a Objetos

## 📋 Descripción del Proyecto

Este proyecto implementa un **Sistema de Gestión de Restaurante** que demuestra los conceptos fundamentales de la **Programación Orientada a Objetos (POO)** en Python, incluyendo:

- ✅ **Constructores** - Inicialización de objetos con `__init__`
- ✅ **Decoradores @property y @setter** - Control de acceso y validación de atributos
- ✅ **Decorador @dataclass** - Simplificación de clases de datos
- ✅ **Arquitectura modular por capas** - Organización profesional del código
- ✅ **Menú interactivo** - Interfaz de consola amigable
- ✅ **Transformación de datos** - Entrada de usuario → Objeto → Almacenamiento

---

## 📁 Estructura del Proyecto

```
restaurante_app/
├── modelos/                      # Capa de Datos
│   ├── __init__.py              # Inicialización del módulo modelos
│   ├── producto.py              # Clase Producto (constructor + properties)
│   └── cliente.py               # Clase Cliente (decorador @dataclass)
│
├── servicios/                    # Capa de Negocio (Lógica)
│   ├── __init__.py              # Inicialización del módulo servicios
│   └── restaurante.py           # Clase Restaurante (administrador)
│
├── main.py                       # Capa de Presentación (Menú interactivo)
└── README.md                     # Este archivo
```

---

## 🎯 Concepto Educativo: Arquitectura por Capas

La aplicación está organizada en **3 capas**:

### 1️⃣ **Capa de Datos (modelos/)**
- Contiene las clases que representan las entidades del negocio
- `Producto.py` - Define la estructura de un producto del restaurante
- `Cliente.py` - Define la estructura de un cliente registrado

### 2️⃣ **Capa de Negocio (servicios/)**
- Contiene la lógica de operación y administración
- `Restaurante.py` - Administra productos y clientes
- Realiza validaciones y búsquedas

### 3️⃣ **Capa de Presentación (main.py)**
- Interfaz con el usuario
- Captura entrada del usuario mediante `input()`
- Presenta menú interactivo
- No contiene lógica de negocio

**Flujo de Datos:**
```
Entrada del Usuario
        ↓
main.py (input())
        ↓
Restaurante (servicio)
        ↓
Constructor de Producto/Cliente
        ↓
Objeto creado y almacenado
        ↓
Salida al usuario
```

---

## 🏛️ Clases Principales

### 📦 Clase `Producto`

**Ubicación:** `modelos/producto.py`

**Características:**

```python
# Constructor tradicional
def __init__(self, nombre, categoria, precio, disponible=True):
    pass

# Decoradores @property para lectura
@property
def nombre(self):
    return self._nombre

# Decoradores @setter para escritura controlada
@nombre.setter
def nombre(self, valor):
    # Validaciones automáticas
    pass
```

**Atributos:**
- `nombre` (str) - Nombre del producto
- `categoria` (str) - Categoría del producto
- `precio` (float) - Precio unitario (validación: > 0)
- `disponible` (bool) - Estado de disponibilidad

**Validaciones Implementadas:**
- ✓ El nombre no puede estar vacío
- ✓ La categoría no puede estar vacía
- ✓ El precio debe ser mayor que cero
- ✓ El precio debe ser un número válido

**Método Especial:**
```python
producto.mostrar_informacion()  # Retorna información formateada
```

---

### 👥 Clase `Cliente`

**Ubicación:** `modelos/cliente.py`

**Características - Decorador @dataclass:**

```python
@dataclass
class Cliente:
    nombre: str
    correo: str
    id_cliente: str
    telefono: str = "No proporcionado"
    fecha_registro: datetime = field(default_factory=datetime.now)
```

**Ventajas del @dataclass:**
- ✓ Genera automáticamente `__init__()`, `__repr__()`, `__eq__()`
- ✓ Código más limpio y legible
- ✓ Menos código boilerplate

**Método Especial:**
```python
cliente.mostrar_informacion()  # Retorna información formateada
```

---

### 🏪 Clase `Restaurante`

**Ubicación:** `servicios/restaurante.py`

**Responsabilidades:**
1. Mantener listas de productos y clientes
2. Crear objetos a partir de datos ingresados
3. Validar información antes de almacenar
4. Proporcionar métodos para buscar información

**Métodos Principales:**

#### Para Productos:
```python
# Registrar un producto
producto = restaurante.registrar_producto(
    nombre="Ceviche",
    categoria="Entrada",
    precio=12.50,
    disponible=True
)

# Listar todos
productos = restaurante.listar_productos()

# Buscar por nombre
producto = restaurante.buscar_producto_por_nombre("Ceviche")

# Buscar por categoría
entradas = restaurante.buscar_productos_por_categoria("Entrada")
```

#### Para Clientes:
```python
# Registrar un cliente
cliente = restaurante.registrar_cliente(
    nombre="Juan Pérez",
    correo="juan@email.com",
    id_cliente="C001",
    telefono="+34 123 456 789"
)

# Listar todos
clientes = restaurante.listar_clientes()

# Buscar por ID
cliente = restaurante.buscar_cliente_por_id("C001")

# Buscar por nombre
clientes = restaurante.buscar_cliente_por_nombre("Juan")
```

---

## 🚀 Cómo Ejecutar el Programa

### Paso 1: Navegar a la carpeta del proyecto
```powershell
cd "C:\Users\William.Changoluisa\PycharmProjects\2026---POO---Changoluisa-Willian\Parcial 1\Semana 7\restaurante_app"
```

### Paso 2: Ejecutar el programa
```powershell
python main.py
```

### Paso 3: Seleccionar opciones del menú
```
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Listar productos
3. Buscar producto
----------------------------------------
4. Registrar cliente
5. Listar clientes
6. Buscar cliente
----------------------------------------
7. Ver resumen
0. Salir
```

---

## 📖 Ejemplo de Uso Paso a Paso

### Flujo Completo: Registrar un Producto

1. **Entrada del Usuario (main.py)**
   ```
   El usuario selecciona opción 1: "Registrar producto"
   ```

2. **Captura de Datos (main.py → input())**
   ```
   Nombre: Lomo a la Parrilla
   Categoría: Plato Principal
   Precio: 22.00
   Disponible: S
   ```

3. **Creación del Objeto (Restaurante → Producto)**
   ```python
   # El constructor de Producto se invoca:
   producto = Producto("Lomo a la Parrilla", "Plato Principal", 22.00, True)
   # El setter de precio valida: 22.00 > 0 ✓
   # El setter de nombre valida: no está vacío ✓
   ```

4. **Almacenamiento (Restaurante)**
   ```python
   self.productos.append(producto)
   ```

5. **Salida al Usuario**
   ```
   ✅ Producto 'Lomo a la Parrilla' registrado correctamente.
   
   📊 Información del producto creado:
   ┌─────────────────────────────────────┐
   │ Producto: Lomo a la Parrilla         │
   │ Categoría: Plato Principal           │
   │ Precio: $ 22.00                      │
   │ Estado: ✓ Disponible                 │
   └─────────────────────────────────────┘
   ```

---

## 🔑 Conceptos Clave de POO Aplicados

### 1. ✅ Constructor (`__init__`)
```python
def __init__(self, nombre, categoria, precio, disponible=True):
    """Inicializa un nuevo producto"""
    self._nombre = None  # Atributo privado
    self.nombre = nombre  # Usa el setter para validar
```

**¿Por qué?** Permite crear objetos con datos validados automáticamente.

---

### 2. ✅ Decorador @property
```python
@property
def nombre(self):
    """Getter - Obtener el valor de forma controlada"""
    return self._nombre
```

**¿Por qué?** Permite acceder a los atributos como si fueran públicos, pero manteniendo control.

**Uso:**
```python
print(producto.nombre)  # Lectura
```

---

### 3. ✅ Decorador @setter
```python
@nombre.setter
def nombre(self, valor):
    """Setter - Asignar valor con validación"""
    if not valor or not isinstance(valor, str):
        raise ValueError("El nombre debe ser un texto válido")
    self._nombre = valor.strip()
```

**¿Por qué?** Permite validar datos ANTES de asignarlos.

**Uso:**
```python
producto.nombre = "Nuevo nombre"  # Escritura con validación
```

---

### 4. ✅ Decorador @dataclass
```python
@dataclass
class Cliente:
    nombre: str
    correo: str
    id_cliente: str
    telefono: str = "No proporcionado"
```

**¿Por qué?** Reduce mucho código boilerplate para clases simples de datos.

**Genera automáticamente:**
- `__init__()`
- `__repr__()`
- `__eq__()`
- Validaciones en `__post_init__()`

---

### 5. ✅ Encapsulación
```python
self._nombre = None  # Atributo privado (convención _)
```

**¿Por qué?** Protege los datos internos del objeto.

---

### 6. ✅ Validación
```python
if precio_numerico <= 0:
    raise ValueError("El precio debe ser mayor que cero")
```

**¿Por qué?** Garantiza que solo se creen objetos con datos válidos.

---

## 💡 Datos de Ejemplo

Al ejecutar el programa, se ofrecerá cargar datos de ejemplo:

### Productos de Ejemplo:
| Producto | Categoría | Precio |
|----------|-----------|--------|
| Ceviche | Entrada | $12.50 |
| Lomo a la Parrilla | Plato Principal | $22.00 |
| Ojo de Bife | Plato Principal | $25.50 |
| Coca Cola | Bebida | $3.50 |
| Agua Natural | Bebida | $1.50 |
| Helado de Fresa | Postre | $5.00 |

### Clientes de Ejemplo:
| Nombre | ID | Correo |
|--------|----|----|
| Juan Pérez | C001 | juan@email.com |
| María García | C002 | maria@email.com |
| Carlos López | C003 | carlos@email.com |

---

## ✨ Características Especiales Implementadas

### 🎨 Interfaz Amigable
- Emojis y formatos visuales claros
- Mensajes de error y éxito diferenciados
- Menú estructurado y fácil de navegar

### 📚 Código Didáctico
- Comentarios explicativos en cada sección
- Docstrings detallados en todas las funciones
- Nombres descriptivos para variables y funciones

### 🔍 Búsquedas Avanzadas
- Buscar producto por nombre exacto
- Buscar productos por categoría
- Buscar cliente por ID
- Buscar cliente por nombre (búsqueda parcial)

### ✅ Validaciones Robustas
- Evita duplicados (mismo nombre de producto, mismo ID de cliente)
- Valida tipos de datos
- Valida rangos de valores
- Mensajes de error claros

---

## 🚫 Restricciones Respetadas

✓ No se copió código literal del ejemplo de biblioteca
✓ No hay interfaces gráficas (solo consola)
✓ No hay base de datos externa (solo listas en memoria)
✓ Nombres descriptivos en todo el código
✓ Objetos NO quemados en el código (creados desde input)
✓ Estructura modular respetada
✓ Archivos `__init__.py` en todos los módulos
✓ Se usa `@property`, `@setter` y `@dataclass` según se requería

---

## 📚 Próximas Mejoras Sugeridas

1. **Persistencia de Datos:**
   - Guardar productos y clientes en archivo JSON
   - Cargar datos al iniciar la aplicación

2. **Sistema de Pedidos:**
   - Crear clase Pedido
   - Registrar pedidos de clientes
   - Calcular montos totales

3. **Reportes:**
   - Reporte de productos más vendidos
   - Reporte de clientes frecuentes
   - Ingresos totales

4. **Mejoras de Validación:**
   - Formato de correo más robusto
   - Validación de teléfono
   - Límites de precio

5. **Base de Datos:**
   - Usar SQLite o PostgreSQL
   - Persistencia real de datos

---

## 📝 Notas Importantes

### Importaciones
Las importaciones se manejan correctamente entre capas:
```python
# En main.py
from servicios.restaurante import Restaurante

# En servicios/restaurante.py
from modelos.producto import Producto
from modelos.cliente import Cliente
```

### Punto de Entrada
```python
if __name__ == "__main__":
    main()
```

Esto asegura que `main()` solo se ejecute cuando se corre el archivo directamente.

### Manejo de Errores
Todas las operaciones incluyen manejo de excepciones:
```python
try:
    # Operación
except ValueError as e:
    mostrar_error(str(e))
```

---

## 🎓 Lecciones Aprendidas

Al completar este proyecto, habrás aprendido:

1. **Diferencia entre atributos privados y públicos** - Use `_` para privados
2. **Control de acceso mediante decoradores** - `@property` y `@setter`
3. **Validación de datos en setters** - Garantiza integridad
4. **Uso de @dataclass** - Reduce código boilerplate
5. **Arquitectura por capas** - Separación de responsabilidades
6. **Menú interactivo** - Interfaz de usuario en consola
7. **Transformación input → Objeto** - Flujo de datos en POO
8. **Manejo de excepciones** - Try/except para errores

---

## 📞 Soporte

Si tienes dudas sobre el código:
1. Lee los comentarios en el código fuente
2. Consulta los docstrings de las funciones
3. Ejecuta el programa y explora las opciones
4. Lee este README completo

---

**¡Espero que disfrutes aprendiendo los conceptos de Programación Orientada a Objetos!** 🚀

**Autor:** Sistema Educativo POO - Semana 7  
**Fecha:** 2026  
**Nivel:** Principiante - Intermedio

