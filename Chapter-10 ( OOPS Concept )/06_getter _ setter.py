# Topic: Introduction with Getter Method & Setter Method in Python
# Author: Subhrangsu Sinha
# Date: 19.09.2022

'''
What is Getter Decorator?
Getter is a decorator property. If we want to use a function as a attribute / variable then we need to Getter decorator.
'''
class Employee:
    company = 'Amazon'
    salary = 10000
    salary_bonus = 1100
    @property
    def Total_Salary(self):
        return  self.salary + self.salary_bonus

e = Employee()
print(e.Total_Salary)

'''
What is Setter Decorator?
Setter is a decorator property. If we want to update the value of getter attributes then we need to update rest the attributes also.
setter helps to do that.
'''

class Employee:
    company = 'Amazon'
    salary = 10000
    salary_bonus = 1100
    @property
    def Total_Salary(self):
        return  self.salary + self.salary_bonus
    
    @Total_Salary.setter
    def Total_Salary(self,value):
        self.salary_bonus = value - self.salary
        print('value is ',value)

e = Employee()
print(e.Total_Salary)
e.Total_Salary = 15000
print(e.salary)
print(e.salary_bonus)


