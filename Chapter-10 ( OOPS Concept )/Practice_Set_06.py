# Topic: Practice Set--> write a python program to create a class pets from a class Animals and further create a class Dog from pets. Add a method bark to class Dog.
# Author: Subhrangsu Sinha
# Date: 20.09.2022

class Animals:
    AnimalType = 'Mammal'
class Pets(Animals):
    colour = 'white'
class Dogs(Pets):
    @staticmethod
    def bark():
        return 'The Dog is barking'
d = Dogs()
print(d.bark())

#--> We're using MultiLevel Inheritance
