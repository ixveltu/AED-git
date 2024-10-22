total = 0
maior = 0
i = 0
while i < 10:
 numero = int(input("Idique o {:n}º numero: ".format(i+1)))
 if numero > 20:
   print("Intruduza um numero menor que vinte.")
   continue #se numero > 20 volta a pedir
 if numero > numero:
   maior = numero    #NAO FUNCIONA
 total = total + numero 
 i = i + 1    
media = total/10
print("A media é {:n}".format(media))
print("O número maior é {:n}" .format(maior))