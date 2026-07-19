# Instrucciones - Semana 8 (restaurante_app)

1. Abrir PowerShell y navegar a la carpeta del proyecto:

```powershell
cd "C:\Users\William.Changoluisa\PycharmProjects\2026---POO---Changoluisa-Willian\Parcial 1\semana 8\restaurante_app"
```

2. Ejecutar la aplicación:

```powershell
python main.py
```

3. Menú disponible:

- 1. Registrar producto
- 2. Registrar bebida
- 3. Registrar cliente
- 4. Listar productos
- 5. Listar clientes
- 6. Salir

4. Recomendaciones de prueba:
- Registrar una `Bebida` y luego listar productos; comprobar que la bebida aparece usando `mostrar_informacion()`.
- Intentar registrar dos productos con el mismo `codigo` para comprobar la validación.
- Intentar registrar dos clientes con la misma `identificacion` para comprobar la validación.

5. Archivos importantes:
- `modelos/producto.py`: clase `Producto`.
- `modelos/bebida.py`: clase `Bebida` (hereda de `Producto`).
- `modelos/cliente.py`: clase `Cliente` (@dataclass).
- `servicios/restaurante.py`: clase `Restaurante` (lógica y validaciones).
- `main.py`: menú y entrada de usuario.

6. Comprobar sintaxis (opcional):

```powershell
python -m py_compile main.py
```

Si necesitas que añada ejemplos de datos o pruebas unitarias (por ejemplo `test_sistema.py`), dímelo y los agregaré.

