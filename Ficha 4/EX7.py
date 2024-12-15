def pluviosidade(mes):
    pluviosidadeMensal.sort()
    pluviosidadeMensal.reverse()
    for i in range (len(meses)):
        print("A pluviosidade no mês {:s}, é de {:n}" .format(meses[i], pluviosidadeMensal[i]))
    



pluviosidadeMensal=[]
meses=["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novebro", "Dezembro"]
for i in range (len(meses)):
    pluviosidades=int(input("Indique a pluviosidade no mes {0}: " .format(meses[i])))
    pluviosidadeMensal.append(pluviosidades)
pluviosidade(pluviosidadeMensal)