def estacionarVeiculo(lista):
    for i in range(len(parque)):    
        if 0 in parque[i]:
            lugar = parque[i].index(0)
            print(lugar + 1, i + 1)
            parque[i][lugar] = 1
            print(lista)
            break
        
def tirarVeiculo(lista):
    fila = int(input("Indique a fila onde o seu veículo se encontra: "))
    lugar = int(input("Indique o número onde o seu veículo se encontra: "))
    if lista[fila-1][lugar-1] == 1:
        lista[fila-1][lugar-1] = 0
        print(lista)
    
def estadoParque(lista):
    ocupado = 0
    for i in range(len(lista)):    
        for j in range(len(lista[i])):
            if lista[i][j] == 1:
                ocupado+=1
    livre=15-ocupado
    print(f"Lugares ocupados {ocupado}")
    print(f"Lugares livres {livre}")

parque=[]
for i in range(3):
    parque.append([])
    for j in range(5):
        parque[i].append(0)

while True:
    resposta=(input("""           MENU
        1 - Entrada de veículo
        2 - Saída de carro
        3 - Estado de parque
        0 - Sair
        """))

    if resposta == "1":
        estacionarVeiculo(parque)
    elif "2":
        tirarVeiculo(parque)
    elif "3":
        estadoParque(parque)
    elif "0":
        exit
    else:
        print("Erro, opção inválida.")