import random
i=0
tentativas=1
numero= random.randint(1,50) #gera um numero random de 1,50 incluindo os limites
guess=int(input("Indique um número de entre 1 e 50 (incluindo os limites): "))
while guess!=numero and tentativas<10: #enquanto as tentativas forem menor que 10 ou guess dif do numero
 if guess>numero:
  print("O número é menor")
 elif guess<numero:
  print("O número é maior")
 guess=int(input("Indique um número de entre 1 e 50 (incluindo os limites): "))
 tentativas+=1
if guess==numero:
 print("Parabéns acertou em {:n} tentativas!".format(tentativas))
else:
 print("Esgotou as 10 tentativas") 