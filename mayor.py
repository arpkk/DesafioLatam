# Autor: Gina Ozimisa
# Se pide crear el programa mayor.py, este script debe tomar los 3 argumentos y determinar
# cual es el mayor.

import sys


def grande(a, b, c):
    return max(a, b, c)


if __name__ == '__main__':
    print(grande(sys.argv[1], sys.argv[2], sys.argv[3]))
