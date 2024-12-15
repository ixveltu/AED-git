def maior(faturacao):
    maiorFaturacao=max(faturacaoMensal)
    posMaior=faturacaoMensal.index(maiorFaturacao)
    print("O mês de maior faturação é {}".format(meses[posMaior]))
def menor(faturacao):
    menorFaturacao=min(faturacaoMensal)
    posMenor=faturacaoMensal.index(menorFaturacao)
    print("O mês de menor faturação é {}".format(meses[posMenor]))
def media(faturacao):
    mediaFaturacao=sum(faturacaoMensal)/len(faturacaoMensal)
    print("O valor médio de faturação é {:}€" .format(mediaFaturacao))

faturacaoMensal=[]
meses=["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novebro", "Dezembro"]
for i in range (len(meses)):
    faturacao1=input("Faturação do mês de {0}: ".format(meses[i]))
    faturacaoMensal.append(faturacao1)
maior(faturacaoMensal)
menor(faturacaoMensal)
media(faturacaoMensal)
