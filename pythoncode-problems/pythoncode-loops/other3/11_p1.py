import types
from typing import Any


class TwoDvetor:
    def __init__(self, i , j) -> None:
        self.i = i
        self.j = j

       
    def show(self):
        print(f'The Vector is {self.i}i + {self.j}j')


class ThreeDVector(TwoDvetor):
    def __init__(self, i , j ,k):
        super( ).__init__(i, j )
        self.k = k


    def show(self):
        print(f'The Vector is {self.i}i + {self.j}j + {self.k}k')


a = TwoDvetor(3 , 5)
a.show()
b = ThreeDVector(3, 9, 7)
b.show()    