#Star pattern


n = int(input('enter the number '))

# for _ in range(3):
#     for i in range(_):
#         print('*',end='')
#     print()
'''
   *
  ***
 ***** 
'''


for _ in range(1, n+1):
    print(' '*(n-_), end='')
    print('*'*(2*_-1),end='')
    print()

