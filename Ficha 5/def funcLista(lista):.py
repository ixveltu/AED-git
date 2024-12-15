def func(lista, num) : 
    if num not in lista:
        return num
    else:
        return -1
    
import random
lista = [1,3,3,5,5,7,7,8,9]
print(func(lista, random. randint (0,10)))