# Semana 13 - Restaurante App con interfaz gráfica

Esta carpeta contiene la base inicial de una aplicación gráfica para el proyecto de restaurante usando Tkinter. La estructura sigue el mismo patrón del repositorio docente de la semana 13: modelos, servicios, datos JSON y una capa `ui/` para las vistas, con `main.py` como punto de entrada.

## Objetivo

Crear una versión preliminar de la interfaz de usuario que permita:

- iniciar sesión con un usuario simulado,
- validar credenciales a través de `RestauranteServicio`,
- mostrar los productos y usuarios cargados desde archivos JSON,
- mantener una sola ventana principal de Tkinter.

## Estructura

```
Semana 13/
├── README.md
└── restaurante_app/
    ├── __init__.py
    ├── main.py
    ├── README.md
    ├── datos/
    │   ├── productos.json
    │   └── usuarios.json
    ├── modelos/
    │   ├── __init__.py
    │   ├── producto.py
    │   └── usuario.py
    ├── servicios/
    │   ├── __init__.py
    │   ├── archivo_servicio.py
    │   └── restaurante_servicio.py
    └── ui/
        ├── __init__.py
        ├── login_view.py
        └── main_view.py
```

## Credenciales de prueba

- Usuario: `admin`
- Contraseña: `1234`

También se incluye un segundo usuario para probar el flujo:

- Usuario: `cajero`
- Contraseña: `5678`

## Ejecución

Desde la carpeta `Semana 13`:

```bash
python restaurante_app/main.py
```

## Flujo de la aplicación

1. Se inicia `main.py`.
2. La aplicación prepara la ventana principal y los servicios.
3. Se muestra la pantalla de login.
4. El usuario ingresa sus datos.
5. `RestauranteServicio` valida el acceso.
6. Si es correcto, se presenta la vista principal.
7. Se puede consultar la información de productos y usuarios.
8. El botón de cerrar sesión regresa a la pantalla de login dentro de la misma ventana.

## Observación

Esta versión es una base gráfica simplificada, conforme a la guía de la semana 13. Las ventas y otras funcionalidades complejas se mantienen como pendientes para futuras etapas.
