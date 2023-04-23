# Topic: Introduction with IF-Else Statement in Python
# Author: Subhrangsu Sinha
# Date: 26.08.2022

# Simple If-Else statement:-
'''Suppose user given a number, we need to find out that the number is greater than 400 or not'''

no1 = int(input('Pls enter the number: '))
if no1<400:
    print(f'{no1} is lesser than 400')
else:
    print(f'{no1} is greater than 400')



# Multiple Condition If-else Statement:-
'''We need to find out a boy is eligible to drive or not'''
age = int(input('Enter Your Age: '))
if age > 18 and age < 60:
    print("You can drive")
else:
    print("You can't drive")

# Else-If Statement:-
'''We need to find generation according to age'''
age = int(input('Enter Your Age: '))
if age >0 and age<=3:
    print("You're a baby")
elif age>3 and age<=10:
    print("You're a child")
elif age>10 and age<=18:
    print("You're a tenager")
elif age>18 and age<=35:
    print("You're a Adult")
elif age>35 and age<=60:
    print("You're a senior Person")
elif age>60 and age<=100:
    print("You're Senior Citizen")
else:
    print("You're living in extra time")


# Complex If-Else Statement:-

'''Suppose we have some fruits(Banana,Apple,Mango).Use IF-ELse condition on this'''
f_name = input('Enter the fruit name: ')
if (f_name.startswith('B') or f_name.startswith('b')) and (f_name.endswith('A') or f_name.endswith('a')):
    print("The Fruit is BANANA")
elif (f_name.startswith('A') or f_name.startswith('a')) and (f_name.endswith('E') or f_name.endswith('e')):
    print("The Fruit is APPLE")
elif (f_name.startswith('M') or f_name.startswith('m')) and (f_name.endswith('M') or f_name.endswith('m')):
    print("The Fruit is Mango")
else:
    print("NOT IN THE LIST")

