

class Programmer :
    company = 'Mircosoft'
    designation = 'SDE'

    def __init__(self, name, pin, salary) -> None:
        self.name1 = name 
        self.salary = salary
        self.pin = pin

    def get_name(self):
        return self.name
    
    def get_capital_name(self):
        return self.name.capitalize()
    
    def get_multiplier(self, x):
        return 2 * x

    @staticmethod
    def hello():
        print("ge")

p = Programmer('Mohan', 110, 10)

p.get_name()
p.get_multiplier(15)


print(p.name1)
print(p.company)
