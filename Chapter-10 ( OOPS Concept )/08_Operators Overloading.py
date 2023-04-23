# Topic: Introduction with Oeprators Overloading in Python
# Author: Subhrangsu Sinha
# Date: 20.09.2022

#--> Operators can be overloaded using dunder methods(which methods contains double underscore)
'''
We have some Magic functions:-
__add__() -> overload +
__sub__() -> overload -
__mul__() -> overload *
__truediv__() -> overload /
__floordiv__() -> overlaoad ||
__str__() ->
__len__() -> 

'''
class Number:
    def __init__(self,num):
        self.num = num

    def __add__(self,num2):
        print('Lets Add')
        return self.num + num2.num
n1 = Number(4)
n2 = Number(6)
print(n1 + n2)

# Another example:-
class Test:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def __add__(self,self2):
        num1 = self.num1 + self2.num1
        num2 = self.num2 + self2.num2
        Nu = Test(num1,num2)
        return Nu
n1 = Test(10,20)
n2 = Test(20,30)
n3 = n1+n2
print(n3.num1)
print(n3.num2)

        