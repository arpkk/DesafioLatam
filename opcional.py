password = int(input("Ingrese password\n"))

if password == 12345:
    print("Password incorrecto")
else:
    if password < 100000:
        print("la contrasena tiene menos de 6 letras")
    valor1 = int(input("Ingrese valor 1\n"))
    valor2 = int(input("Ingrese valor 2\n"))
    if valor1 >= valor2:
        print("valor1 {} es mayor".format(valor1))
    else:
        print("valor2 {} es mayor".format(valor2))
