# Topic: Practice Set--> write a python function which converts inchs to cms
# Author: Subhrangsu Sinha
# Date: 11.09.2022
def convert(length_inch):
    return length_inch * 2.54
length_inch = float(input('Enter the length in inchs: '))
print(f'{length_inch} inchs length = {convert(length_inch)} cms length')