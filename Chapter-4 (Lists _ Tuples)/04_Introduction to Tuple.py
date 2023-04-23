# Topic: Introduction with Tuple in Python
# Author: Subhrangsu Sinha
# Date: 23.08.2022
'''Tuple is a container which can store a set of values of any data types.
If you know the C,C++, JAVA then I can say Tuple is one kind of Array. But the major difference between array and Tuple is,
Tuple can store different kind of datatypes while array can store only same kind of datatypes.

In python, tuple looks similar to the list but tuple is not the accurate list

Features of Tuples:-
Tuple should be written between first brackets
2) It always follows the sequential order
3) Each value stored in a particular index. Index is started by 0.
4) Tuple values are immutable  )---> Very Important point<---(
5) Tuple can be 1D, 2D, 3D.... 
6) Tuple also can be Empty,single,multiple.

'''
# 1D Tuple:-
# Multiple Element in the Tuple
tuple1 = (10,20,'Mango','Apple',52.48)
print(tuple1)
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])
print(tuple1[4])

# tuple[3] = 'Subhrangsu'  -->It throws error, we can;t change the tuples value
# Empty Tuple:-
Empty_Tuple = ()

# Single Element in the Tuple:-
singleElementTuple = (1,) #--> should have to add comma(,)


# 2D Tuple:-

tuple2=(10,20,('Mango','Apple',100),30,40.65)
print(tuple2)
print(tuple2[0])
print(tuple2[1])
print(tuple2[2]) 
print(tuple2[3])
print(tuple2[4])

# If we want to access particular a 2D element:-
print(tuple2[2][1]) #--> It will print Apple


# 3D Tuple:-

tuple3=(10,20,('I','hate',('C','JAVA','PYTHON','ANGULAR','HTML','CSS',True)),30,40.65)
print(tuple3)
print(tuple3[0])
print(tuple3[1])
print(tuple3[2]) 
print(tuple3[3])
print(tuple3[4])


# If we want to access particular a 2D element:-
print(tuple3[2])

# If we want to access particular a 3D element:-
print(tuple3[2][2])

