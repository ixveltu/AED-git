meses=["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novebro", "Dezembro"]
def pluviosidade(listaOrdenada):
    listaOrdenada.sort()
    listaOrdenada.reverse()
    print(listaOrdenada)


pluviosidadeLista=[10,20,30,40,50,60,70,80,90,100,110,120]
# pluviosidadeLista=[]
# i=0
# while i < 12:
#     pluviosidade.append(str(input("Pluviosidade no mês de {}".format(meses[i]))))
#     i+=1
pluviosidade(pluviosidadeLista)