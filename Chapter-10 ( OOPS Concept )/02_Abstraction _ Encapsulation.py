# Topic: Introduction with Abstraction & Encapsulation in Python
# Author: Subhrangsu Sinha
# Date: 16.09.2022

'''
What is Abstraction / Data Abstraction?
Astraction word is used to hide the unnecessary things to the user.

Suppose, we all have a calculator. User given the number and perform the mathematical operation like add, sub, mul,div, mod. But, user cannnot see the implemented code behind the operation, and the major thing is user doesn't need to see the code. user just click on the button and perform the operation.
This is called abstraction.

Sometimes, we're using lots of built-in modules and functions. we don't need to know the code in those methods.Instead of this, we're just passing aurguments and we're getting the result.
This is called abstraction.

When we're using smart phone and some how we need to take photo. what will be happend?
we just click on camera app and click on camera button to take photo. but, we don't know the operation behind the all of theses and we don't need to know.
This is called abstraction.

Hide the all unnecessary things to the user. 
'''
class Listing:
    def sum(self):
        Sum = 0
        for i in range(len(self.List1)):
            Sum = Sum + self.List1[i]
        return Sum
list1 = Listing()
list1.List1 = [1,2,3,4,5,6]
result = list1.sum() #--> Layer of Abstraction
print(result)

'''
Users can see only from line no 27 - line no 30. Users doesn't need to know about the behind operation in the class. Users just call function and pass the aurguments
'''


'''
What is Encpsulation?
En(In the) + Capsulation(Capsule) => we have seen capsule as a medicine. There are mixtured of lots medicines like:- zinc, protein, vitamin, calcium etc, mixed up and wrap it in to a particular capsule for particular dieses.

Same Way:-
In the programming, we have lots of functions, methods, loops for a particular operation. We can wrap these in to a particular class according to oepartions. This is called encapsulation.
'''

# Suppose we're filling Railway form:-
class Railway: #--> This class is similar as a capsule where only trains & passangers details are stored
    class Railway_Application: #--> This class is similar as a capsule where only train details are stored
        train_name = 'Rajdhani Express'
        def detail(self):
            if self.destination == 'Delhi':
                print(f'{self.train_name} is available')
            else: 
                print('No Train is available')
    class Passanger_Details:  #--> This class is similar as a capsule where only passanger details are stored
        def passanger_detail(self):
            print(f'''The first name of passanger is {self.first_name}\n The last name of passanger is {self.last_name}\n The total passangers are {self.member}''')
    app = Railway_Application()
    app.name = 'Subhrangsu'
    app.destination = 'Delhi'
    app.detail()
    passanger = Passanger_Details()
    passanger.first_name = app.name
    passanger.last_name = 'Sinha'
    passanger.member = 5
    passanger.passanger_detail()