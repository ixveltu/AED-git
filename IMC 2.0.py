altura = float(input("Indique a sua altura em metros "))
peso = float(input("Indique o seu peso em kilogramas "))
IMC = peso/(altura*altura)
print("O seu IMC é {:.2f}" .format(IMC))
if IMC < 18.5:
 print("Você está a baixo do peso.")  
if 24.9>IMC>18.5:
 print("Você está com o peso normal.")
if 25<IMC<29.9:
 print("Você está com excesso de peso:")
if 30<IMC<34.9:
 print("Você está com obesidade grau I.")
if 35<IMC<39.9:
 print("Você está com obesidade grau II.")
if IMC >= 40:
 print("Você está com obesidade morbida.")