numero=int(input("Indique um número: "))
if numero < 0:
    print("Indique um número positivo")
else:
    if numero<=1:
        print(f"O {numero} não é primo.")
    else:
        primo = True #começa o else por assumir que o num sera primo
        for i in range(2,int(numero**0.5)+1): #se for divisivel por algum numero neste intervalo nao é primo
            if numero % i ==0:
             primo = False #se for divisivel no intervalo nao é primo
            break
        if primo:
            print(f"O número {numero} é primo.")
        else:
            print(f"O número {numero} não é primo.")



