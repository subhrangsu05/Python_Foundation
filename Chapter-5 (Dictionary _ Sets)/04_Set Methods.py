# Topic: Methods of Set in Python
# Author: Subhrangsu Sinha
# Date: 25.08.2022

set1 = set()
print(set1)
# If we want to add elements in set:-
set1.add(10)
set1.add('Subhrangsu')
set1.add('Subhrangsu')
set1.add('Subhrangsu')

print(set1) #--> set cannot store duplicate eliments
# we can add tuple in the set:--
set1.add(("Suvo",10,10.45))
print(set1)
# we cannot add LIST & DICTIONARY in the set

# If we want remove any item from set:-
set1.remove(10)
print(set1)

# If we want to remove any random item from the set:-
print(set1.pop())

# If we want to make a empty set from a existing set:-
print(set1.clear())

# if We want to print all the element between two sets:-
set1 = {1,2,3,4}
print(set1.union({9,8}))

# if We want to print distict element between two sets:-
print(set1.intersection({9,8,1,2}))
