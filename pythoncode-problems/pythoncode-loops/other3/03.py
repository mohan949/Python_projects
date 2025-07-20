class Employee:
    salry = 234
    increment = 20
    @property
    def  salary(self):
        return (self.salry  + self.salry *(self.increment/100))

e = Employee()
print(e   .salary)


