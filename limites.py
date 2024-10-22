i=0
soma=0
limiteInferior = int(input("Indique o limite inferior: "))
limiteSuperior = int(input("Indique o limite superior: "))
#if limiteSuperior<limiteInferior:
   #print("Insira novos limites.")
#exit(0)
for i in range(limiteInferior, limiteSuperior+1):
    if i % 2 == 0:
        soma+=i
print("A soma de todos os números pares entre {:n} e {:n} é de {:n}." .format(limiteInferior,limiteSuperior,soma))