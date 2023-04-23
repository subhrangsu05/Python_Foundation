# Topic: Introduction with LIST in Python
# Author: Subhrangsu Sinha
# Date: 23.08.2022
'''List is a container which can store a set of values of any data types.
If you know the C,C++, JAVA then I can say list is one kind of Array. But the major difference between array and list is,
list can store different kind of datatypes while array can store only same kind of datatypes.

Features of Lists:-
1) List should be written between third brackets
2) It always follows the sequential order
3) Each value stored in a particular index. Index is started by 0.
4) List values are mutable
5) List can be 1D, 2D, 3D.... 

'''

# 1D List:-
list1=[10,20,'Mango','Apple',52.48]
print(list1)
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])

# We can change the value using index:--
list1[3]='Grapes'
print(list1)

# 2D List:-

list2=[10,20,['Mango','Apple',100],30,40.65]
print(list2)
print(list2[0])
print(list2[1])
print(list2[2]) 
print(list2[3])
print(list2[4])

# If we want to access particular a 2D element:-
print(list2[2][1]) #--> It will print Apple

# we can change the value of 2D element:-
list2[2][1] = 'Orange'
print(list2)

# 3D List:-

list3=[10,20,['I','hate',['C','JAVA','PYTHON','ANGULAR','HTML','CSS',True]],30,40.65]
print(list3)
print(list3[0])
print(list3[1])
print(list3[2]) 
print(list3[3])
print(list3[4])


# If we want to access particular a 2D element:-
print(list3[2])

# we can change the value of 2D element:-
list3[2][1] = 'love'
print(list3)

# If we want to access particular a 3D element:-
print(list3[2][2])

# we can change the value of 3D element:-
list3[2][2][3] = 'REACT'
list3[2][2][6] = False
print(list3)
