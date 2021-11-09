from itertools import groupby

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

def sort_dic(dict1):
    sorted_dict = {}
    sorted_keys = sorted(dict1, key=dict1.get)  # [1, 3, 2]
    for w in sorted_keys:
        sorted_dict[w] = dict1[w]
    return sorted_dict

ventas=sort_dic(ventas)
new = {k: len(list(v)) for k, v in groupby(ventas, key=lambda x: ventas[x])}

print(new)