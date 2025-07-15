class Employee :
    company = "ITC "
    name = 'mohan'
    salary = 1000
    language = 'Pyhton'
    def __init__(self) -> None:
        print('This is a super constructor of Employee')
 

class coder(Employee):

    def __init__(self) -> None:
        super().__init__()   
        print('This is a super constructor of coder')

    def showCoder(self):
        print(f'The employee {self.name} and code the language {self.language}')        

class Programmer(coder):
    
    def __init__(self) -> None:
        super().__init__()
        print('This is a super constructor of Programmer')

    def showSalary(self):
        print(f'The name is {self.name} and the salary is {self.salary}')

    def showLanguage(self, Rating):
        print(f'the name is {self.name} and he is good with {self.language} language with {Rating}')

b= Programmer()

# b.showSalary()
# b.showCoder()
# b.showLanguage(5)