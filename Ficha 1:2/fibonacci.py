numeroFibonacci=int(input("Indique o numero da sequencia que deseja: "))
if numeroFibonacci <=0:
    print("Por favor indique um número positivo.")
else:
    t1=0 #define o termo 1 como 0 (como dito na sequencia)
    t2=1 #define o termo 2 como 1 (como dito na sequencia)
    print(f"Os {numeroFibonacci} primeiros termos da sequência sao ", end=" ")
    for i in range(numeroFibonacci):
        if i==0:
            print(t1, end=", ")
        elif i==1:
            print(t2, end=", ")
        else:
            t_atual= t1 + t2 #define o 3 termo da sequencia fazendo a soma dos dois anteriores
            print(t_atual, end=", ")
            t1, t2=t2, t_atual #define o t1 como o antigo t2 e o t2 como o resultado da soma dos termos anteriores

