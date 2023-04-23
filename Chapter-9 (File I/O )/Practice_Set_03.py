# Topic: Practice Set--> write a python program to generate multiplication table for 2 to 20 and write it to the different files. Place these files in a folder for a 13 years old student.
# Author: Subhrangsu Sinha
# Date: 12.09.2022
for table_no in range(2,21):
    for table_column in range(1,11):
        data =(f'{table_no} X {table_column} = {table_no*table_column}\n')
        with open(f'C:\\Users\\subhr\\Desktop\\PYTHON BASICS\\Chapter-9 (File I\O )\\13 Years old\\table {table_no}.txt','a') as file_content:
            file_content.write(str(data)) 