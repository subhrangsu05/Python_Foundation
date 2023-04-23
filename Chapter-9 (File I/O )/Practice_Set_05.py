# Topic: Practice Set--> Repeat the practice set 4 for a list of such words.
# Author: Subhrangsu Sinha
# Date: 12.09.2022
list1 = ['Apple','Banana','Mango','Donkey']
for item in list1:
    if item == 'Donkey':
        list1.remove('Donkey')
with open('C:\\Users\\subhr\\Desktop\\PYTHON BASICS\\Chapter-9 (File I\O )\\fruits.txt','w') as file_content:
    for item in list1:
         file_content.write(item)
         file_content.write('\n')

