sexo = str(input("Indique o seu sexo, F/M "))
idade = int(input("Indique a sua idade "))
if sexo == "F":
  FCM = 226 - idade
  print("FCM = %s" %FCM)
else:  
  FCM = 220 - idade
  print("FCM = %s" %FCM)