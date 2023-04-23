# Topic: Practice Set--> write a python program to create a class Vector of n dimension. Overload the + and * operator which calculates the sum and the dot product of them
# Author: Subhrangsu Sinha 
# Date: 20.09.2022

class Vector:
    def __init__(self,list1):
        self.list1 = list1
    
    def __str__(self):
        str1 = ''
        index = 0
        for i in self.list1:
            str1 = str1 + f' {i} a{index} +'
            index = index +1
        return str1

    def __add__(self,self2):
        newlist  =[]
        for i in range(len(self.list1)):
            newlist.append(self.list1[i] + self2.list1[i])
        return(Vector(newlist))

    def __mul__(self,self2):
        newlist  =[]
        for i in range(len(self.list1)):
            newlist.append(self.list1[i] * self2.list1[i])
        return(Vector(newlist))
v1 = Vector([1,4])
v2 = Vector([1,6])
print(v1 + v2)

print(v1*v2)
