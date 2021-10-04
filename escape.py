#Autor: Gina Ozimisa
#Se pide crear el programa escape.py donde el usuario ingrese la gravedad y el radio y como
#resultado obtenga la velocidad de escape.


import sys

def ue(g, r):
    return (2 * float(g) * float(r)*1000) ** 0.5


if __name__ == '__main__':
    print("La velocidad de escape es "+str(ue(sys.argv[1], sys.argv[2]))+" m/s")
