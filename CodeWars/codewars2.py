words=["segunda", "terça", "quarta", "quinta", "sexta"]

frase=""

for i in range(len(words)):
    if i < len(words)-1:
        frase+= words[i] +" "
    else:
        frase+= words[i] + "."

print(frase)