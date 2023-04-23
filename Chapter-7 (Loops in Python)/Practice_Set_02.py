# Topic: Practice Set--> Write a python program to greet all the person names stored in a list and person names should be start with 'S'
# Author: Subhrangsu Sinha
# Date: 04.09.2022
name = ['Subhrangsu','Rahul','Rohan','Subham']
for item in name:
    if item.startswith('S') or item.startswith('s'):
        print(f'Good Afternoon, {item}')