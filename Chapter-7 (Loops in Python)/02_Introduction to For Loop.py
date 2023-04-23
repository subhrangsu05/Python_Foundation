# Topic: Introduction with For Loop in Python
# Author: Subhrangsu Sinha
# Date: 03.09.2022

'''
range():-
suppose we need to write range(n), that means loop will be iterated upto (n-1) times.
we have to put integer value in the range function.
'''
# suppose I want to print 1-50 using For Loop:-
i = 0
for i in range (50):
    print(i+1)

# Suppose we have a list, we want to print a list:-
list1 = ['Apple','Mango','Grapes','Water Melon','Straw berry']
for item in list1:
    print(item)

# Another Approach:-
for item in range(len(list1)):
    print(list1[item])

# we want store some data in list  using loop:-
i = 1
list2=[]
for i in range(10):
    list2.append(i+1)
    i+=1
print(list2)

# we want store some data in 2-D list  using loop:-
list3=[]
for i in range(3):
    print(i)
    for j in range(3):
        print(j)
        user_first = input('Enter your first name: ')
        user_last = input('Enter your last name: ')
        i1 = [user_first,user_last]
        list3.append(i1)
print(list3)
print(list3[2][1])

### EXTRA ACTIVITIES OF FOR LOOP:-

for i in range(1,8,2): #range(starting index, stop index, skip index)
    print(i)

for i in range(10):
    print(i)
else:
    print('This is inside of FOR')

#Break:-
for i in range(10):
    print(i)
    if(i==5):
        break
else:
    print('This is inside of FOR')

#Continue:-
for i in range(10):
    print(i)
    if(i==5):
        continue
else:
    print('This is inside of FOR')

#pass:

i=4
if i>0:
    pass
print('Subhrangsu')