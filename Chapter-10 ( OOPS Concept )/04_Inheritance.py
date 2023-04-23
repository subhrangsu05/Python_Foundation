# Topic: Introduction with Inheritance in Python
# Author: Subhrangsu Sinha
# Date: 16.09.2022
'''
What is Inheritance?
Inheritance is a biological term it means next generation has taken some characteristics from the parent generation.
Now this concept has been deployed in programming.
We know very well, if we write anything in the class then only class attributes and instances can access those things.

But, supposed we have two class A & Class B. class A & B has individual attributes. Suppose, class B needs to access some attributes of class A. Then, we need to you use Inheritance.
During that time, Class A beacome a parent class and class B become a child class. child class can access parent class attributes but parent class can not access the child class attributes.
Class A--> Parent Class--> Base Class(Programming Term)
Class B--> Child Class--> Derived Class(Programming Term)
'''
class A:
    name ='Subhrangsu'
    Company = 'Google'
class B(A): #--> This is called Inheritance where child B taking the characteristics from parent A
    name = 'SUBHRANGUSU'
    Company = A.Company
    print(f'{name} is a employee and his company name is {Company}')


'''
In Python we have three kinds of Inheritance,
1) Simple Inheritance: One Derived class having one base class
2) Multiple Inheritance: One Derived class having more than one base class
3) Multilevel Inheritance: One Derived class having a Base class as well as the Derived class also be a Base class of another Derived class
'''
# Single Inheritace:-
class A:
    name ='Subhrangsu'
    Company = 'Google'
class B(A):
    Company = A.Company
    print(f'{A.name} is a employee and his company name is {Company}')

# Multiple Inheritace:-
class A:
    name ='Subhrangsu'
class B:
    Company = 'Google'
class c(A,B):
    print(f'{A.name} is a employee and his company name is {B.Company}')

# Multilevel Inheritance:-
class A:
    name ='Subhrangsu'
class B:
    name = A.name
    Company = 'Google'
class c(B):
    print(f'{B.name} is a employee and his company name is {B.Company}')
