# Topic: Practice Set--> Write a python program using function to find greatest number in the list
# Author: Subhrangsu Sinha
# Date: 10.09.2022
def greatest(list1):
   list1.sort()
   return list1[-1]
list1=[]
for i in range(5):
    num = int(input(f"Enter the no{i+1} : "))
    list1.append(num)
print(f'The greatest number will be: {greatest(list1)}')
