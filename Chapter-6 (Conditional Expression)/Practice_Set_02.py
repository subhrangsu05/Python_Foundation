# Topic: Practice Set--> Write a python program to find out weather a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subject and take marks as an input from user.
# Author: Subhrangsu Sinha
# Date: 27.08.2022

# Lets try this program in different Approach.
sub1,sub2,sub3 = int(input('Enter the marks: ')),int(input('Enter the marks: ')),int(input('Enter the marks: '))
total = (sub1+sub2+sub3)*(1/3)
if sub1 > 33 and sub2 > 33 and sub3 > 33:
    if total > 40:
        promotion = True
    else:
        promotion = False
else:
    promotion = False

if promotion:
    print('The Student is Promoted')
else:
    print('The student is Non-Promoted')