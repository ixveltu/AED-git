"""
Write a function that takes an array of numbers and returns 
the sum of the numbers. The numbers can be negative or non-integer.
If the array does not contain any numbers then you should return 0.
"""
numbers=[10, 20, 30, 40, -30, -20, -40, 0.1]

soma=0
for i in range(len(numbers)):
    soma+=numbers[i]
print(soma)