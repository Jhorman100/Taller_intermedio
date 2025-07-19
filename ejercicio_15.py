# Búsqueda con while-else
# Dada la lista [4, 8, 15, 16, 23, 42], pide al usuario un número a buscar.

# Recorre la lista con un while y, si lo encuentras, muestra su índice y haz break.

# Si terminas el bucle sin encontrarlo, el bloque else debe imprimir “Número no encontrado”.



lista = [4, 8, 15, 16, 23, 42]
numero_buscado = True

while lista:
    numero = int(input("Ingrese el numero a buscar: "))
    if numero in lista:
        numero_buscado = False
        print("Numero encontrado")
        break
    else:
        print("Numero no encontrado")

