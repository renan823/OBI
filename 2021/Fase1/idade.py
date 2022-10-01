idades = []
cont = 0
while cont < 3:
    val = int(input("Digite a idade: "))
    idades.append(val)
    cont+=1
print(idades)
idades.sort()
print(idades[1])