# Topic: Introduction with While Loop in Python
# Author: Subhrangsu Sinha
# Date: 26.08.2022

'''
Which is called perfect program?
A perfect program should have to follow some points--
1) It takes minimum storage in memory
2) we have to reduce the line of code in the program
3) Maintain the time complexity:- the program's executing time should not be very longer
'''
'''
Why we are using loops?
1) Reduce the line of code
2) Maintain the time complexity
3) Maintain the storage 
4) Programs follows the user flexibility
'''
# Primarily, we have two types of in python: While and For
# Let's see how to use while loop:-

# suppose I want to print 0-50 but I don't want to use 50 print statement:-
i=1
while i <= 50: 
    print(i)
    i+=1 #--> it increases the value of i, for next iteration. i = i+1
# Once the condition will false then the loop will be terminated 

# Suppose we have a list, we want to print a list:-
list1 = ['Apple','Mango','Grapes','Water Melon','Straw berry']
i= 0
while i<len(list1):
    print(list1[i],'\n')
    i=i+1 


# we want store some data in list  using loop
i = 1
list2=[]
while i<=10:
    list2.append(i)
    i+=1
print(list2)

# we want store some data in 2-D list  using loop
i=0
list3=[]
while i<3:
    print(i)
    j=1
    while j<=3:
        print(j)
        user_first = input('Enter your first name: ')
        user_last = input('Enter your last name: ')
        i1 = [user_first,user_last]
        list3.append(i1)
        j+=1
    i+=1
print(list3)
print(list3[0][0])

