# Topic: Practice Set--> write a python program to read the text from a given file 'poem.txt' and find out wheather it contains the 'twinkle' 
# Author: Subhrangsu Sinha
# Date: 11.09.2022
contains_data = open('C:\\Users\\subhr\\Desktop\\PYTHON BASICS\\Chapter-9 (File I\O )\\poem.txt')
data = contains_data.read()
if data.count('Twinkle') or data.count('twinkle'):
    print('Found Successfull')
else:
    print('Twinkle world is not present')
contains_data.close()


# Modern Approach:-
with open('C:\\Users\\subhr\\Desktop\\PYTHON BASICS\\Chapter-9 (File I\O )\\poem.txt') as contains_data:
    data = contains_data.read()
if data.count('Twinkle') or data.count('twinkle'):
    print('Found Successfull')
else:
    print('Twinkle world is not present')