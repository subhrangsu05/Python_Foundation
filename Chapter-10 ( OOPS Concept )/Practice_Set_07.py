# Topic: Practice Set--> write a python program to create a class Employee and add salary and the increment properties to it. Write a method salayAfterIncrement method with a @property decorator with a setter which changes the value of increment based on the salary
# Author: Subhrangsu Sinha
# Date: 20.09.2022
class Employee:
    def __init__(self,sal,hike):
        self.salary = sal
        self.hike = hike

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.hike

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,newvalue):
        self.hike = newvalue/self.salary

sal = int(input('Enter the salary: '))
hike = float(input('Enter the hike percentage: '))
E = Employee(sal,hike)
print(E.salaryAfterIncrement)
E.salaryAfterIncrement = int(input('Enter the New Salary: '))
print(f'The New Hike willbe: {E.hike}')

