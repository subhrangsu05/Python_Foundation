# Topic: Practice Set--> Write a python program to print multiplictin table of a given number using for loop
# Author: Subhrangsu Sinha
# Date: 04.09.2022

table_no = int(input("Enter the table no: "))
for i  in range(10):
    print ( f"{table_no} X {i+1} = {table_no*(i+1)}")
