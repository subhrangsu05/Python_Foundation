# Topic: Practice Set--> write a python program to create a class Complex to represent complex numbers , along with overloaded operators + and * which adds and multiplies them
# Author: Subhrangsu Sinha
# Date: 20.09.2022


class Complex:
    def __init__(self,r,i):
        self.real = r
        self.imaginary = i

    def __add__(self,self2):
        return Complex(self.real + self2.real,self.imaginary + self2.imaginary)

    def __mul__(self,self2):
        mul_real = self.real * self2.real - self.imaginary * self2.imaginary
        mul_imagiary  = self.real * self2.imaginary + self.imaginary * self2.real
        return Complex(mul_real,mul_imagiary)

    def __str__(self):
        return f'{self.real} + {self.imaginary}i'
c1 = Complex(3,2)
c2 = Complex(1,7)
print(c1+c2)
print(c1*c2) 
