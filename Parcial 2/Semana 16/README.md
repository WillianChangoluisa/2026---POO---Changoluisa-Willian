# Restaurant App - Semana 16

## Propósito

Esta entrega evoluciona el proyecto de la Semana 15 para practicar el manejo de eventos de Tkinter mediante la gestión administrativa de usuarios. Se conserva la aplicación del restaurante, su inicio de sesión, la gestión de productos y el registro de ventas.

## Organización

- `restaurante_app/datos/`: persistencia de productos, usuarios y ventas en archivos JSON.
- `restaurante_app/modelos/`: modelos `Producto`, `Usuario` y `Venta`.
- `restaurante_app/servicios/`: reglas del negocio y acceso a los archivos.
- `restaurante_app/ui/`: pantallas de login y panel principal.
- `restaurante_app/assets/`: logotipo e íconos de la aplicación.
- `restaurante_app/main.py`: punto de entrada.

## Gestión de usuarios

El usuario `Administrador` puede registrar, consultar, actualizar y eliminar cuentas de tipo `Empleado` y `Cliente`. El formulario valida los datos mediante `RestauranteServicio`, mientras que la tabla muestra el usuario, nombre, correo y rol; no muestra contraseñas. Para actualizar una cuenta, se deja el campo de contraseña vacío si no se desea cambiarla. La aplicación solicita confirmación antes de eliminar y protege la cuenta administrativa autenticada.

El modelo `Usuario` conserva el rol en `datos/usuarios.json`. Los registros previos a esta semana se cargan con un rol compatible: `admin` como Administrador, `cajero` como Empleado y las demás cuentas como Cliente.

## Eventos de Tkinter

- `<<TreeviewSelect>>` usa `bind()` para obtener el identificador seleccionado, consultar el usuario en el servicio y cargarlo en el formulario.
- `<Return>` llama al callback de registro existente, sin duplicar la lógica de negocio.
- `<Escape>` limpia el formulario y quita la selección.
- `<<ComboboxSelected>>` responde al cambio de rol y actualiza el mensaje de la interfaz.
- Los botones Registrar, Actualizar, Eliminar y Limpiar usan `command=`.

Los callbacks coordinan la interacción y la respuesta visual. La validación de usuarios y la persistencia permanecen en `RestauranteServicio` y `ArchivoServicio`.

## Ejecución

Desde esta carpeta:

```bash
python restaurante_app/main.py
```

Credenciales iniciales:

- Administrador: `admin` / `1234`
- Empleado: `cajero` / `5678`
