# Sistema de Gestión de Restaurante

## 📋 Descripción General

Este proyecto implementa un sistema básico de gestión de restaurante utilizando **Programación Orientada a Objetos (POO)** en Python. El sistema demuestra la aplicación de conceptos fundamentales como identificadores descriptivos, tipos de datos básicos, listas, clases, objetos e importaciones dentro de una estructura modular.

El proyecto está organizado en módulos independientes que representan diferentes aspectos de un restaurante: productos disponibles, clientes registrados y la gestión centralizada del establecimiento.

---

## 🏗️ Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py              # Inicializador del módulo modelos
│   ├── producto.py              # Clase Producto
│   └── cliente.py               # Clase Cliente
├── servicios/
│   ├── __init__.py              # Inicializador del módulo servicios
│   └── restaurante.py           # Clase Restaurante
├── main.py                      # Punto de entrada del programa
└── README.md                    # Este archivo
```

---

## 📚 Clases Implementadas

### 1. **Clase Producto** (`modelos/producto.py`)

Representa un producto disponible en el restaurante (plato o bebida).

#### Atributos:
- `nombre_producto: str` - Nombre del producto
- `descripcion: str` - Descripción detallada del producto
- `precio: float` - Precio unitario del producto
- `cantidad_disponible: int` - Cantidad en stock
- `es_bebida: bool` - Indica si es una bebida (True) o plato (False)

#### Métodos:
- `obtener_tipo_producto() -> str` - Retorna el tipo de producto
- `actualizar_cantidad(cantidad_vendida: int) -> None` - Reduce el stock al vender
- `__str__() -> str` - Representación en texto del producto

---

### 2. **Clase Cliente** (`modelos/cliente.py`)

Representa una persona registrada en el sistema del restaurante.

#### Atributos:
- `nombre_cliente: str` - Nombre completo del cliente
- `correo_electronico: str` - Correo electrónico del cliente
- `numero_telefono: str` - Número de teléfono del cliente
- `es_cliente_frecuente: bool` - Indica si es cliente frecuente

#### Métodos:
- `obtener_estado_cliente() -> str` - Retorna el estado (Regular o Frecuente)
- `actualizar_estado_frecuente(estado_nuevo: bool) -> None` - Actualiza el estado
- `__str__() -> str` - Representación en texto del cliente

---

### 3. **Clase Restaurante** (`servicios/restaurante.py`)

Administra la gestión centralizada de productos y clientes del restaurante.

#### Atributos:
- `nombre_restaurante: str` - Nombre del restaurante
- `ubicacion: str` - Ubicación del restaurante
- `lista_productos: list[Producto]` - Lista de productos disponibles
- `lista_clientes: list[Cliente]` - Lista de clientes registrados

#### Métodos:
- `agregar_producto(producto: Producto) -> None` - Agrega un producto al catálogo
- `agregar_cliente(cliente: Cliente) -> None` - Registra un nuevo cliente
- `mostrar_todos_productos() -> None` - Muestra todos los productos
- `mostrar_todos_clientes() -> None` - Muestra todos los clientes
- `obtener_cantidad_productos() -> int` - Retorna cantidad de productos
- `obtener_cantidad_clientes() -> int` - Retorna cantidad de clientes
- `__str__() -> str` - Representación en texto del restaurante

---

## 🚀 Cómo Ejecutar el Programa

### Requisitos Previos
- Python 3.8 o superior instalado

### Pasos para Ejecutar

1. Navega a la carpeta del proyecto:
```bash
cd restaurante_app
```

2. Ejecuta el programa principal:
```bash
python main.py
```

3. El programa mostrará:
   - Información del restaurante
   - Catálogo de productos disponibles
   - Base de datos de clientes registrados
   - Demostraciones de funcionalidades (ventas, cambio de estado de clientes)

---

## ✨ Características Principales

### Tipos de Datos Utilizados
- ✅ `str` - Nombres, descripciones, correos, teléfonos
- ✅ `int` - Cantidades, números de teléfono (como string)
- ✅ `float` - Precios de productos
- ✅ `bool` - Estado de cliente frecuente, tipo de producto (plato/bebida)
- ✅ `list` - Listas de productos y clientes

### Convenciones de Nombres
- ✅ **PascalCase** para nombres de clases: `Producto`, `Cliente`, `Restaurante`
- ✅ **snake_case** para variables, atributos y métodos: `nombre_producto`, `agregar_cliente()`, `lista_productos`

### Características OOP
- ✅ Constructores `__init__()` en todas las clases
- ✅ Método especial `__str__()` para representación en texto
- ✅ Anotaciones de tipo en atributos
- ✅ Métodos con responsabilidades claras
- ✅ Encapsulación de datos en clases
- ✅ Importaciones correctas entre módulos

---

## 📝 Ejemplo de Uso

```python
# Crear un restaurante
mi_restaurante = Restaurante("El Sabor Tradicional", "Calle Principal 123")

# Crear productos
ceviche = Producto(
    nombre_producto="Ceviche de Camarones",
    descripcion="Camarones frescos marinados en limón",
    precio=18.50,
    cantidad_disponible=25,
    es_bebida=False
)

# Crear clientes
cliente1 = Cliente(
    nombre_cliente="Juan García López",
    correo_electronico="juan.garcia@email.com",
    numero_telefono="987-654-3210",
    es_cliente_frecuente=False
)

# Agregar al restaurante
mi_restaurante.agregar_producto(ceviche)
mi_restaurante.agregar_cliente(cliente1)

# Mostrar información
mi_restaurante.mostrar_todos_productos()
mi_restaurante.mostrar_todos_clientes()

# Realizar venta
ceviche.actualizar_cantidad(5)

# Promover cliente
cliente1.actualizar_estado_frecuente(True)
```

---

## 📊 Datos de Ejemplo

El programa `main.py` incluye ejemplos predefinidos:

### Productos (4 ejemplos):
1. Ceviche de Camarones - $18.50 (Plato)
2. Lomo Saltado - $22.00 (Plato)
3. Chicha Morada - $4.50 (Bebida)
4. Jugo de Naranja Fresco - $5.00 (Bebida)

### Clientes (4 ejemplos):
1. Juan García López - Regular
2. María Rodríguez Pérez - Frecuente
3. Carlos Hernández Flores - Regular
4. Ana Martínez Sánchez - Frecuente

---

## 🎯 Requisitos Cumplidos

✅ Estructura modular con carpetas y archivos organizados  
✅ Implementación de dos clases en `modelos/`  
✅ Implementación de una clase en `servicios/`  
✅ Constructores `__init__()` en todas las clases principales  
✅ Identificadores descriptivos en clases, métodos y variables  
✅ Convenciones de nombres: PascalCase y snake_case  
✅ Tipos de datos básicos: `str`, `int`, `float`, `bool`  
✅ Uso de listas como tipo compuesto  
✅ Anotaciones de tipo en atributos  
✅ Métodos para gestionar información  
✅ Método especial `__str__()` en las clases  
✅ Importaciones correctas entre módulos  
✅ Al menos 4 objetos de cada modelo  
✅ Información organizada en consola  
✅ Comentarios y docstrings explicativos  

---

## 👨‍💻 Notas de Desarrollo

- El proyecto no utiliza interfaces gráficas ni menús interactivos
- No se han utilizado frameworks adicionales más allá de la biblioteca estándar de Python
- Todos los nombres son descriptivos y evitan genéricos como `x`, `dato` o `clase1`
- El código demuestra comprensión clara de los conceptos OOP solicitados

---

## 📄 Licencia

Este proyecto es para fines educativos como parte de un curso de Programación Orientada a Objetos.

---

**Autor:** Willian Changoluisa  
**Curso:** POO - 2026  
**Fecha de Creación:** 2026
