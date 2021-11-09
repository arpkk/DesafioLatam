import sys

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

for param in sys.argv[1:]:
    ban = False
    for mes, value in ventas.items():
        if value == int(param):
            print(mes)
            ban = True
            break
    if ban==False:
        print("No encontrado")