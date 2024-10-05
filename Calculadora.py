def calculadora():
    print("Selecciona la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    # Pedir al usuario que seleccione una operación
    opcion = input("Ingresa el número de la operación (1/2/3/4): ")

    # Pedir al usuario los dos números
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    # Realizar la operación correspondiente
    if opcion == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif opcion == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif opcion == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif opcion == '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: División por cero no permitida.")
    else:
        print("Opción no válida.")

# Llamar a la función de calculadora
calculadora()
