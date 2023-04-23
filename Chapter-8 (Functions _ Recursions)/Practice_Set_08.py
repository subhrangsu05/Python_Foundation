# Topic: Practice Set--> write a python function to print multiplicatin table of a given number
# Author: Subhrangsu Sinha
# Date: 11.09.2022
def table(table_no,table_limit):
    for i in range(table_limit):
        print( f'{table_no} X {i+1} = {table_no*(i+1)}')
table_no = int(input('Enter the table no: '))
table_limit = int(input('Enter your table limit: '))
table(table_no,table_limit)