import random 
def ordenarLista(elementos):
    lista=[]
    novaLista=[]
    for i in range(elementos):
        numero=random.randint(0, 50)
        lista.append(numero)
    for i in lista:
        if i not in novaLista:
            novaLista.append(i)
    novaLista.sort()
    print(novaLista)

numeros=int(input("Número de elementos desejados: "))
ordenarLista(numeros)