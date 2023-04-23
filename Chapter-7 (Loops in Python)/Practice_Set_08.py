# Topic: Practice Set--> Write a python program to dynamically reverse 2-D elements in a List
# Author: Subhrangsu Sinha
# Date: 04.09.2022
# def reversing(list3,k):
#     for l in range(k):
#         for m in range(int(k/2)):
#             temp_var =  list3[l][m]
#             list3[l][m] = list3[l][k-1-m]
#             list3[l][k-1-m] = temp_var
#     print('After Swapping the List will be:-')
#     print(list3)    
k=3
i=0
list3=[]
while i<k:
    j=1
    while j<=k:
        user_first = input('Enter your first name: ')
        user_last = input('Enter your last name: ')
        user_occupation = input('Enter your occupation: ')
        i1 = [user_first,user_last,user_occupation]
        list3.append(i1)
        j+=1
    i+=1
print(list3)
for l in range(k):
        for m in range(int(k/2)):
            temp_var =  list3[l][m]
            list3[l][m] = list3[l][k-1-m]
            list3[l][k-1-m] = temp_var
print('After Swapping the List will be:-')
print(list3)
# swapping = reversing(list3,k)

