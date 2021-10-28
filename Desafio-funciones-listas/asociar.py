def promedio_velocidad(lista):
    cont = 0
    for i in lista:
        cont += i[0]
    return cont / len(lista)


def promedio_distancia(lista):
    cont = 0
    for i in lista:
        cont += i[1]
    return cont / len(lista)


def cont_velocidad_menor(lista):
    cont = 0
    for i in lista:
        if i[0] < promedio_velocidad(lista):
            cont += 1
    return cont


def cont_velocidad_menor_distancia_mayor(lista):
    cont = 0
    for i in lista:
        if i[0] < promedio_velocidad(lista) and i[1] > promedio_distancia(lista):
            cont += 1
    return cont


def cont_velocidad_mayor(lista):
    cont = 0
    for i in lista:
        if i[0] > promedio_velocidad(lista):
            cont += 1
    return cont


def cont_velocidad_mayor_distancia_menor(lista):
    cont = 0
    for i in lista:
        if i[0] > promedio_velocidad(lista) and i[1] < promedio_distancia(lista):
            cont += 1
    return cont


def resultados(velocidad, distancia):
    lista = list(zip(velocidad, distancia))
    print("Velocidad bajo el promedio: " + str(cont_velocidad_menor(lista)))
    print(
        "Velocidad bajo el promedio y distancia sobre el promedio: " + str(cont_velocidad_menor_distancia_mayor(lista)))
    print("Velocidad sobre el promedio: " + str(cont_velocidad_mayor(lista)))
    print(
        "Velocidad sobre el promedio y distancia bajo el promedio: " + str(cont_velocidad_mayor_distancia_menor(lista)))


velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10,
             11, 11, 12, 12, 12, 12, 13, 13,
             13, 13, 14, 14, 14, 14, 15, 15,
             15, 16, 16, 17, 17, 17, 18, 18,
             18, 18, 19, 19, 19, 20, 20, 20,
             20, 20, 22, 23, 24, 24, 24, 24, 25]
distancia = [2, 10, 4, 22, 16, 10, 18, 26, 34,
             17, 28, 14, 20, 24, 28, 26, 34, 34,
             46, 26, 36, 60, 80, 20, 26, 54, 32,
             40, 32, 40, 50, 42, 56, 76, 84, 36,
             46, 68, 32, 48, 52, 56, 64, 66, 54,
             70, 92, 93, 120, 85]
resultados(velocidad, distancia)
