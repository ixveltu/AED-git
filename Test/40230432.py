def dadosEstatistica(lista):
    media= sum(lista)/len(lista)    #calcula a media de temperatura da lista recolhida pelo usuario
    diferencaMaior = 0
    diferenteCidade = 0
    for i in range(len(lista)):    
        diferenca = abs(lista[i] - media)    #verifica a maior diferenca entre as temperaturas e a media calculada
        if diferenca > diferencaMaior:   #verifica se a diferença calculada é a maior 
            diferencaMaior = diferenca   #da o valor à maior diferença à variavel
            diferenteCidade = cidades[i]   #define qual a cidade com maior descrepancia

    print(f"A cidade com a temperatura mais distante da média é {diferenteCidade}")


    
cidades = ['Porto', 'Maia', 'Matosinhos', 'Vila do Conde', 'Póvoa de Varzim', 'Gondomar', 'Gaia']

temperatura= []

for cidade in cidades:
    while True: 
        try: 
            temperaturas=float(input(f"Indique a temperatura na cidade de {cidade} de 0-40ºC: "))
            if temperaturas<40 and temperaturas>0:    #verifica se as temperaturas estao dentro do intervalo desejado
                temperatura.append(temperaturas)   #adiciona a temperatura recolhida a lista
                break
            else:
                raise ValueError   #chama erro caso a temperatura esteja fora do intervalo
        except ValueError:
            print("Temperatura invalida") #printa o erro 
dadosEstatistica(temperatura) #chama a função com a lista de temperaturas
