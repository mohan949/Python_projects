class Employee :
    company = "ITC "
    name = 'mohan'
    salary = 1000
    language = 'Pyhton'
 

class coder:
    def showCoder(self):
        print(f'The employee {self.name} and code the language {self.language}')        

class Programmer(Employee, coder):
    
    def showSalary(self):
        print(f'The name is {self.name} and the salary is {self.salary}')

    def showLanguage(self, Rating):
        print(f'the name is {self.name} and he is good with {self.language} language with {Rating}')

b= Programmer()

print(b.name)
b.showSalary()
b.showCoder()
b.showLanguage(5)