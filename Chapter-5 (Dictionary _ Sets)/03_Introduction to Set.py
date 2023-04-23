# Topic: Introduction with Set in Python
# Author: Subhrangsu Sinha
# Date: 25.08.2022
'''
1) Set is a collection of Non-repitative elements
2) We can declare set elements between double brackets
3) Sets are unordered
4) sets are unindexed
5) There are no way to change items in sets, So, sets are immutable
6) Sets can not contains duplicate values
'''
set1 = {1,2,3,4}
print(set1)
set2 = {1,2,3,4,1}
print(set2) #--> It wont print the repitative items 
# print(set2[2]) #--> It will throws error due to unindexing

# Empty Set Declaration:-
empty_set = set()
