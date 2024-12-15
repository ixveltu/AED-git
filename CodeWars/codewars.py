def contagem(x, n):

    multiplos=[]
    for i in range(1, n+1):
        multiplos.append(x*i)
    return multiplos

tabuada=contagem(10, 5)
print(tabuada)