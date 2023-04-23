# Topic: Practice Set--> write a python program to create a class calculator capable of finding square,cube and squareroot of a number.
# Author: Subhrangsu Sinha
# Date: 17.09.2022
class Calculator:
    def __init__(self,num):
        self.number = num
    def find_square(self):
        square = pow(self.number,2)
        print(f'The square of {self.number} is: {square} ')
    def find_cube(self):
        cube = pow(self.number,3)
        print(f'The cube of {self.number} is: {cube} ')
    def find_squareroot(self):
        import math
        sqrt = math.sqrt(self.number)
        print(f'The squareroot of {self.number} is: {sqrt} ')
class Greet:
    @staticmethod
    def greet():
        print('Good Morning Sir,')
greet = Greet()
greet.greet()
num1 = int(input('Enter the number: '))
num = Calculator(num1)
num.find_square()
num.find_cube()
num.find_squareroot()