contrasena = input("Ingresa contrasena\n")
cont = 0

for j in range(len(contrasena)):
    for i in range(ord('a'), ord('z') + 1):
        cont = cont + 1
        if chr(i) == contrasena[j]:
            break
print(str(cont)+" intentos")