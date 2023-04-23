# Topic: Practice Set--> Write a python program to calculate the factorial of the given number using for loop
# Author: Subhrangsu Sinha
# Date: 04.09.2022
num = int(input("Enter the number: "))
fact = 1
i = 1
for i in range(num):
    fact = fact * i
print(f'The factorial of {num} is {fact}')