# Contador de vocales
# Solicita al usuario una palabra y, con un for,
# cuenta cuántas vocales (a, e, i, o, u) contiene. Muestra el total al final.


vocales = "aeiou"
palabra = str(input("Escribe una palabra: "))
contador = 0

for letra in palabra:
    if letra.lower() in vocales:
        contador += 1
    
print(f"La palabra '{palabra} tiene {contador} vocales")