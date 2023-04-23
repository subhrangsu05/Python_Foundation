# Topic: Introduction with Static Method & Constructor in Python
# Author: Subhrangsu Sinha
# Date: 16.09.2022

'''
What is Static Method?
Static Method can be called directly without creating an instance variables.
'''
class Abc:
    @staticmethod # --> This is called decorator which helps to modify a function
    def greet():
        print('Good Morning')
num = Abc()
num.greet()
# --> see, we haven't created any instance variables but we can access the function

'''
What is Constructor?
Constructor is a special type of method which helps to initialise the objects in the class.
Advantages of Constructor over normal methods:-
1) It helps to initialise the object in to the variable, which variable we can in the entire program if permission has been given.
2) Constructor automatically is called automatically when the class has been called. we don't need to write extra line to call it.
3) In python program, constructor should be define by __init__ ()
4) It takes self aurgument as well as normal aurguments
'''
class Xyz:
    def __init__(self,first,second): #--> Costructor define
        a = first 
        b = second 
    def sum(self):
        return a + b
b = 12
a = 10
number = Xyz(a,b)
print(f'The Summation will be {number.sum()}')

#--> See, we have't called the constructor function but it's working automatically.