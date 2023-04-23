# Topic: String slicing in Python
# Author: Subhrangsu Sinha
# Date: 21.08.2022

name = 'Subhrangsu'
# S-> index 0
# u-> index 1
# b-> index 2
# h-> index 3
# r-> index 4
# a-> index 5
# n-> index 6
# g-> index 7
# s-> index 8
# u-> index 9
# If we want to print a character in the string -->
print(name[0]) #-->[index position]
# If we want to print 'Sub' -->
print(name[0:3])  #-->[index starting position : end position (index - 1)]


###################################### SLICING WITH SKIP VALUE ######################################

company = 'TATA CONSULTANCY SERVICES INDIA PVT LTD'
# T-> index 0
# A-> index 1
# T-> index 2
# A-> index 3
#  -> index 4
# C-> index 5
# O-> index 6
# N-> index 7
# S-> index 8
# U-> index 9

print(company[0:10:2])  #-->[index starting position : end position (index - 1) : Skip value ]