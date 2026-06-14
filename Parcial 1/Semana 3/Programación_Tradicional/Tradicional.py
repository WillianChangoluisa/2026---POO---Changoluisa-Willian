mascotas = []

def registrar_mascota():
    """
    Registra una nueva mascota solicitando datos por teclado.
    Almacena la información en un diccionario dentro de la lista global.
    """
    print("\n" + "="*50)
    print("REGISTRAR NUEVA MASCOTA")
    print("="*50)

    # Solicitar datos de la mascota
    nombre = input("Ingrese el nombre de la mascota: ")
    tipo = input("Ingrese el tipo de mascota (perro, gato, loro, etc.): ")
    edad = input("Ingrese la edad de la mascota: ")
    color = input("Ingrese el color de la mascota: ")
    raza = input("Ingrese la raza de la mascota: ")

    # Crear diccionario con la información de la mascota
    mascota = {
        "nombre": nombre,
        "tipo": tipo,
        "edad": edad,
        "color": color,
        "raza": raza
    }

    # Agregar la mascota a la lista
    mascotas.append(mascota)
    print(f"\n✓ Mascota '{nombre}' registrada exitosamente.")

def mostrar_mascotas():
    """
    Muestra toda la información registrada de las mascotas de forma organizada.
    """
    print("\n" + "="*50)
    print("INFORMACIÓN DE MASCOTAS REGISTRADAS")
    print("="*50)

    if len(mascotas) == 0:
        print("\nNo hay mascotas registradas aún.")
    else:
        for indice, mascota in enumerate(mascotas, 1):
            print(f"\n--- Mascota {indice} ---")
            print(f"Nombre:  {mascota['nombre']}")
            print(f"Tipo:    {mascota['tipo']}")
            print(f"Edad:    {mascota['edad']}")
            print(f"Color:   {mascota['color']}")
            print(f"Raza:    {mascota['raza']}")

    print("\n" + "="*50)

def buscar_mascota():
    """
    Busca una mascota por nombre y muestra su información.
    """
    print("\n" + "="*50)
    print("BUSCAR MASCOTA")
    print("="*50)

    nombre_busca = input("Ingrese el nombre de la mascota a buscar: ").lower()
    encontrada = False

    for mascota in mascotas:
        if mascota['nombre'].lower() == nombre_busca:
            print(f"\n✓ Mascota encontrada:")
            print(f"Nombre:  {mascota['nombre']}")
            print(f"Tipo:    {mascota['tipo']}")
            print(f"Edad:    {mascota['edad']}")
            print(f"Color:   {mascota['color']}")
            print(f"Raza:    {mascota['raza']}")
            encontrada = True
            break

    if not encontrada:
        print(f"\n✗ No se encontró ninguna mascota con el nombre '{nombre_busca}'")

    print("="*50)

def editar_mascota():
    """
    Edita la información de una mascota existente.
    """
    print("\n" + "="*50)
    print("EDITAR MASCOTA")
    print("="*50)

    nombre_busca = input("Ingrese el nombre de la mascota a editar: ").lower()

    for mascota in mascotas:
        if mascota['nombre'].lower() == nombre_busca:
            print(f"\n✓ Mascota encontrada. Ingrese los nuevos datos (presione Enter para no cambiar):")

            nuevo_nombre = input("Nuevo nombre (actual: " + mascota['nombre'] + "): ")
            if nuevo_nombre:
                mascota['nombre'] = nuevo_nombre

            nuevo_tipo = input("Nuevo tipo (actual: " + mascota['tipo'] + "): ")
            if nuevo_tipo:
                mascota['tipo'] = nuevo_tipo

            nueva_edad = input("Nueva edad (actual: " + mascota['edad'] + "): ")
            if nueva_edad:
                mascota['edad'] = nueva_edad

            nuevo_color = input("Nuevo color (actual: " + mascota['color'] + "): ")
            if nuevo_color:
                mascota['color'] = nuevo_color

            nueva_raza = input("Nueva raza (actual: " + mascota['raza'] + "): ")
            if nueva_raza:
                mascota['raza'] = nueva_raza

            print("\n✓ Información de la mascota actualizada exitosamente.")
            print("="*50)
            return

    print(f"\n✗ No se encontró ninguna mascota con el nombre '{nombre_busca}'")
    print("="*50)

def eliminar_mascota():
    """
    Elimina una mascota del registro.
    """
    print("\n" + "="*50)
    print("ELIMINAR MASCOTA")
    print("="*50)

    nombre_busca = input("Ingrese el nombre de la mascota a eliminar: ").lower()

    for i, mascota in enumerate(mascotas):
        if mascota['nombre'].lower() == nombre_busca:
            confirmacion = input(f"¿Desea eliminar a '{mascota['nombre']}'? (s/n): ").lower()
            if confirmacion == 's':
                mascotas.pop(i)
                print("\n✓ Mascota eliminada exitosamente.")
            else:
                print("\n✗ Operación cancelada.")
            print("="*50)
            return

    print(f"\n✗ No se encontró ninguna mascota con el nombre '{nombre_busca}'")
    print("="*50)

def contar_mascotas():
    """
    Conta el número total de mascotas registradas.
    """
    return len(mascotas)

def menu_principal():
    """
    Muestra el menú principal y maneja las opciones del usuario.
    """
    while True:
        print("\n" + "*"*50)
        print("Hola  Bienvenido al Sistema de Registro de Mascotas")
        print("Aquí puedes registrar, ver, buscar, editar y eliminar información de tus mascotas.")
        print("*"*50)
        print(" Selecciona la opcion que deseas realizar con tus mascotas:")
        print("1. Registrar nueva mascota")
        print("2. Ver todas las mascotas")
        print("3. Buscar mascota")
        print("4. Editar mascota")
        print("5. Eliminar mascota")
        print("6. Ver cantidad total de mascotas")
        print("7. Salir")
        print("="*50)

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == '1':
            registrar_mascota()
        elif opcion == '2':
            mostrar_mascotas()
        elif opcion == '3':
            buscar_mascota()
        elif opcion == '4':
            editar_mascota()
        elif opcion == '5':
            eliminar_mascota()
        elif opcion == '6':
            cantidad = contar_mascotas()
            print(f"\nTotal de mascotas registradas: {cantidad}")
        elif opcion == '7':
            print("\n¡Gracias por usar el sistema de registro de mascotas!")
            print("*"*50)
            break
        else:
            print("\n✗ Opción inválida. Por favor, intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu_principal()

