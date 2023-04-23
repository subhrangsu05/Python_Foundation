# Topic: Practice Set--> write a python program to create a class Train which has methods to book a ticket, get status(no of seats),get fare info and cancel ticket of trains running under the Indian Railways.
# Author: Subhrangsu Sinha
# Date: 17.09.2022
class Train:
    total_seat = 100
    print(f'The available seats are {total_seat}')
    @staticmethod
    def greet():
        print('Good Morning Sir')

    def __init__(self,name,train_name):
        self.name = name
        self.train_name = train_name
    
    def Ticket_Book(self):
        if self.total_seat > 0:
            print(f'Mr.{self.name}, Your ticket has been booked  Successfully at {self.train_name}')
            print(f'Your seat number is {self.total_seat}')
            self.total_seat = self.total_seat-1
        else:
            print(f'Sorry, Mr.{self.name}. No seats are available in this train.')

    def get_status(self):
        print(f'Now,the total available seats are {self.total_seat}')

    def Ticket_cancel(self):
        cancel_ticket = input('if you want to cancel your ticket pls write, yes: ')
        if cancel_ticket == 'Yes' or cancel_ticket == 'yes' or cancel_ticket == 'YES':
            self.total_seat = self.total_seat + 1
            print(f'Mr.{self.name}, Your ticket has been Cancelled Successfully at {self.train_name}')
            print(f'Now,the total available seats are {self.total_seat}')
        else:
            print('Thank You, Sir')


name = input('Enter your name: ')
train_name = input('Enter your train name: ')
passanger = Train(name, train_name)
passanger.greet()
passanger.Ticket_Book()
passanger.get_status()
passanger.Ticket_cancel()