i=0
maior=0
segundoMaior=0
numero=int(input("Quantos números deseja ler: "))
while i < numero:
    numeros=int(input("Numero: "))
    i+=1
    if numeros > maior: 
        maior = numeros
    else: 
        segundoMaior < numeros and numeros != maior #NAO FUNCIONA

print(f"O segundo maior número da lista é {segundoMaior}.",)
print("\b")

