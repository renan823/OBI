N = int(input("Números: "))

numeros = []
for i in range(0, N, 1):
    num = int(input("Número: "))
    if(num > 0):
        numeros.append(num)
    else:
        numeros.pop()

print(sum(numeros))