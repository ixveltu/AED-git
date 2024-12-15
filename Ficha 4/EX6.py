def searchNumbers(numeros, pesquisa):
    pesquisaLista=[]
    for i in range(len(numeros)):
        if numeros[i]==pesquisa:
            pesquisaLista.append(i+1)
    print(f"O número que procura encontra-se na posiçao {pesquisaLista}")


numerosLista=[]
for i in range(10):
    numerosLista.append(int(input("Numeros: ")))
numeroDesejado=int(input("Pesquisa: "))
searchNumbers(numerosLista, numeroDesejado)
