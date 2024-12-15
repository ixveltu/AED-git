sexo = str(input("Indique o seu sexo, F ou M: "))
altura = int(input("Indique a sua altura em cm: "))
if sexo == "F" |"f" :
 k = 2
 pesoIdeal = (altura-100) - (altura-150)/k
 print("O seu peso ideal é {:.2f} Kg" .format(pesoIdeal))
else: 
 k = 4
pesoIdeal = (altura-100) - (altura-150)/k
print("O seu peso ideal é {:.2f} Kg" .format(pesoIdeal))