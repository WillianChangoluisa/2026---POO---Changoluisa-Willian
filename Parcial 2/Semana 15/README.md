# Restaurant App - Semana 15

## Descripción

Esta versión de `restaurante_app` conserva la arquitectura modular desarrollada en semanas anteriores y añade la operación de ventas como ejemplo claro del manejo de eventos en una interfaz gráfica con Tkinter.

La funcionalidad principal demuestra el flujo:

Usuario -> acción -> botón con `command=` -> callback -> servicio -> persistencia -> respuesta visual.

## Estructura del proyecto

- `restaurante_app/datos/`: archivos JSON con usuarios, productos y ventas.
- `restaurante_app/modelos/`: clases `Usuario`, `Producto` y `Venta`.
- `restaurante_app/servicios/`: lectura/escritura de archivos y lógica del negocio.
- `restaurante_app/ui/`: pantallas de autenticación y vista principal.
- `restaurante_app/assets/`: recursos visuales del sistema.
- `restaurante_app/main.py`: punto de entrada de la aplicación.

## Funcionalidades

- Inicio de sesión con validación del usuario.
- Consulta de usuarios registrada.
- Gestión de productos ya desarrollada anteriormente.
- Nueva sección de ventas.
- Selección de usuario y producto mediante `ttk.Combobox`.
- Botón `Registrar venta` vinculado con `command=self.registrar_venta`.
- Callback que llama al servicio para validar y registrar la venta.
- Persistencia de ventas en `datos/ventas.json`.
- Tabla de ventas actualizada automáticamente en la interfaz.

## Ejecución

Desde la carpeta `Parcial 2/Semana 15`:

```bash
python restaurante_app/main.py
```

## Credenciales de prueba

- `admin` / `1234`
- `cajero` / `5678`
