# restaurante_app - Semana 14

## Descripción

Esta versión de `restaurante_app` evoluciona la interfaz gráfica sin perder la arquitectura modular. La aplicación mantiene el acceso por usuario y contraseña, consulta de usuarios y añade una gestión de productos con formularios, contenedores y controles de acción usando Tkinter y ttk.

## Estructura del proyecto

- `datos/`: archivos JSON con productos y usuarios.
- `modelos/`: clases `Producto` y `Usuario`.
- `servicios/`: lectura/escritura de archivos y lógica del negocio de restaurante.
- `ui/`: pantallas de login y vista principal.
- `main.py`: punto de entrada de la aplicación.

## Componentes y contenedores utilizados

- `Frame` para estructurar la ventana principal.
- `Label` y `Entry` para el formulario de productos.
- `Button` para registrar, consultar, actualizar y eliminar productos.
- `Treeview` para visualizar la lista de productos.
- `Text` para mostrar los usuarios registrados.
- `pack` y `grid` para organizar los contenedores y mantener una experiencia clara para el usuario.

## Operaciones implementadas sobre productos

- Registrar productos.
- Consultar un producto por código.
- Actualizar información del producto.
- Eliminar un producto.
- Persistencia en `datos/productos.json`.

## Validaciones y persistencia

Las validaciones de negocio y los cambios sobre productos se gestionan desde `RestauranteServicio`, evitando la manipulación directa de archivos JSON desde la capa visual. El servicio guarda los datos en los JSON correspondientes cada vez que se realiza una operación.

## Ejecución

Desde la carpeta `Parcial 2/Semana 14`:

```bash
python restaurante_app/main.py
```

O desde dentro de la carpeta del proyecto:

```bash
cd restaurante_app
python main.py
```

## Credenciales de prueba

- `admin` / `1234`
- `cajero` / `5678`
