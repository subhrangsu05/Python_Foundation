# Topic: Practice Set--> write a python program to create a class 2-D Vector and use it to create another class representing a 3-D Vector
# Author: Subhrangsu Sinha
# Date: 20.09.2022
class C2dvec:
    def __init__(self,i,j):
        self.icap = i
        self.jcap = j
    def __str__(self):
        return f'{self.icap}i + {self.jcap}j'
class C3dvec(C2dvec):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap = k
    def __str__(self):
        return f'{self.icap}i + {self.jcap}j + {self.kcap}k'
v2d = C2dvec(1,3)
v3d = C3dvec(2,4,6)
print(v2d)
print(v3d)