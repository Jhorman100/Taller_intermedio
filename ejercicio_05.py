# Promedio de lista
# Dada la lista [12, 7, 22, 5, 14, 9], utiliza un for,
# un acumulador y un contador para calcular y mostrar su promedio.


numeros = [12, 7, 22, 5, 14, 9]
contador = 0
sumatoria = 0
print(f"{numeros}")


for i in numeros:
    sumatoria += i
    contador += 1

promedio = sumatoria / contador

print(f"{promedio}")


