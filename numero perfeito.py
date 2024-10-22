soma=0
numero=int(input("Indique um número: "))
for i in range(1,numero):
    if numero % i == 0:
        soma+=i
print(soma)   
if soma == numero:
    print(f"{numero} é um numero perfeito.", end="") 
else:
    print(f"O {numero} não é perfeito.")
print("\b\b")
