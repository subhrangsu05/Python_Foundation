# Topic: Practice Set--> Write a python program to print this star pattern
#          *
#        * * *
#      * * * * *
# Author: Subhrangsu Sinha
# Date: 04.09.2022

line = int(input('Enter the line no: '))
for i in range(line):
        print(' '*(line-i-1),end='')
        print('*'*(2*i+1),end='')
        print(' '*(line-i-1))
