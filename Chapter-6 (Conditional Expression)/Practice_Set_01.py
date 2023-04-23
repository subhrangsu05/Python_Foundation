# Topic: Practice Set--> Write a python program to find the greatest number between four numbers entered by the user
# Author: Subhrangsu Sinha
# Date: 27.08.2022
n1,n2,n3,n4 = int(input("Enter the no1: ")),int(input("Enter the no2: ")),int(input("Enter the no3: ")),int(input("Enter the no4: "))
if n1 > n2 and n1 > n3 and n1 > n4:
    print(f"{n1} is the greatest number")
elif n2 > n4 and n2 > n1 and n2 > n3:
    print(f"{n2} is the greatest number")
elif n3 > n4 and n3 > n1 and n3 > n2:
    print(f"{n3} is the greatest number")
else:
    print(f"{n4} is the greatest number")


# Another Approach:-
# Smartest Technique:-
if n1 > n4:
    f1 = n1
else:
    f1 = n4
if n2 > n3:
    f2 = n2
else:
    f2 = n3
if f1 > f2:
    print(f"{f1} is the greatest")
else:
    print(f"{f2} is the greatest")