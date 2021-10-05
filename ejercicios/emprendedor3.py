if __name__ == '__main__':
    print("Ingrese el precio de venta de un servicio")
    precio=input()
    print("Ingrese el numero de usuarios suscritos")
    cantusuarios=input()
    print("Ingrese los gastos asociados")
    gastos=input()
    print("Ingrese la utilidad pasada (0 para no ingresar)")
    utilidadPasada = input()
    if utilidadPasada==0:
        utilidadPasada=1000

    utilidad=precio*cantusuarios-gastos

    razon=utilidad/utilidadPasada
    if(razon>1):
        print("Las utilidades actuales fueron superiores a las anteriores.")
    else:
        print("Las utilidades actuales fueron inferiores a las anteriores.")
