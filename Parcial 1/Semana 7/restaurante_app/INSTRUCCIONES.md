# 🚀 GUÍA RÁPIDA DE INICIO

## ¿Cómo ejecutar el programa?

### Opción 1: Desde la terminal (Recomendado)

1. **Abre PowerShell o CMD**
2. **Navega a la carpeta del proyecto:**
   ```powershell
   cd "C:\Users\William.Changoluisa\PycharmProjects\2026---POO---Changoluisa-Willian\Parcial 1\Semana 7\restaurante_app"
   ```

3. **Ejecuta el programa:**
   ```powershell
   python main.py
   ```

### Opción 2: Desde PyCharm (IDE)

1. Abre PyCharm
2. Navega a: `Parcial 1 → Semana 7 → restaurante_app → main.py`
3. Haz clic derecho en `main.py`
4. Selecciona **"Run 'main'"**

---

## 📖 Estructura del Menú Interactivo

Al ejecutar el programa, verás este menú:

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
7. Ver resumen del restaurante
0. Salir
```

---

## 💡 Ejemplos de Uso

### Ejemplo 1: Registrar un Producto

```
➜ Selecciona una opción (0-7): 1

==================================================
REGISTRAR NUEVO PRODUCTO
==================================================
📝 Nombre del producto: Sopa de Cebolla
🏷️  Categoría (ej: Entrada, Plato Principal, Bebida): Entrada
💰 Precio en $ (debe ser > 0): 7.50
✅ ¿Disponible ahora? (S/N, por defecto S): S

✅ Producto 'Sopa de Cebolla' registrado correctamente.
```

### Ejemplo 2: Listar Productos

```
➜ Selecciona una opción (0-7): 2

==================================================
LISTA DE PRODUCTOS
==================================================

📦 Total de productos: 3

1. Sopa de Cebolla (Entrada) - $7.50
2. Ceviche (Entrada) - $12.50
3. Jugo Natural (Bebida) - $4.50
```

### Ejemplo 3: Buscar Producto

```
➜ Selecciona una opción (0-7): 3

==================================================
BUSCAR PRODUCTO
==================================================
🔍 Ingresa el nombre del producto a buscar: Ceviche

✅ Producto encontrado:
┌─────────────────────────────────────┐
│ Producto: Ceviche                      │
│ Categoría: Entrada                     │
│ Precio: $ 12.50                       │
│ Estado: ✓ Disponible                  │
└─────────────────────────────────────┘
```

### Ejemplo 4: Registrar Cliente

```
➜ Selecciona una opción (0-7): 4

==================================================
REGISTRAR NUEVO CLIENTE
==================================================
👤 Nombre completo del cliente: Juan Pérez
📧 Correo electrónico: juan.perez@email.com
🔑 ID único del cliente (ej: C001): C001
📞 Teléfono (opcional): +34 600 123 456

✅ Cliente 'Juan Pérez' registrado correctamente.
```

### Ejemplo 5: Listar Clientes

```
➜ Selecciona una opción (0-7): 5

==================================================
LISTA DE CLIENTES
==================================================

👥 Total de clientes: 3

1. Juan Pérez (C001) - juan.perez@email.com
2. María García (C002) - maria@email.com
3. Carlos López (C003) - carlos@email.com
```

### Ejemplo 6: Buscar Cliente

```
➜ Selecciona una opción (0-7): 6

==================================================
BUSCAR CLIENTE
==================================================
1. Buscar por ID
2. Buscar por nombre
----------------------------------------
Selecciona una opción: 1

🔍 Ingresa el ID del cliente a buscar: C001

✅ Cliente encontrado:
┌─────────────────────────────────────┐
│ Nombre: Juan Pérez                    │
│ ID Cliente: C001                      │
│ Correo: juan.perez@email.com          │
│ Teléfono: +34 600 123 456            │
│ Registrado: 11/07/2026 - 23:55:30    │
└─────────────────────────────────────┘
```

---

## 🎯 Conceptos Educativos Implementados

### 1. Constructor Tradicional (`__init__`)
```python
# En modelos/producto.py
def __init__(self, nombre, categoria, precio, disponible=True):
    self._nombre = None
    self.nombre = nombre  # Usa el setter
```

**¿Por qué?** Permite crear objetos de forma controlada y validada.

---

### 2. Decorador @property
```python
# Lectura de atributo de forma controlada
@property
def nombre(self):
    return self._nombre
```

**Uso:**
```python
print(producto.nombre)  # Acceso como si fuera público
```

---

### 3. Decorador @setter
```python
# Escritura con validación automática
@nombre.setter
def nombre(self, valor):
    if not valor or not isinstance(valor, str):
        raise ValueError("El nombre debe ser un texto válido")
    self._nombre = valor.strip()
```

**Uso:**
```python
producto.nombre = "Nuevo Nombre"  # Validación automática
```

---

### 4. Decorador @dataclass
```python
# Simplifica la definición de clases de datos
from dataclasses import dataclass

@dataclass
class Cliente:
    nombre: str
    correo: str
    id_cliente: str
    telefono: str = "No proporcionado"
```

**Ventajas:**
- ✓ Genera automáticamente `__init__()`
- ✓ Genera automáticamente `__repr__()`
- ✓ Genera automáticamente `__eq__()`
- ✓ Menos código boilerplate

---

### 5. Arquitectura Modular por Capas

```
        ENTRADA (Consola)
               ↓
       main.py (Presentación)
               ↓
   Restaurante.py (Negocio)
               ↓
   Producto.py / Cliente.py (Datos)
```

**Ventajas:**
- ✓ Código organizado
- ✓ Fácil de mantener
- ✓ Fácil de extender
- ✓ Bajo acoplamiento

---

## ✅ Validaciones Implementadas

### Validaciones de Producto:
- ✓ Nombre no puede estar vacío
- ✓ Categoría no puede estar vacía
- ✓ Precio debe ser mayor que cero
- ✓ Precio debe ser un número válido
- ✓ No se pueden registrar productos duplicados

### Validaciones de Cliente:
- ✓ Nombre no puede estar vacío
- ✓ Correo debe tener formato válido (debe contener '@')
- ✓ ID del cliente no puede estar vacío
- ✓ No se pueden registrar clientes con ID duplicado

---

## 🧪 Ejecutar Pruebas Automáticas

Si deseas verificar que todo funciona correctamente, puedes ejecutar el script de pruebas:

```powershell
cd "C:\Users\William.Changoluisa\PycharmProjects\2026---POO---Changoluisa-Willian\Parcial 1\Semana 7\restaurante_app"
python test_sistema.py
```

Este script probará:
- ✓ Creación de productos
- ✓ Validaciones de entrada
- ✓ Listados
- ✓ Búsquedas
- ✓ Propiedades y setters
- ✓ Decoradores @dataclass

---

## 📁 Archivos Incluidos

```
restaurante_app/
├── modelos/                  # Capa de Datos
│   ├── __init__.py
│   ├── producto.py           # Clase Producto
│   └── cliente.py            # Clase Cliente
├── servicios/                # Capa de Negocio
│   ├── __init__.py
│   └── restaurante.py        # Clase Restaurante
├── main.py                   # Punto de entrada
├── test_sistema.py           # Script de pruebas
└── README.md                 # Documentación completa
```

---

## 💬 Preguntas Frecuentes

**P: ¿Cómo modifico un producto ya registrado?**
R: Por ahora, el sistema solo permite registrar, listar y buscar. Para modificar, deberías desarrollar un nuevo menú con option que edite atributos usando los setters.

**P: ¿Cómo guardo los datos permanentemente?**
R: El sistema actualmente guarda datos en listas (memoria). Para persistencia, puedes agregar:
- Guardar en archivo JSON
- Usar una base de datos (SQLite)

**P: ¿Puedo cambiar los datos de ejemplo?**
R: Sí, en `main.py` hay una función que carga ejemplos. Puedes modificarla.

**P: ¿Qué pasa si ingreso un precio con letra?**
R: El sistema validará y mostrará: "Error al registrar producto: El precio debe ser un número válido"

---

## 🎓 Próximos Pasos de Aprendizaje

1. **Persistencia:** Agregar guardado/carga en JSON
2. **Sistema de Pedidos:** Crear clase Pedido
3. **Reportes:** Generar reportes de ventas
4. **Base de Datos:** Usar SQLite para almacenamiento
5. **Interfaz Gráfica:** Crear GUI con tkinter o PyQt

---

## 📚 Recursos Útiles

- **Documentación @dataclass:** https://docs.python.org/es/3/library/dataclasses.html
- **Decoradores en Python:** https://docs.python.org/es/3/glossary.html#term-decorator
- **POO en Python:** https://docs.python.org/es/3/tutorial/classes.html

---

## ✨ Comentarios Finales

Este sistema es **completamente funcional** y demuestra los conceptos fundamentales de la Programación Orientada a Objetos. Todos los requisitos solicitados han sido implementados:

✅ Constructores  
✅ Decoradores @property y @setter  
✅ Decorador @dataclass  
✅ Validaciones  
✅ Arquitectura modular  
✅ Menú interactivo  
✅ Entrada de usuario  
✅ Gestión de objetos  

¡Ahora el código es tuyo para estudiar y extender! 🚀

---

**¡Éxito con tu aprendizaje de POO!** 🎓

