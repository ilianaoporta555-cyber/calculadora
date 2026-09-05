pila = [
    "Boaco",
    "Carazo",
    "Chinandega",
    "Chontales",
    "Estelí",
    "Granada",
    "Jinotega",
    "León",
    "Madriz",
    "Masaya",
    "Matagalpa",
    "Nueva Segovia",
    "Río San Juan",
    "Rivas"
]


def agregar_departamento():
    departamento = input("Ingrese el departamento que desea agregar: ").strip()

    departamentos = [
        "Boaco",
        "Carazo",
        "Chinandega",
        "Chontales",
        "Estelí",
        "Granada",
        "Jinotega",
        "León",
        "Madriz",
        "Managua",
        "Masaya",
        "Matagalpa",
        "Nueva Segovia",
        "Río San Juan",
        "Rivas"
    ]

    encontrado = None

    for d in departamentos:
        if d.lower() == departamento.lower():
            encontrado = d
            break

    if encontrado is None:
        print("Ese no es un departamento de Nicaragua.")

    elif encontrado in pila:
        print("Ese departamento ya está en la pila.")

    else:
        pila.append(encontrado)
        print(encontrado, "fue agregado a la pila.")


def remover_departamento():
    if len(pila) == 0:
        print("La pila está vacía.")
        return

    departamento = input("Ingrese el departamento que desea remover: ").strip()

    encontrado = None

    for d in pila:
        if d.lower() == departamento.lower():
            encontrado = d
            break

    if encontrado is None:
        print("Ese departamento no está en la pila.")

    else:
        pila.remove(encontrado)
        print(encontrado, "fue removido de la pila.")


def imprimir_pila():
    if len(pila) == 0:
        print("La pila está vacía.")

    else:
        print("\n========== PILA ==========")

        for i, departamento in enumerate(reversed(pila), 1):
            print(f"{i}. {departamento}")

        print("==========================")


def buscar_departamento():
    departamento = input("Ingrese el departamento que desea buscar: ").strip()

    if departamento.lower() in [d.lower() for d in pila]:
        print("El departamento está en la pila.")
    else:
        print("El departamento no está en la pila.")


def mostrar_menu():
    print("\n========== MENÚ ==========")
    print("1. Agregar departamento")
    print("2. Remover departamento")
    print("3. Imprimir pila")
    print("4. Buscar departamento")
    print("5. Salir")
    print("==========================")


while True:
    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_departamento()

    elif opcion == "2":
        remover_departamento()

    elif opcion == "3":
        imprimir_pila()

    elif opcion == "4":
        buscar_departamento()

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")