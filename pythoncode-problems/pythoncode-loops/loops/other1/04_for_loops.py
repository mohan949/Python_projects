#range (start, stop, step)

Table = int(input('Enter the no for which you want table : '))

for _ in range(1, 10+1):
    print(f'{Table} X {_} = ',_*Table)