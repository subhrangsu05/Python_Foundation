# Topic: Practice Set--> Write a python program to fill in a letter template given below with name and date.
# letter =    <NAME>,
#             You are Selected.
#             <Date>
# Author: Subhrangsu Sinha
# Date: 23.08.2022


#-------------> Traditional Way------------->
name = 'subhrangsu'
date = '23.08.2022'
letter = '''<NAME>,
You are selected.
<DATE>'''
letter = letter.replace('<NAME>',name)
letter = letter.replace('<DATE>',date)
print(letter)

#-------------> Advanced Way--------------->
name1 = 'subhrangsu'
date1 = '23.08.2022'
letter1 = '''{name1},
You are selected.
{date1}'''
print(letter)
 