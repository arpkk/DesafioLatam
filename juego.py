# Autor: Gina Ozimisa
# Se pide crear el programa mayor.py, este script debe tomar los 3 argumentos y determinar
# cual es el mayor.

import sys
import random


def juegoRandom():
    return random.choice([1, 2, 3])


def partida(jugador, computador):
    print("Computador juega " + computador)
    if jugador == computador:
        print("Empataste.")
    if not (jugador in ['tijera', 'piedra', 'papel']):
        print("Argumento invalido: Debe ser piedra, papel o tijera.")
    else:
        if ((jugador == 'piedra' and computador == 'tijera') or (jugador == 'tijera' and computador == 'papel') or (
                jugador == 'papel' and computador == 'piedra')):
            print("Ganaste.")
        else:
            print("Perdiste.")


if __name__ == '__main__':

    jugador = sys.argv[1]

    if juegoRandom() == 1:
        computador = "piedra"
    elif juegoRandom() == 2:
        computador = "papel"
    else:
        computador = "tijera"
    partida(jugador, computador)
