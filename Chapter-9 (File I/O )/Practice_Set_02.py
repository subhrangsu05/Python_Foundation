# Topic: Practice Set--> write a python function game() in a program. Lets a user play any game and returns the score as an integer. You need to read a file 'Highscore.txt' which is either blank or contains the previous High score. You need to write a program to update the high score when-ever game() breaks the previous high score.
# Author: Subhrangsu Sinha
# Date: 11.09.2022
def game(list1):
    return sum(list1)
name = input('Enter your name: ')
list1 = []
for charcter in name:
    list1.append(ord(charcter))
result = game(list1)
with open('C:\\Users\\subhr\\Desktop\\PYTHON BASICS\\Chapter-9 (File I\O )\\High_Score.txt','r') as file_content:
    data = file_content.read()
if data == '' :
    with open('C:\\Users\\subhr\\Desktop\\PYTHON BASICS\\Chapter-9 (File I\O )\\High_Score.txt','w') as file_content:
        file_content.write(str(result))
elif result > int(data) :
    with open('C:\\Users\\subhr\\Desktop\\PYTHON BASICS\\Chapter-9 (File I\O )\\High_Score.txt','w') as file_content:
        file_content.write(str(result))

else:
    print(f"Your highest score is {int(data)}")
    print("Your current score is equals to / poor than highest score")
