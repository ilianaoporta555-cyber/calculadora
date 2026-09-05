cola = []
pila = []


while True:
    print("\n--- CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Ver cola")
    print("6. Ver pila")
    print("7. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "7":
        print("Programa terminado")
        break

    if opcion in ["1", "2", "3", "4"]:
        n1 = float(input("Primer numero: "))
        n2 = float(input("Segundo numero: "))

        if opcion == "1":
            resultado = n1 + n2
            operacion = str(n1) + " + " + str(n2)

        elif opcion == "2":
            resultado = n1 - n2
            operacion = str(n1) + " - " + str(n2)

        elif opcion == "3":
            resultado = n1 * n2
            operacion = str(n1) + " * " + str(n2)

        elif opcion == "4":
            if n2 == 0:
                print("No se puede dividir entre cero")
                continue

            resultado = n1 / n2
            operacion = str(n1) + " / " + str(n2)

        # Guardar en la cola
        cola.append(operacion)

        # Guardar en la pila
        pila.append(resultado)

        print("Resultado:", resultado)

    elif opcion == "5":
        print("\nCola:")
        for elemento in cola:
            print(elemento)

    elif opcion == "6":
        print("\nPila:")
        for elemento in reversed(pila):
            print(elemento)

    else:
        print("Opcion incorrecta")