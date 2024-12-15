i=0
numero=int(input("Digite o número de digitos pretendidos: "))
while i < numero:
    numeros=int(input("Número: "))
    i+=1
    if numeros % 2 == 0:
        par=True
    else:
        par=False
if par==True:
    print(f"Os numeros {numeros}  sao par.",end =" ")
elif par==False:
    print(f"Os numeros {numeros}  sao impar.", end=" ")