# Topic: Practice Set--> A file contains a word 'Donkey' multiple times.You need to write a python program which replaces this word with ####### by updating the same file.
# Author: Subhrangsu Sinha
# Date: 12.09.2022
with open('C:\\Users\\subhr\\Desktop\\PYTHON BASICS\\Chapter-9 (File I\O )\\sample3.txt','r') as file_content:
    data = file_content.read()
    data = data.replace('Donkey','######')
with open('C:\\Users\\subhr\\Desktop\\PYTHON BASICS\\Chapter-9 (File I\O )\\sample3.txt','w') as write_content:
    write_content.write(data)