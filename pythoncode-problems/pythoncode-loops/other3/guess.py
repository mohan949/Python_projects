import random
a = random.randint(1, 100)

print(a)
n  = 0
guess = 0
while(n!=a):
    n = int(input('Enter the number :'))
    if(a>n):
        print('Enter a high number')
    elif(a<n):
        print('Enter a low number')
    guess = guess + 1    

print(f'congrats you hav guessed right number {a} in guess {guess}')
    
    