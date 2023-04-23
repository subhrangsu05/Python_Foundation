# Topic: Practice Set--> write a recursive function to calculate the sum of first n natural numbers
# Author: Subhrangsu Sinha
# Date: 11.09.2022
def natural(num):
    if num == 0 or num == 1:
        return 1
    else:
        first = num + natural(num-1)
        return first
num = int(input('Enter the reachest number: '))
print(f'The sum of the first {num} natural number is {natural(num)}')