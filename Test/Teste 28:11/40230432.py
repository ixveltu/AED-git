"""
Nome: Emanuel José Fernandes Gomes
Número: 40230432
MacOS
"""


import os
from datetime import datetime

#consultar distâncias
def consultaDistancia():
    #pedir distãncia
    distancia = input("Insira a distância que pretende consultar (5k, 10k, 21k): ")
    #verificar dados pedidos
    if distancia not in ["5k", "10k", "21k"]:
        print("Distância inválida.") 
        return 
        #abrir o ficheiro
    ficheiro = open("Test/Teste 28:11/atividades.txt", "r")
    linhas = ficheiro.readlines()
        #resultados da distância pededida
    print(f"\nConsulta de: {distancia}\n")
    print(f"DataTempo registrado")
    print("-----------------------------------------")
    for linha in linhas:  
        dados = linha.strip().split(",")
        if dados[0] == distancia:
            print(f"{dados[1]}{dados[2]}")
#melhores tempos
def melhoresTempos():
        #Abrir o arquivo
        ficheiro = open("atividades.txt", "r")
        linhas = ficheiro.readlines()
        #dicionário para guardar os melhores tempos
        melhores = {"5k": None, "10k": None, "21k": None}
        for linha in linhas: 
            dados = linha.strip().split(",")
            distancia, data, tempo = dados[0], dados[1], float(dados[1])
            if melhores[distancia] is None or tempo < melhores[distancia][1]:
                melhores[distancia] = (data, tempo)
        #print dos melhores tempos
        print("\nMelhores tempos registrados:")
        for distancia, info in melhores.items():
            if info:
                print(f"{distancia}: {info[1]} minutos em {info[0]}")
            else:
                print(f"{distancia}: Sem registros.")

# funcao para guardar progressos
def progressoPessoal():
        # Abrir o ficheiro
        ficheiro = open("atividades.txt", "r")
        linhas = ficheiro.readlines()
        # dicionario para guardar distâncias
        progresso = {}
        
        for linha in linhas:
            dados = linha.strip().split(",")
            distancia, data = dados[0], dados[1]
            mes = datetime.strptime(data, "%Y-%m-%d").strftime("%Y-%m")  # Formatar ano-mês
            
            if mes not in progresso:
                progresso[mes] = []
            progresso[mes].append(distancia)
        
        # Cria diretorio
        os.mkdir("ficheiros")
        # cria e escreve no ficheiro progresso.txt
        with open("ficheiros/progresso.txt", "w") as arquivo:
            arquivo.write(f"{'Mês':<10}{'Distâncias Percorridas':<30}\n")
            arquivo.write("-" * 40 + "\n")
            for mes, distancias in sorted(progresso.items()):
                arquivo.write(f"{mes:<10}{', '.join(distancias):<30}\n")
        
        print("Arquivo progresso.txt foi criado na subpasta 'ficheiros'.")


while True:
    print("\nMenu:")
    print("1- Consultar por Distância")
    print("2- Consultar melhores tempos")
    print("3- Gravar Progresso")
    print("0- Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        consultaDistancia()
    elif opcao == '2':
        melhoresTempos()
    elif opcao == '3':
        progressoPessoal()
    elif opcao == '0':
        break
    else:
        print("Opção inválida.")

