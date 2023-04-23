# Topic: Introduction with Class & Object in Python
# Author: Subhrangsu Sinha
# Date: 15.09.2022
'''
What is OOP?
OOP means Object Oriented Programming. OOP contains some specific & mandatory characteristics:-
1) Class
2) Object
3) Abstraction
4) Encapsulation
5) Constructor
6) Inheritance
7) Polymorphism(Compile Time, Run Time)
'''
'''
What is class?
Class is a blueprint for creating object. In Python class name should have to start by Capital letter. 

What is Object?
Object is an instances of class means objects are member of the class. Objects are real life entity who can access the class data.

Suppose, We have class room for class 10. There are 30 people in that class. According to these scenario, we can say that class room is the class, where 'class 10' is the class name and students are the members of the class that means objects of that class.
Only students can sit on the bench, read from books, write on the board in the class as similar as objects / members of a class can access only class data.
'''
# Coding Example 1:-
class Ten:                                                  #--> Here, we have declared the class which name is Ten
    totalNumberOfStudent = 100                              #--> Declare the Class variable
student = Ten()                                             #--> Creating an object of Ten Class, object name is student
student.boys = 60                                           #--> Creating an object variable
student.girls = student.totalNumberOfStudent - student.boys #--> Here, we can see that, we can call class variables out side of the class using by the particular class object
print(f'The count of girl students are {student.girls}')    #--> We can print object variables


# Coding Example 2:- Summation of two numbers
class Sum:
    def Sum(self): #--> self not a any keyword. Self is used to pass the aurguments to the methods automatically. We can write anything instead of self 
        return self.a + self.b
num = Sum()
num.a = 12
num.b = 10
Result = num.Sum() #--> Result is a normal variable
print(f'The sum of {num.a} and {num.b} is {Result}')

'''
We can do these things by Procedural Programming. So, Why we need to do add Object Oriented Programming?
If we're trying build a big project then we need to write lots of code. after a certain time, we can't track the code and break the real Life entity scenario. It will hamper and makes the negative impact on the project.

If we are used OOP instead of traditional approach then we can maintain the project flow, busiess flow and real time entity feature.
'''

# Coding Example 3:- Railway form
class Railwayform:
    formTtype = 'Railway Reservation Form'
    def printdata(self):
        print(f'Name is {self.name}')
        print(f'Name is {self.train}')

application = Railwayform()
application.name = 'Subhrangsu'
application.train = 'Rajdhani Express'
application.printdata()


# Priority Checking:-
'''
Priority first --> Instance /Object Attributes
Priority second --> Class Attributes
'''
class detail:
    salary = 10000
num = detail()
num.salary = 5000
print(num.salary) #--> As we can see, It's printing 5000. That means if class and object has same attributes then object attributes has got much priority 

 