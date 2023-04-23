# Topic: Introduction with Super Method & Class Method in Python
# Author: Subhrangsu Sinha
# Date: 19.09.2022
'''
What is Super method?
Super Method is used to access the method of a super class in the derived class
'''
class Employer:
    company = 'ABC'
    def sal(self):
        salary = 10000
        print(salary)
class Employee(Employer):
    name = 'Subhrangsu'
    def salo(self):
        super().sal()
Emp = Employee()
Emp.sal()

'''
What is Class Method?
IF we want to manipulate class attributes then we need to use Class Method. We don't want to create self / instance attribute
'''
class Student:
    school = 'ABC'
    total_student = 100
    @classmethod
    def studentt(clss,total_student):
        clss.total_student = total_student + 1
        
s = Student()
s.studentt(255)
print(Student.total_student)
print(s.total_student)


# Another Approach of class method:-

class Student:
    school = 'ABC'
    total_student = 100
    def studentt(self,total_student):
        self.__class__.total_student = total_student + 1
        
s = Student()
s.studentt(300)
print(Student.total_student)
print(s.total_student)
