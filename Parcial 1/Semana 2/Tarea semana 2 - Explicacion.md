# Explicación detallada del programa: `CuentaBancaria`

Este documento explica paso a paso el contenido de `Tarea semana 2.py` para quien está empezando en Programación Orientada a Objetos (POO).

## Resumen

El programa define una clase llamada `CuentaBancaria` que modela una cuenta del mundo real con atributos y comportamientos (métodos) como `depositar`, `retirar` y `transferir`. Al final hay una pequeña demostración que crea dos cuentas y muestra operaciones básicas.

---

## Secciones principales del código

1. Encabezado y documentación
2. Importaciones y contador de números de cuenta
3. Definición de la clase `CuentaBancaria`
4. Implementación de métodos (comportamientos)
5. Función de demostración y ejecución directa

A continuación se detalla cada sección.

### 1) Encabezado y documentación

Al inicio del archivo hay un bloque de documentación entre comillas triples. Describe de forma breve qué hace el archivo, la clase que contiene y qué se demuestra en `__main__`.

Propósito: ayudar a cualquier lector (incluido tú mismo) a entender rápidamente la intención del archivo.

### 2) Importaciones y contador de cuentas

Líneas clave:

- `from __future__ import annotations` — permite usar anotaciones de tipo que referencian la propia clase dentro de la definición (útil para `CuentaBancaria` en `transferir`).
- `from dataclasses import dataclass, field` — usamos `@dataclass` para reducir código repetitivo (como `__init__`).
- `import itertools` — para crear un contador automático de números de cuenta.
- `_account_counter = itertools.count(1001)` — contador que genera números de cuenta únicos empezando en 1001.

Por qué: estas importaciones hacen el código más claro y menos propenso a errores. El contador evita que tengas que asignar manualmente números de cuenta.

### 3) Definición de la clase `CuentaBancaria`

La clase se declara con `@dataclass` para generar automáticamente el constructor y otras funciones útiles.

Campos principales:

- `titular: str` — nombre del propietario de la cuenta.
- `saldo: float = 0.0` — saldo inicial (por defecto 0.0).
- `numero_cuenta: int = field(default_factory=lambda: next(_account_counter))` — se asigna automáticamente un número.

Notas de POO:

- Clase: plantilla que describe objetos del mismo tipo (aquí: cuentas bancarias).
- Objeto (instancia): cuando haces `CuentaBancaria("Ana")` creas una cuenta concreta con sus propios valores.

### 4) Métodos (comportamientos)

Los métodos son funciones dentro de la clase que actúan sobre sus datos (atributos).

- `depositar(self, cantidad: float) -> None`:
  - Comprueba que `cantidad` sea positiva.
  - Suma la cantidad al `saldo`.
  - Levanta `ValueError` si la cantidad no es válida.

- `retirar(self, cantidad: float) -> None`:
  - Comprueba que `cantidad` sea positiva.
  - Verifica que haya fondos suficientes (`cantidad <= saldo`).
  - Resta del `saldo` o lanza `ValueError` si no hay suficiente dinero.

- `transferir(self, cantidad: float, destino: "CuentaBancaria") -> None`:
  - Verifica que `destino` sea otra `CuentaBancaria`.
  - Usa `self.retirar(cantidad)` (reutiliza lógica) y luego `destino.depositar(cantidad)`.
  - Esto demuestra el principio DRY (Don't Repeat Yourself): reutilizar métodos evita duplicar validaciones.

- `__str__(self) -> str`:
  - Método especial que devuelve una representación legible de la cuenta, útil para `print()`.

Conceptos de POO visibles aquí:

- Encapsulación: los datos (`saldo`, `titular`) están unidos a los métodos que los manipulan.
- Reutilización: `transferir` llama a `retirar` y `depositar`.

### 5) Demo y ejecución directa

Función `_demo()` crea dos instancias:

- `a = CuentaBancaria("Ana Pérez", saldo=500.0)`
- `b = CuentaBancaria("Luis Gómez", saldo=150.0)`

Se muestran operaciones: imprimir estados, depositar, transferir y manejar un intento de retirar más dinero del disponible (capturando la excepción y mostrando el error).

Bloque `if __name__ == "__main__":`:

- Esto hace que `_demo()` se ejecute sólo cuando ejecutas el archivo directamente (`python "Tarea semana 2.py"`) y no cuando importas la clase desde otro módulo. Es una buena práctica para incluir demos o pruebas rápidas.

---

## Explicación paso a paso (lectura sugerida)

Si quieres leer el código línea por línea, sigue este orden mental:

1. Lee las importaciones y entiende qué herramientas externas usamos (`dataclass`, `itertools`).
2. Observa cómo se genera el `numero_cuenta` automáticamente.
3. Estudia los métodos: intenta imaginar qué pasa si depositas números negativos o si pides retirar más de lo que hay.
4. Revisa `_demo()` para ver ejemplos prácticos de uso.

## Cómo ejecutar el programa

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
python "Parcial 1/Semana 2/Tarea semana 2.py"
```

Verás impresiones por pantalla con los estados antes y después de las operaciones.

## Buenas prácticas y recomendaciones para principiantes

- Prueba diferentes entradas (cantidad negativa, transferencias a la misma cuenta, etc.) para entender manejo de errores.
- Añade comentarios cortos sobre la intención de cada método si algo no queda claro.
- Intenta escribir pruebas pequeñas (funciones que creen cuentas y verifiquen saldos) cuando te sientas cómodo.

## Ejercicios propuestos

1. Añade un método `historial` que guarde una lista de transacciones (depósitos, retiros, transferencias).
2. Implementa límites: por ejemplo un `límite_diario_retiro` que evite sacar demasiado en un día.
3. Crea una clase `Banco` que contenga varias `CuentaBancaria` y permita buscar cuentas por titular o número.

---

Si quieres, puedo también:

- Agregar comentarios en el propio archivo `Tarea semana 2.py` explicando cada bloque.
- Escribir pruebas unitarias sencillas con `unittest`.
- Implementar el ejercicio 1 y dejar el código listo.

Dime qué prefieres y continúo.
