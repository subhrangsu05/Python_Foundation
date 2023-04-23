# Topic: Type Casting in Python
# Author: Subhrangsu Sinha
# Date: 20.08.2022

# before TypeCasting
age = 25
name = 'Subhrangsu'
number = '420'
weight = 52.97
print(type(age))
print(type(name))
print(type(number))
print(type(weight))

# After TypeCasting
age = str(age)
# name = int(name) --> It throws error because string can not directly change to integer
number = int(number)
weight = int(weight)
print(type(age))
print(type(name))
print(type(number))
print(type(weight))