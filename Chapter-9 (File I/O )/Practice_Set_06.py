# Topic: Practice Set--> Write a python program to find out the line number where python is present.
# Author: Subhrangsu Sinha
# Date: 12.09.2022
data = True
line_no = 1
with open('C:\\Users\\subhr\\Desktop\\PYTHON BASICS\\Chapter-9 (File I\O )\\sample4.txt','r') as file_content:
    while data:
        data = file_content.readline()
        line_no = line_no+1
        if 'Python' in data:
            print(f'Python keyword is present in line no {line_no}')
        else:
            print('Python keyword is not present in the File')
