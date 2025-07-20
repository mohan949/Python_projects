n = int(input('enter the number '))

for _ in range(2, n):
    if (n%_) == 0:
        print('Number os not a prime')
        break
else:
    print('Number is prime')    