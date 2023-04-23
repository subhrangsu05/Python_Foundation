# Topic: Methods of the LIST in Python
# Author: Subhrangsu Sinha
# Date: 24.08.2022
list1 = [100,3,1203,2,5,67,45]

# If we want to sort the value of a list:-
list1.sort()
print(list1)

# If we want to reverse the value of the list:-
list1.reverse()
print(list1)

# If we want to add any value at end of the list:-
list1.append('Subhrangsu')
print(list1)

# If we want to insert a data at any particular position:-
list1.insert(3,4.34)  #--> list-name.insert(index position,value)
print(list1)

# If we want to delete a value from list using index:-
list1.pop(1)
print(list1)

# If we want to remove a value from list using that value:-
list1.remove('Subhrangsu')
print(list1) 