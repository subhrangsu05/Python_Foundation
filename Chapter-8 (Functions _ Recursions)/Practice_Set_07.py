# Topic: Practice Set--> write a python function to remove a given word from a string and strip it at the same time
# Author: Subhrangsu Sinha
# Date: 11.09.2022
def remove_and_strip(text):
    new_text = text.replace('my name is','Subhrangsu')
    print(new_text )
    print(new_text.strip())
    

text = '  my name is '
remove_and_strip(text)