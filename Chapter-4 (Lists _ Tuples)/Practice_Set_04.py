# Topic: Practice Set--> Write a python program to sum a list with 4 numbers.
# Author: Subhrangsu Sinha
# Date: 25.08.2022

n1,n2,n3,n4 = int(input('Number 1 : ')),int(input('Number 2 : ')),int(input('Number 3 : ')),int(input('Number 4 : ')),
Number = [n1,n2,n3,n4]
print(Number)
# Traditional Approach:- 
print(Number[0]+Number[1]+Number[2]+Number[3])
# Modern Approach:-
print(sum(Number)) # Python has inbuilt sum() method