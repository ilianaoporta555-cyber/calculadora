
pila = []

def agregar_nombre():
    nombre = input("Ingrese el primer nombre: ")
    pila.append(nombre)
    print("Nombre agregado correctamente.")

def eliminar_nombre():
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        nombre = pila.pop()
        print("Nombre eliminado:", nombre)

def mostrar_cima():
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        print("Elemento en la cima:", pila[-1])

def buscar_nombre():
    nombre = input("Ingrese el nombre que desea buscar: ")

    if nombre in pila:
        print("El nombre se encuentra en la pila.")
    else:
        print("El nombre no se encuentra en la pila.")

def contar_elementos():
    cantidad = len(pila)
    print("Cantidad de elementos:", cantidad)

def mostrar_elementos():
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        print("Elementos de la pila:")
        for nombre in reversed(pila):
            print(nombre)

def limpiar_pila():
    pila.clear()
    print("La pila ha sido limpiada.")

def mostrar_menu():
    print("\n========== MENÚ ==========")
    print("1. Agregar nombre")
    print("2. Eliminar nombre de la pila")
    print("3. Mostrar último elemento en la cima")
    print("4. Buscar elemento de la pila")
    print("5. Contar elementos de la pila")
    print("6. Mostrar todos los elementos")
    print("7. Limpiar la pila")
    print("8. Salir")
    print("==========================")

while True:
    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_nombre()

    elif opcion == "2":
        eliminar_nombre()

    elif opcion == "3":
        mostrar_cima()

    elif opcion == "4":
        buscar_nombre()

    elif opcion == "5":
        contar_elementos()

    elif opcion == "6":
        mostrar_elementos()

    elif opcion == "7":
        limpiar_pila()

    elif opcion == "8":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")