# Menú repetitivo
# Desarrolla un menú en bucle while con estas opciones:

# Sumar dos números

# Restar dos números

# Multiplicar dos números

# Salir
# Elige la opción, pide los operandos, muestra el resultado y vuelve a mostrar
# el menú hasta que seleccione “Salir”.


while True:
    print("1 - sumar")
    print("2 - restar")
    print("3 - multiplicar")
    print("4 - salir")

    opcion = int(input("Escoje una opcion: "))

    if opcion == 1:
        numero_1 = int(input("Ingrese el primer numero: "))
        numero_2 = int(input("Ingrese el segundo numero: "))
        suma = numero_1 + numero_2
        print(f"La suma total es {suma}")

    elif opcion == 2:
        numero_1 = int(input("Ingrese el primer numero: "))
        numero_2 = int(input("Ingrese el segundo numero: "))
        resta = numero_1 - numero_2
        print(f"La resta total es {resta}")

    elif opcion == 3:
        numero_1 = int(input("Ingrese el primer numero: "))
        numero_2 = int(input("Ingrese el segundo numero: "))
        multiplicacion = numero_1 * numero_2
        print(f"La multiplicacion total es {multiplicacion}")
    
    elif opcion == 4:
        break