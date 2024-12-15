meses=["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novebro", "Dezembro"]
def faturacaoMensal(faturacao):
    def mediaFaturacao(faturacao):
        faturacaoMedia=sum(faturacao)/len(faturacao)
        print("A faturação media é {:n}" .format(faturacaoMedia))
    def maximaFaturacao(faturacao):
        maxFaturacao=max(faturacao)
        posMaior = faturacao.index(maxFaturacao)
        print("O mês com maior faturação é {:s} com {:n}€." .format(meses[posMaior], maxFaturacao))
    def minimaFaturacao(faturacao):
        minFaturacao=min(faturacao)
        posMenor = faturacao.index(minFaturacao)
        print("O mês com maior faturação é {:s} com {:n}€." .format(meses[posMenor], minFaturacao))
    mediaFaturacao(faturacao)
    maximaFaturacao(faturacao)
    minimaFaturacao(faturacao)

faturacaoLista=[]
for i in range(12):
    faturacaoLista.append(int(input("Faturação no mês de {}: ".format(meses[i]))))
faturacaoMensal(faturacaoLista)