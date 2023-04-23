# Topic: Practice Set--> Write a python program to find hypotenuse using Pythagorean Theorem
# Author: Subhrangsu Sinha
# Date: 21.08.2022

# Using Arithmetic Operator:-
BASE = int(input('Enter the value of a base of triangle: '))
HEIGHT = int(input('Enter the value of a height of triangle: '))
HYPOTENUSE = ((BASE*BASE)+(HEIGHT*HEIGHT))**0.5
print('The Value of hypotenuse is: ',HYPOTENUSE)

# Using Math Built-in Module:-
import math
BASE = int(input('Enter the value of a base of triangle: '))
HEIGHT = int(input('Enter the value of a height of triangle: '))
HYPOTENUSE = math.sqrt(((pow(BASE,2))+(pow(HEIGHT,2))))
print('The Value of hypotenuse is: ',HYPOTENUSE)