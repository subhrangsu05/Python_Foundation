# Topic: Introduction with IS and IN keyword in Python
# Author: Subhrangsu Sinha
# Date: 26.08.2022

# We can use is and in keyword instead of '=' assign operator
# Utilisation of is keyword:
from ast import keyword


no  = 25
if no is 25:
    print("Yes")
else:
    print("No")

    
# utilisation of in keyword:-
list1 = [10,20,30]
if 30 in list1:
    print("Yes")
else:
    print("No")