# Explorando range()
# Escribe un programa que cree y muestre las listas resultantes de:

# list(range(5))

# list(range(1, 6))

# list(range(0, 10, 2))

print("Lista 1")

for i in range(0, 5):
    print(f"Hola soy el numero {i + 1} de la lista 1")

print("Lista 2")

for i in range(1, 6):
    print(f"Soy el numero {i + 1} de la lista 2")

print("Lista 3")
for i in range(0, 10, 2):
    print(f"Soy el numero {i + 1} de la lista 3")