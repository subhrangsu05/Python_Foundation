# Topic: Practice Set--> write a python program to create a class to show that can we change self parameter to something else. Try changing self to 'slf' or 'your name' and see the impacts.
# Author: Subhrangsu Sinha
# Date: 17.09.2022
class Sum:
    def Sum(subhrangsu): 
        return subhrangsu.a + subhrangsu.b
num = Sum()
num.a = 12
num.b = 10
Result = num.Sum() 
print(f'The sum of {num.a} and {num.b} is {Result}')

#--> yes, we can chnage becasue self is not any reserved keyword in python. we can write anything instead of self 
