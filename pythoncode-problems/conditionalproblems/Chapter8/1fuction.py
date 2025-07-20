# a = 12
# b = 3
# c = 5 

def sum(a, b, c=2):
    sum = a+b+c
    print(sum)

sum(1 , 1, 1 )

def default(name , surname='No surname'):
    print(name, surname)



default('mohan', 'prasad')
default('mohan')