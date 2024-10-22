i = 0
fatorial = 1
numero=int(input("Indique um número: "))
for i in range(1, numero+1):
    fatorial=fatorial*i
print("Fatorial de {:n} é {:n}".format(numero, fatorial))