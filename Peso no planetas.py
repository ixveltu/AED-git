print(""" Planetas 
         1 -Mercurio 
         2 - Venus
         3 - Marte
         4 - Júpiter 
         5 - Saturno
         6 - Urano""")
peso=float(input("Indique o seu peso em Kilogramas: "))
planeta=int(input("Indique o código do seu planeta: "))
match planeta:  
    case 1:
        gravidade = 0.37
        print("O seu peso em Mercúrio é {:.2f}Kg" .format(pesoPlaneta))
    case 2: 
        gravidade= 0.90
        print("O seu peso em Venus é {:.2f}Kg" .format(pesoPlaneta))
    case 3:
        gravidade = 0.37
        print("O seu peso em Marte é {:.2f}Kg" .format(pesoPlaneta))
    case 4: 
        gravidade = 2.53
        print("O seu peso em Júpiter é {:.2f}Kg" .format(pesoPlaneta))
    case 5: 
        gravidade = 1.06
        print("O seu peso em Saturno é {:.2f}Kg" .format(pesoPlaneta))
    case 6: 
        gravidade = 0.91

pesoPlaneta = peso * gravidade / 0.98
print("O seu peso em Urano é {:.2f}Kg" .format(pesoPlaneta))