def positiveList(notas):
    pontuacoesPositivas=[]
    nomesPositivos=[]
    for i in range(len(notas)):
        if notas[i] >= 10:
            pontuacoesPositivas.append(notas[i])
            nomesPositivos.append(nomesLista[i])
    print(pontuacoesPositivas)
    print(nomesPositivos)

        
pontuacoes=[]
nomesLista=[]
i=0
while len(pontuacoes)<10:
    nome=str(input("Nome: "))
    pontuacoes1=int(input("Indique as pontuações: "))
    try: 
        if pontuacoes1<0 or pontuacoes1>20:
            raise ValueError
    except ValueError:
        print("A pontuação não é valida.")
    else:
        pontuacoes.append(pontuacoes1)
        nomesLista.append(nome)
positiveList(pontuacoes)