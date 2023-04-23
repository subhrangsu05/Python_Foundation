# Topic: String methods in Python
# Author: Subhrangsu Sinha
# Date: 21.08.2022

name = 'Subhrangsu'
story = 'once upon a time in my Lyf, I was chemistry lover'
# 1> len(variable) / string variable.len() --> Find the length of a string
print(len(name))

# 2> string variable.startswith() --> String starts with a particular character
print(name.startswith('S'))
print(name.startswith('s'))
print(story.startswith('Once'))


# 3> string variable.endswith() --> String ends with a particular character
print(name.endswith('u'))
print(name.endswith('U'))
print(name.endswith('lover'))


# 4> string variable.count() --> count a particular character / word in the entire string but it's case sensitive
print(name.count('s'))
print(name.count('S'))
print(story.count('s'))
print(story.count('chemistry'))

# 5> string variable.capitalize() --> It changes to the capital letter from the small letter of a string
print(story.capitalize())

# 6> string variable.find() --> to find a word in the string
print(story.find('was')) # If it will return -1, that means the word is not available in the string

# Note: find() takes the first occurence of that word in the string

# 7> string variable.replace() --> to change a existing word to new word / existing character to new character
print(story.replace('once upon a time','Many Many times ago'))


# Disclaimer: When you're using string methods then original string also changed.
