"""
Sum all the numbers of a given array ( cq. list ), except the highest
and the lowest element ( by value, not by index! ).
The highest or lowest element respectively is a single element at each 
edge, even if there are more than one with the same value.
"""
numbers=[10, 20, 40, 50, 60, 70, 80]
def soma(numbers):
    numeroMenor=min(numbers)
    numeroMaior=max(numbers)
    somatorio=0
    for i in range(len(numbers)):
        somatorio+=numbers[i]
    somatorio=numeroMaior-numeroMenor
    print(somatorio)
    print(numeroMenor)
    print(numeroMaior)
soma(numbers)