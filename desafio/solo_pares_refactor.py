n = int(input("Ingrese la cantidad de numeros pares\n"))
print("\n")

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
