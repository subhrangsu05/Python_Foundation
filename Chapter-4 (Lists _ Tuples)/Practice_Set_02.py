# Topic: Practice Set--> Write a python program to accept marks of 6 students and display them in a sorted manner.
# Author: Subhrangsu Sinha
# Date: 25.08.2022
s1,s2,s3,s4,s5,s6=int(input('Enter the marks1: ')),int(input('Enter the marks2: ')),int(input('Enter the marks3: ')),int(input('Enter the marks4: ')),int(input('Enter the marks5: ')),int(input('Enter the marks6: ')),
student = [s1,s2,s3,s4,s5,s6]
print(student)
student.sort()
print(student)