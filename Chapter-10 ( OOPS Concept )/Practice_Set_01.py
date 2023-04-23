# Topic: Practice Set--> write a python program to create a class programmer for storing information of few programmers working at your company.
# Author: Subhrangsu Sinha
# Date: 17.09.2022
class Employee:
    Company = 'Microsoft'
    store = {'name':'',
        'age': '',
        'domain': '',
        'Company': Company}
    def __init__(self,name,age,domain):
        self.name, self.age, self.domain = name, age, domain
    def data_stored(self):
        self.store.update({'name': self.name})
        self.store.update({'age': self.age})
        self.store.update({'domain': self.domain})
        print(Employee.store)
name = input('Enter your name: ')
age = input('Enter your age: ')
domain = input('Enter your domain: ')
Subhrangsu_details = Employee(name,age,domain)
Subhrangsu_details.data_stored()