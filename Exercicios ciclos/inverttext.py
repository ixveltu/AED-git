"""frase=str(input("Indique uma frase: "))
print(frase [::-1])"""


"""frase=str(input("Indique uma frase: "))
vogais=0
espaços=0
caracteres=0
for i in range(len(frase)):
    caracteres=len(frase)-espaços
    espaços=frase.count(" ")
    vogais=frase.count("a")+frase.count("e")+frase.count("i")+frase.count("o")+frase.count("u")
    vogais=frase.count("A")+frase.count("E")+frase.count("I")+frase.count("O")+frase.count("U")
print("A frase tem {:n} caracteres".format(caracteres))
print("A frase tem {:n} espaços".format(espaços))
print("A frase tem {:n} vogais".format(vogais))"""


"""palavra=str(input("Indique uma palavra: "))
palavra2=palavra[::-1]
if palavra2==palavra:
    print(f"{palavra} é capicua")
elif palavra2 != palavra:
    print(f"{palavra} nao é capicua")"""

"""def capicua(palavra):
    palavra2=palavra[::-1]
    if palavra2==palavra:
        return "True"
    elif palavra2 !=palavra:
        return "False"
    
palavra=str(input("Indique uma palavra: "))
qualquer=capicua(palavra)
print(qualquer)"""


"""def fraseCorrigida(frase):
    fraseCorrigida= " " .join(frase.split())
    print(fraseCorrigida)

frase=str(input("Indique uma frase: "))
fraseCorrigida(frase)"""


"""def shortName():
    nomeCorrigido= nome.split()
    print(nomeCorrigido[0], nomeCorrigido[len(nomeCorrigido)-1])
nome=str(input("Nome: "))
shortName()"""


"""def shortName():
    nomeCorrigido= nome.split()
    primeiroNome=nomeCorrigido[0]
    ultimoNome=nomeCorrigido[len(nomeCorrigido)-1]
    abreviaçoes=[f"{p[0]}." for p in nomeCorrigido[1:-1] if p[0].isupper()]
    nomeAbreviado=f"{primeiroNome} {' '.join(abreviaçoes)} {ultimoNome}".strip()
    print(nomeAbreviado)
nome=str(input("Nome: "))
shortName()"""

def contaOccurs (texto):
    numero = texto. count ("AED")
    i=0
    pos=0
    while i<numero:
        local= texto. find ("AED", pos)
        print (local)
        pos=local+1
        i+=1

texto = "Em AED: este, em AED, o primeiro exercicio de progresso de AED'
contaOccurs(texto)