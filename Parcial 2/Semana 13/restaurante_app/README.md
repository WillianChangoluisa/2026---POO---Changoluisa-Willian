# restaurante_app

Aplicación base del proyecto de restaurante creada con Tkinter. La estructura está organizada en capas para separar modelos, servicios, datos JSON y la interfaz gráfica.

## Propósito

Esta primera versión permite:

- acceder mediante una pantalla de login simulado,
- consultar los productos almacenados,
- consultar los usuarios registrados,
- validar el acceso desde `RestauranteServicio`,
- mantener una sola ventana principal y cambiar de vista sin cerrar la aplicación.

## Estructura

- `datos/`: archivos JSON con productos y usuarios.
- `modelos/`: clases `Producto` y `Usuario`.
- `servicios/`: lectura de archivos y lógica de negocio del restaurante.
- `ui/`: pantallas de login y principal.
- `main.py`: punto de entrada de la aplicación.

## Ejecución

```bash
python main.py
```

O desde la carpeta superior:

```bash
python restaurante_app/main.py
```

## Usuarios de prueba

- `admin` / `1234`
- `cajero` / `5678`
