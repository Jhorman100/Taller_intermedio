# Iteración sobre tuplas
# Define la tupla (10, 20, 30, 40, 50) y recórrela con un for
# para imprimir cada elemento y su índice (usa enumerate).


tupla = (10, 20, 30, 40, 50)
print(tupla)

i = 1

for elemento in tupla:
    print(f"{i}: {elemento}")
    i += 1
