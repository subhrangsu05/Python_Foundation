# Topic: Practice Set--> Write a python program to detect the spam comments
# Author: Subhrangsu Sinha
# Date: 27.08.2022

msg = input("Enter your message: ")
if msg == 'make a lot of money' or msg == 'buy now' or msg == 'subscribe this' or msg == 'click this':
    f = False
else:
    f = True
if f:
    print('This is a Normal Message')
else:
    print('This is a Spam Message')