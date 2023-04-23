# Topic: Introduction with Recursion Functions in Python
# Author: Subhrangsu Sinha
# Date: 09.09.2022
'''
What is Recursion Function?
Recursion is a one kind of function which calls itself. It's used to directly use mathematical formula as a function.
We can say, recursion makes a own personal mathematical loop. 
'''
# If we want to print normal factorial with recursion:-
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        fact = num * factorial(num-1) # This is a recursion function
        return fact
num = int(input("Enter the number: "))
result = factorial(num)
print(f"{num} factorial is {result}")