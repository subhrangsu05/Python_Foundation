# Topic: Introduction with Functions in Python
# Author: Subhrangsu Sinha
# Date: 06.09.2022
'''
What is Function?
A group of statement which is performing some particular task. Suppose we need to perform a particular task in several times in a program. Then we can call function instead of copyied same oepartion line.

Features:-
1) Function can call from anywheare in a program
2) It should be return some thing
3) what ever we are used in function, those are existing only in the function 
'''

# Suppose I want to get the marks percentage of several student. Then we have to write that oepration for several students. Instead of this, we can write the opeartion in the function & we can call that function from anywheare in the code. Let's dig in to it...

def percentage(points):  #--> def function_name(parameter)
    percent = sum(points)*(1/5)
    return int(percent)   #-->  return value by function
marks = [10,20,30,40]
result = percentage(marks) #--> function_name(aurgument)
print(f'The toatal percentage will be: {result}')


# Suppose I want greet those persons who's name started by 'S':-
def greeting(list1):
    greet = 'Good Morning'
    for i in range(len(list1)):
        if list1[i].startswith('S') or list1[i].startswith('s'):
            print (greet+' '+list1[i])
list1 = []
for i in range(3):
    name = input(f'Enter the name {i+1}: ')
    list1.append(name)
greeting(list1)
