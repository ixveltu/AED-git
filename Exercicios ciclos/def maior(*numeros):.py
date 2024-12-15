def maior(*numeros):
    """
    Recebe um conjunto de numeros e informa o maior destes
    Args: numeros
    """
    maior=0
    for i in range(len(numeros)):
        if numeros[i] > maior:
            maior = numeros[i]
    return(maior)

#numb=int(input("Indique o numero de termos que deseja inserir: "))
#for i in range(1 ,numb+1):
    #numeros=int(input("Numero {:n}º: " .format(i)))

print(maior(10, 20, 30))