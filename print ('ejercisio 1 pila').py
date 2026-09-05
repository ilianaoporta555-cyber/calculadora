
pila = []

while True:

    print("==** MENÚ **==")
    print("1. Agregar número")
    print("2. Contar elementos")
    print("3. Mostrar elementos")
    print("4. Calcular promedio")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        numero = int(input("Ingrese un número entero: "))
        pila.append(numero)

        print("Número agregado correctamente.")

    elif opcion == "2":

        cantidad = len(pila)

        print("Cantidad de elementos:", cantidad)

    elif opcion == "3":

        if len(pila) == 0:
            print("La pila está vacía.")

        else:
            print("\nElementos de la pila:")

            for numero in reversed(pila):
                print(numero)

    elif opcion == "4":

        if len(pila) == 0:
            print("No se puede calcular el promedio.")
            print("La pila está vacía.")

        else:
            suma = sum(pila)
            promedio = suma / len(pila)

            print("Promedio:", promedio)

    elif opcion == "5":

        print("Programa finalizado.")
        break

    else:

        print("Opción no válida. Intente nuevamente.")