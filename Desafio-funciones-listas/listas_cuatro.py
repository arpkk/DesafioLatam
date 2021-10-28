import listas_uno


def autos_true():
    autos = listas_uno.lista()
    for auto in autos:
        if auto[3]:
            print(auto[0])
