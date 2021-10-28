import listas_uno
import velocidad


def generar_lista_mayores():
    lista = []
    autos = listas_uno.lista()
    camp1 = []
    for auto in autos:
        camp1.append(auto[1])
    for auto in autos:
        if auto[1] > velocidad.promedio(camp1):
            lista.append(auto[1])
    return lista
