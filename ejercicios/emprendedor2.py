if __name__ == '__main__':
    print("Ingrese la cantidad de usuarios normales")
    normales = input()
    print("Ingrese la cantidad de usuarios premium")
    premium = input()
    print("Ingrese la cantidad de usuarios prueba")
    prueba = input()

    print("Ingrese el precio de venta de un servicio")
    precio = input()
    print("Ingrese los gastos asociados")
    gastos = input()

    print("Las utilidades son " + str(precio * (normales+(premium*2)) - gastos))