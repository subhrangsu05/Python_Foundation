# Topic: String negative indices in Python
# Author: Subhrangsu Sinha
# Date: 21.08.2022

# Why We need to use NEGATIVE INDICES? Ans--> If we don't know the length of  the string and we want to access the last index then we can use NEGATIVE INDICES.
name = 'Subhrangsu'
# S-> index 0   as well as -10
# u-> index 1   as well as -9
# b-> index 2   as well as -8
# h-> index 3   as well as -7
# r-> index 4   as well as -6
# a-> index 5   as well as -5
# n-> index 6   as well as -4
# g-> index 7   as well as -3
# s-> index 8   as well as -2
# u-> index 9   as well as -1
# If we want to print a last character in the string -->
print(name[-1]) #-->[index position]
# If we want to print 'Sub' -->
print(name[-10:-1])  #-->[Negative index starting position : end position (-index - 1)]
