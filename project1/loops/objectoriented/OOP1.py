class Employee :
    name = ''
    language =  'english'
    salary = 100

    # def __init__(self) -> None:
    #     pass

    def getInfo(self , salary, language, name):
        print(f'name --> {name} salary --> {salary} & language --> {language}')


    def getGreeting(self, name):
        print('Good Morninng',name)



mohan = Employee()
mohan.salary = 120
mohan.name = 'mohan'
print(f'name --> {mohan.name} salary --> {mohan.salary} & language --> {mohan.language}')

kavaita = Employee()
kavaita.getInfo(100, 'english', 'kavita')
kavaita.getGreeting('kavita')