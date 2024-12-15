def aboveAverage(numeros):
    numerosMaiores=[]
    media=sum(numeros)/(len(numeros))
    for numero in numeros:
        if numero > media:
            numerosMaiores.append(numero)
    print(numerosMaiores)
        
i=0
numeros=[]
while i < 10:
    numeros.append(input("Numeros: "))
    i+=1
aboveAverage(numeros)