# Topic: Practice Set--> Write a python program to find whether a given username contains less than 10 characters or not!
# Author: Subhrangsu Sinha
# Date: 27.08.2022

username = input("Enter your user name: ")
if len(username) < 10:
    print(f'{username} is less than 10 characters')
elif len(username) == 10:
    print(f'{username} is equals to 10 characters')
else:
    print(f'{username} is greater than 10 characters')
