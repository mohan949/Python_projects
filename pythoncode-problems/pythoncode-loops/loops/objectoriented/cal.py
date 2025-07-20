class Calcultor :
    def __init__(self, n) -> None:
        self.n = n 

    def add(self):
        print('square ',self.n*self.n)

    def cube(self):
        print('cube ', self.n*self.n*self.n)   


a = Calcultor(5)
a.add()
a.cube()