# Múltiplos de 3
# Escribe un programa que imprima todos los múltiplos de 3 entre 1 y 100.

cien = 100

for i in range(1, cien + 1):
    if i % 3 == 0:
        print("Es multiplo de tres")
    else:
        print(i)