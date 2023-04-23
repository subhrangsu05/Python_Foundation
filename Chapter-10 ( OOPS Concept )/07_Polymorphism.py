# Topic: Introduction with Polymorphism in Python
# Author: Subhrangsu Sinha
# Date: 20.09.2022

'''
What is Polymorphism?
Polymorphism is not a single word. Poly and Morphism both are different word which are originated from Greek word.
  Poly--> Many
  Morphism--> Form
  Polymorphism --> Many Form
--> Same Object Having Different Behaviour Is Known As Polymorphism.

The best example of polymorphism is you. when,
  1) Your behaviour is peaceful & Respectful when you are meeting to your teacher. --> Your role as a student
  2) Your behaviour is enjoyful when you are meeting to your friends. --> Your role as a friend
  3) Your behaviour might be angry / bargaining when your are buying something.  --> your role as a customer
  4) Your behaviour looks formal when you are attempting some event.  --> your role as a participant

I have discussed about 4 scenarios but in the scenarios, you are the same person just roles and behaviours has changes according to situations.Polymorsphism also works like this. Here, You are object having different behaviour, roles.
'''


'''
Polymorphism has two types:-
  1) Compile time polymorphism / Static Polymorphism / Early binding
  2) Run time polymorphism / Dynamic Polymorphism / Late binding



1) Compile Time Polymorphism:-
   A polymorphism which exists at the time of compilation is called compile time polymorphism. Each & Every work has done between compile time.

   METHOD OVERLOADING is the only way to achieve compile time polymorphism.
   Method Overloading:- Whenever a class contains more than one method having the same name and different types of parameters, this is    called Method Overloading.

2) Run Time Polymorphism:-
   A polymorphism which exists at the time of execution of progress is called Run Time Polymorphism. Compiler doesn't make any impact during Runtime polymorphism.

   METHOD OVERRIDING is the only way to achieve run time polymorphism.
   Method Overriding:- Whenever we are writing methods in Base or Derived classes  in such a way that method name and parameter must be same, It's called Method Overriding. 
'''

#--> Method Overloading:- In Python, Method overloading is not working directly
class Listing:
    def sum(self,a = None, b = None, c = None):
        Sum = 0
        if a != None and b != None and c != None:
            Sum = a+b+c
        else:
            Sum = a+b
        return Sum
list1 = Listing()
a = 10
b = 20
c = 30
print(list1.sum(a,b))
print(list1.sum(a,b,c))


#--> Method Overriding:- 
class A:
    def show(self,a,b):
        print('Hi',a,b)
class B(A):
    def show(self,a,b):
        print('Hello',a,b)
a =A()
b =B()
a.show(1,2)
b.show(3,4)



