import random


class Train:

    def __init__(self, TainNO) -> None:
        self.trainNO = TainNO
        


    def book(self, trainNo, fro , to):
        print(f'Ticket Booked for {self.trainNO} from {fro} and {to}')

    @staticmethod
    def getStatus():
        print('Train is running on time')


    def getFare(self, trainNo, fro , to):
        print(f'Ticket fare for {self.trainNO} from {fro} to {to} is {random.randint(200, 900)  }')


t = Train(24567)
t.book(1225, 'Mumbai', 'Gorakhpur')
t.getStatus()
t.getFare(1225, 'Mumbai', 'Gorakhpur')