def mostrar_menu(saldo=0):
    n = int(input(
        "Bienvenido al portal del Banco Amigo. Escoja una opción:\n1. Consultar saldo\n2. Hacer depósito\n3. Realizar giro\n4. Salir\n"))
    while 4 != n:
        if n == 1:
            print("Su saldo es: " + str(saldo))
            n = int(input("Escoja una opción:\n1. Consultar saldo\n2. Hacer depósito\n3. Realizar giro\n4. Salir\n"))
        elif n == 2:
            cantidad = int(input("Ingrese la cantidad a depositar\n"))
            saldo = depositar(saldo, cantidad)
            print("Su nuevo saldo es: " + str(saldo))
            n = int(input("Escoja una opción:\n1. Consultar saldo\n2. Hacer depósito\n3. Realizar giro\n4. Salir\n"))
        elif n == 3:
            cantidad = int(input("Ingrese la cantidad a girar\n"))
            if saldo < 0:
                print("No se puede girar esta cantidad. Su saldo es 0")
            else:
                while not girar(saldo, cantidad):
                    print("No se puede girar esta cantidad. Su saldo es de " + str(saldo))
                    cantidad = int(input("Ingrese la cantidad a girar\n"))

                saldo = girar(saldo, cantidad)
                print("Su nuevo saldo es: " + str(saldo))
            n = int(input("Escoja una opción:\n1. Consultar saldo\n2. Hacer depósito\n3. Realizar giro\n4. Salir\n"))
        else:
            print("Opción invalida. Por favor ingrese 1, 2, 3 ó 4.")
            n = int(input("Escoja una opción:\n1. Consultar saldo\n2. Hacer depósito\n3. Realizar giro\n4. Salir\n"))
    print("Adios")


def depositar(saldo, cantidad):
    return saldo + cantidad


def girar(saldo, cantidad):
    if saldo > cantidad:
        return saldo - cantidad
    return False

mostrar_menu(5)
