# Validación de contraseña
# Implementa un programa que solicite una contraseña correcta (puedes fijarla en tu código)
# y permita hasta 3 intentos.

# Si el usuario acierta: imprime “¡Acceso concedido!” y termina.

# Si agota los 3 intentos: imprime “Usuario bloqueado” y termina.


contraseña = "jhormanelmejor"
intentos = 0
acceso = False

while intentos < 3:
    ingreso = input("Ingrese la contraseña: ")
    if ingreso == contraseña:
        acceso = True
        break
    intentos += 1



if acceso:
    print("Bienvenido señor Jhorman")
else:
    print("Demasiados intentos incorrectos")