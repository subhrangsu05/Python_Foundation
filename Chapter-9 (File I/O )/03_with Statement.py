# Topic: with statement in Python
# Author: Subhrangsu Sinha
# Date: 11.09.2022
'''
what is with statement? 
with statement is an advanced features in python file segmentation. If we're used with statement then we don't need to use close() after data manipulation.
It'll close the file automatically explicitly
'''
with open('C:\\Users\\subhr\\Desktop\\PYTHON BASICS\\Chapter-9 (File I\O )\\sample2.txt','w') as file_content:
    data = file_content.write('My name is Subhrangsu and I am Software Development Engineer')