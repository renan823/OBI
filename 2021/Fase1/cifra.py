alfabeto = 'abcdefghijklmnopqrstuvxz'
vogais = 'aieou'

palavra = input("Digite a palavra: ")
cifrada = ''

def achaVogal(alfabeto):
    achaAntes = True
    vogalAntes = ''
    contAntes = 0
    i = alfabeto.find(letra)
    while (achaAntes):
        i-=1
        if i <= 0 :
            i = len(alfabeto)
        else:
            if vogais.count(alfabeto[i]) >= 1:
                vogalAntes = alfabeto[i]
                achaAntes = False
        contAntes+=1
        
    achaDepois = True
    vogalDepois = ''
    contDepois = 0
    i = alfabeto.find(letra)
    while (achaDepois):
        i+=1
        if i >= len(alfabeto):
            i = 0
        else:
            if vogais.count(alfabeto[i]) >= 1:
                vogalDepois = alfabeto[i]
                achaDepois = False
        contDepois+=1
     
    if contAntes <= contDepois:
        return vogalAntes
    else:
        return vogalDepois


for letra in palavra:
    if vogais.count(letra) >= 1:
        cifrada = cifrada+letra
    else:
        cifrada = cifrada+letra #add msm consoante
        cifrada = cifrada + achaVogal(alfabeto) #vogal proxima
        
        achou = True
        i = alfabeto.find(letra)
        while (achou):
            i+=1
            if i >= len(alfabeto):
                i = 0
            else:
                if vogais.count(alfabeto[i]) < 1:
                    cifrada = cifrada + alfabeto[i]
                    achou = False
print(cifrada)
