import random
def matrizAleatoria(lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(lista[i][j], end=" ")
        print()

def matrizTransposta(lista):
    for z in range(len(lista)):
        for x in range(len(lista[z])):
            print(lista[x][z], end=" ")
        print()

def valorMaior(lista):
    maiorValor = max(lista[i])
    print(f"O maior valor da lista é {maiorValor}")

matriz= []
for i in range(3):
    matriz.append([])
    for j in range(3):
        numero = random.randint(0,100)
        if numero != matriz:
            matriz[i].append(numero)
while True:
    resposta=(input("""           MENU
        1 - Inicializar matriz
        2 - Matriz transposta
        3 - Maior valor
        0 - Sair
        """))

    if resposta=="1":
        matrizAleatoria(matriz)
    if resposta=="2":
        matrizTransposta(matriz)
    if resposta=="3":
        valorMaior(matriz)