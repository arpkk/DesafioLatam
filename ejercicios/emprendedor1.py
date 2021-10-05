if __name__ == '__main__':
    print("Ingrese el precio de venta de un servicio")
    precio=input()
    print("Ingrese el numero de usuarios suscritos")
    cantusuarios=input()
    print("Ingrese los gastos asociados")
    gastos=input()
    print("Las utilidades son "+str(precio*cantusuarios-gastos))