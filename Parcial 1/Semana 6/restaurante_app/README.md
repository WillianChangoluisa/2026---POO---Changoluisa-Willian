# README.md

# Sistema de Gestión de Restaurante - Programación Orientada a Objetos

## Estudiante
Willian Changoluisa

## Descripción del Sistema

El sistema **restaurante_app** es una aplicación en Python que implementa principios fundamentales de Programación Orientada a Objetos (POO). Simula la gestión de productos de un restaurante, permitiendo administrar platillos y bebidas con atributos diferenciados.

La aplicación demuestra cómo aplicar **herencia, encapsulación y polimorfismo** en un contexto real, permitiendo que cada tipo de producto (platillo o bebida) tenga comportamientos y atributos específicos mientras comparte características comunes.

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py          # Inicializador del paquete modelos
│   ├── producto.py          # Clase padre Producto
│   ├── platillo.py          # Clase hija Platillo
│   └── bebida.py            # Clase hija Bebida
├── servicios/
│   ├── __init__.py          # Inicializador del paquete servicios
│   └── restaurante.py       # Clase de servicio Restaurante
└── main.py                  # Punto de entrada de la aplicación
```

## Explicación de la Estructura del Proyecto

### Carpeta `modelos/`
Contiene las clases de dominio que representan los conceptos principales del sistema:

- **producto.py**: Define la clase padre `Producto` con atributos comunes a todos los productos.
- **platillo.py**: Define la clase `Platillo` que hereda de `Producto`.
- **bebida.py**: Define la clase `Bebida` que hereda de `Producto`.

### Carpeta `servicios/`
Contiene la lógica de negocio y servicios del sistema:

- **restaurante.py**: Define la clase `Restaurante` que administra la colección de productos.

### Archivo `main.py`
Punto de entrada de la aplicación. Demuestra:
- Creación de instancias de Platillo y Bebida
- Agregación de productos al restaurante
- Uso de métodos y validaciones
- Polimorfismo en acción

## Relación de Herencia

El sistema implementa la siguiente jerarquía de herencia:

```
    Producto (Clase Padre)
    /        \
Platillo    Bebida
(Clase Hija) (Clase Hija)
```

### Relaciones:

- **Producto**: Clase padre que define atributos y métodos comunes:
  - Atributos: `__nombre`, `__precio`, `__disponibilidad`
  - Métodos: `obtener_precio()`, `cambiar_precio()`, `mostrar_informacion()`

- **Platillo**: Hereda de Producto y agrega:
  - Atributos propios: `__tipo_platillo`, `__calorias`
  - Sobrescribe `mostrar_informacion()` para mostrar información específica

- **Bebida**: Hereda de Producto y agrega:
  - Atributos propios: `__volumen_ml`, `__tipo_bebida`
  - Sobrescribe `mostrar_informacion()` para mostrar información específica

## Atributo Encapsulado

El atributo **`__precio`** implementa encapsulación total:

- Es **privado** (prefijo doble guion `__`)
- Se accede mediante el getter: `obtener_precio()`
- Se modifica mediante el setter: `cambiar_precio(nuevo_precio)`
- **Validación**: El precio no puede ser negativo ni cero
- Si se intenta asignar un valor inválido, se lanza una excepción `ValueError`

Ejemplo:
```python
platillo = Platillo("Lomo Saltado", 25.50, "Plato Principal", 650)
print(platillo.obtener_precio())  # Acceso controlado

platillo.cambiar_precio(28.00)    # Validación y asignación segura
# platillo.cambiar_precio(-5.00) # Genera error
```

## Polimorfismo Demostrado

El polimorfismo se evidencia mediante la **sobrescritura del método `mostrar_informacion()`** en las clases hijas:

### En la clase Producto:
```python
def mostrar_informacion(self):
    # Muestra información básica
    print(f"Producto: {self.__nombre}")
    print(f"Precio: ${self.__precio:.2f}")
```

### En la clase Platillo:
```python
def mostrar_informacion(self):
    # Muestra información específica de platillo
    print(f"PLATILLO: {self.obtener_nombre()}")
    print(f"Tipo: {self.__tipo_platillo}")
    print(f"Calorías: {self.__calorias} kcal")
```

### En la clase Bebida:
```python
def mostrar_informacion(self):
    # Muestra información específica de bebida
    print(f"BEBIDA: {self.obtener_nombre()}")
    print(f"Tipo: {self.__tipo_bebida}")
    print(f"Volumen: {self.__volumen_ml} ml")
```

### En el servicio Restaurante:
```python
def mostrar_productos(self):
    for producto in self.__productos:
        # Polimorfismo: cada objeto ejecuta su propia versión
        producto.mostrar_informacion()
```

Cuando se ejecuta `mostrar_productos()`, se itera sobre la lista de productos y se llama a `mostrar_informacion()`. Cada objeto muestra su información de forma específica según su tipo, demostrando así el polimorfismo.

## Importancia de POO en Proyectos Python Modulares

### Mantenibilidad
La estructura modular facilita encontrar y modificar código. Cada clase tiene una responsabilidad clara.

### Reutilización
La herencia permite que `Platillo` y `Bebida` reutilicen el código de `Producto` sin duplicación.

### Extensibilidad
Agregar nuevos tipos de productos (como "Postre" o "Entrada Especial") es simple: solo se hereda de `Producto`.

### Seguridad
La encapsulación protege los datos internos (como `__precio`). Los datos se modifican de forma controlada y validada.

### Claridad
El código es autodocumentado. Los nombres de clases, métodos y variables explican su propósito claramente.

### Escalabilidad
A medida que el sistema crece, la POO proporciona una base sólida y predecible para agregar funcionalidades.

## Cómo Ejecutar el Programa

1. Navega a la carpeta `restaurante_app`:
   ```bash
   cd restaurante_app
   ```

2. Ejecuta el archivo `main.py`:
   ```bash
   python main.py
   ```

3. El programa creará objetos, los agregará al restaurante y mostrará su información en consola.

## Características Implementadas

✅ Estructura modular con carpetas `modelos` y `servicios`  
✅ Clase padre `Producto` con atributos comunes  
✅ Clases hijas `Platillo` y `Bebida` que heredan de `Producto`  
✅ Uso de `super()` para llamar al constructor de la clase padre  
✅ Encapsulación con atributo privado `__precio`  
✅ Getters y setters (`obtener_precio()`, `cambiar_precio()`)  
✅ Validación de datos (precio > 0)  
✅ Sobrescritura de métodos (`mostrar_informacion()`)  
✅ Polimorfismo en acción (diferentes comportamientos según el tipo)  
✅ Clase de servicio `Restaurante` que administra productos  
✅ Mínimo 2 objetos de `Platillo` y 2 de `Bebida`  
✅ Ejecución desde `main.py`  
✅ Comentarios explicativos en partes clave del código  

## Conclusión

Este proyecto demuestra cómo los principios de Programación Orientada a Objetos (herencia, encapsulación y polimorfismo) se aplican de forma práctica en Python, resultando en código modular, mantenible y extensible.
