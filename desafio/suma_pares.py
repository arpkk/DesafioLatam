n = int(input("Ingrese la cantidad de numeros pares\n"))
print("\n")
sum=0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum=sum+i
print(sum)
