# for _ in range(1,3+1):
#     for i in range(_):
#         print('*',end='')
#     print()

# for _ in range(1,3+1):
#     print('*'*_,end='')
#     print()
'''
****
*  *
*  *
****
'''
# n = int(input('enter the number '))


# for _ in range(1,n+1):
#     print('*'*n,end='')
#     print()

rows = int(input('enter the number '))  # Number of rows

for i in range(rows):
    for j in range(rows):
        # Print '*' at the borders or spaces in the middle
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()  # Move to the next line after each row
