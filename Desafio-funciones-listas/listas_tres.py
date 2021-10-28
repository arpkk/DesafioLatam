import listas_uno
import velocidad


def mayores_al_promedio():
    autos = listas_uno.lista()
    camp1 = []
    for auto in autos:
        camp1.append(auto[1])
    for auto in autos:
        if auto[1] > velocidad.promedio(camp1):
            print(auto)
