N = int(input("Num. registros: "))
amigos = {}
cont = 0

# amigo = [tempo, msgEnviadas, Respostas]
anterior = 'T'
while cont < N:
    val1, val2 = [(i) for i in input().split()]
    if val1 == 'R':
        try:
            amigos[val2][1]+=1
        except:
            amigos[val2] = [0, 1, 0]
        
        if anterior != 'T':
            for amigo in amigos:
                if amigo != val2 and amigos[amigo][1] != amigos[amigo][2]:
                    amigos[amigo][0]+=1

    elif val1 == 'E':
        if anterior != 'T':
            for amigo in amigos:
                if amigos[amigo][1] != amigos[amigo][2]:
                    amigos[amigo][0]+=1
        amigos[val2][2]+=1
    else:
        for amigo in amigos:
            amigos[amigo][0]+=int(val2)
    cont+=1
    anterior = val1

amigosOrdenados = []
for amigo in amigos:
    amigosOrdenados.append(int(amigo))
amigosOrdenados.sort()

print("")
for value in amigosOrdenados:
    amigo = str(value)
    if amigos[amigo][1] == amigos[amigo][2]:
        print(amigo + " " + str(amigos[amigo][0]))
    else:
        print(amigo + " -1")