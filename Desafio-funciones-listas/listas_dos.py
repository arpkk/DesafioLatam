import listas_uno
import velocidad

def promedios_datos_autos():
    autos = listas_uno.lista()
    camp1 = []
    camp2 = []
    camp3 = []
    for i in autos:
        camp1.append(i[1])
        camp2.append(i[2])
        camp3.append(i[4])
    print("el promedio del primer campo numerico es: " + str(velocidad.promedio(camp1)))
    print("el promedio del segundo campo numerico es: " + str(velocidad.promedio(camp2)))
    print("el promedio del tercer campo numerico es: " + str(velocidad.promedio(camp3)))
