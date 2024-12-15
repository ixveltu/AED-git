numero=int(input("Indique um número: "))
if 1 <= numero <= 99:
    binario=" "
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero //2
    print(f"{binario}",end=" ")
    print("\b")
else:
    print("O numero que escolheu nao esta no intervalo de 0 a 99, tente novamente")