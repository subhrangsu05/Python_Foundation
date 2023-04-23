# Topic: Practice Set--> Write a python program to replace the double spaces from practice set 3 with single spaces.
# Author: Subhrangsu Sinha
# Date: 23.08.2022

story = 'My  name is  Subhrangsu. I  wanna be CEO of  Alphabet'
print('Total double spaces are: ',story.count('  '))
print(story.replace('  ',' '))