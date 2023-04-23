# Topic: Practice Set--> Write a python program using function to convert celcius to Farenheit
# Author: Subhrangsu Sinha
# Date: 10.09.2022
def farenheit(celcius):
    return  (celcius*(9/5))+32
celcius = float(input('Enter the celcius temperature: '))
print(f'{celcius} temperature = {farenheit(celcius)} Farenheit')