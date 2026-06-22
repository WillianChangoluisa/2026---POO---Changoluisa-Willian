# Sistema de Gestion de Restaurante - POO en Python

## Estudiante
**Willian Paul Changoluisa Chicaiza**

## Descripcion del Sistema
Sistema basico de gestion de restaurante que demuestra los principios de Programacion Orientada a Objetos (POO) en Python. El sistema permite registrar productos (platos y bebidas), clientes y crear pedidos, organizado en modulos independientes con responsabilidades claramente definidas.

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py      # Clase Producto
│   └── cliente.py       # Clase Cliente
├── servicios/
│   ├── __init__.py
│   └── restaurante.py   # Clase Restaurante (servicio principal)
└── main.py              # Punto de entrada de la aplicacion
```

## Responsabilidad de cada componente

### modelos/producto.py
- **Clase Producto**: Representa un articulo del menu (plato, bebida, postre)
- **Atributos**: codigo, nombre, precio, categoria
- **Metodos**: obtener_precio(), aplicar_descuento(), __str__()

### modelos/cliente.py
- **Clase Cliente**: Representa a una persona que realiza pedidos
- **Atributos**: id_cliente, nombre, telefono, historial_pedidos
- **Metodos**: agregar_pedido(), obtener_historial(), obtener_total_gastado(), __str__()

### servicios/restaurante.py
- **Clase Restaurante**: Servicio central que gestiona productos y clientes
- **Responsabilidades**: 
  - Registrar y almacenar productos
  - Registrar y almacenar clientes
  - Crear pedidos (orquestar productos y clientes)
  - Buscar productos y clientes
  - Mostrar informacion

### main.py
- Punto de entrada de la aplicacion
- Demuestra el funcionamiento creando:
  - Un restaurante
  - Varios productos
  - Varios clientes
  - Multiples pedidos
  - Muestra resultados en consola

## Como ejecutar el programa

Desde la carpeta raiz del repositorio:

```bash
cd "Parcial 1\Semana 4"
python restaurante_app\main.py
```

O directamente desde la carpeta restaurante_app:

```bash
cd "Parcial 1\Semana 4\restaurante_app"
python main.py
```

## Importancia de la Modularizacion y Separacion de Responsabilidades

### Modularizacion
- **Facilita el mantenimiento**: Cada modulo tiene un proposito especifico y es facil de entender y modificar
- **Reutilizacion**: Las clases pueden reutilizarse en otros proyectos sin dependencias innecesarias
- **Escalabilidad**: Permite agregar nuevas funcionalidades sin afectar codigo existente

### Separacion de Responsabilidades
- **Modelos**: Solo representan datos y comportamiento basico de las entidades
- **Servicios**: Gestionan la logica de negocio y orquestacion entre modelos
- **Main**: Solo es responsable de demostrar el uso del sistema

### Ventajas
1. **Codigo mas limpio y legible**: Es facil entender que hace cada clase
2. **Pruebas mas simples**: Cada componente puede probarse independientemente
3. **Mantenimiento reducido**: Los cambios en una clase no afectan a otras innecesariamente
4. **Colaboracion en equipo**: Varios desarrolladores pueden trabajar en modulos diferentes sin conflictos
5. **Control de cambios**: Es facil trackear que cambio y por que

## Ejemplos de Entidades y Relaciones

- **Producto**: Autonomo, representa un articulo disponible
- **Cliente**: Autonomo, representa una persona
- **Restaurante**: Orquestador, contiene y gestiona productos y clientes
- **Pedido**: Relacion entre Cliente y Productos, creado por el Restaurante

## Requisitos cumplidos

- [x] Estructura de carpetas modelos, servicios y main.py
- [x] Clase Producto con atributos y metodos
- [x] Clase Cliente con atributos y metodos
- [x] Clase Restaurante que gestiona el sistema
- [x] Constructor __init__() en todas las clases
- [x] Metodo __str__() en clases pertinentes
- [x] Importaciones correctas entre archivos
- [x] Creacion de objetos en main.py
- [x] Demostracion de funcionalidad en consola
- [x] Comentarios explicativos en el codigo
- [x] README.md con documentacion completa
