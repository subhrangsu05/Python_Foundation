# Topic: Practice Set--> write a python program to print first n lines of the following pattern:
#    * * *
#    * *
#    *
# Author: Subhrangsu Sinha
# Date: 11.09.2022
def pattern(num):
    for i in range(num):
        print('*'*(num-i))
    else:
        print('Successfully print the pattern')

num = int(input('Enter the line no: '))
pattern(num)