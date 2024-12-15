def matrizInvertida(conteudos):
    matriz=[]
    col = 3
    lin = 3
    for i in range(lin):
        matriz.append([ ])
        for j in range(col):
            matriz.append(conteudos)
    for i in range(lin):
        for x in range(len(matriz[i])):
            print(matriz[i][x], end="")

numeros = (1,2,3,4,5,6,7,8,9)
# i=0
# while i < 9:
#     numeros=int(input("Numeros: "))
#     i+=1
matrizInvertida(numeros)
