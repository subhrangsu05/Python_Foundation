# Topic: Practice Set--> Write a python program to to calculate the grade of a student from their marks from the following schema:
# 90-100->Outstanding
# 70-90->Excellent
# 60-70->A
# 50-60->B
# 40-50->C
# 30-40->D
# 30>= -> Fail
# Author: Subhrangsu Sinha
# Date: 27.08.2022

math,english,computer = int(input("Enter your math marks: ")),int(input("Enter your english marks: ")),int(input("Enter your computer marks: "))
total = (math + english + computer)*(1/3)
if total<= 100 and total >90:
    print('Outstanding')
elif total <= 90 and total > 70:
    print('Excellent')
elif total <= 70 and total > 60:
    print('A')
elif total <= 60 and total > 50:
    print('B')
elif total <= 50 and total > 40:
    print('C')
elif total <= 40 and total >30:
    print('D')
else:
    print('FAIL')