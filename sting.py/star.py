
# for i in range (r,0):
#     print(r)
#     # for r in range(i):
#     #     print("*")

# for i in range(r, ):
#    # for r in range(i):
#      print("*",end='')



# for _ in range(1, r):
#     print("i-->",_)
#     print("r-->",r)
#     for x in range(_):
#        print(x," ",end='')
#     print()


r = 6


for _ in range(0, r):
    for x in range(_):
       print('*', end='')
    print()

print("----------------------")

for _ in range(r, 0, -1):
    for x in range(_):
       print('*', end='')
    print()

print("----------------------")

for _ in range(r, 0, -1):
    for x in range(_):
        print(" ",end='')
    print("*")    

print("----------------------")

rows = 10  # Number of rows in the pattern

for i in range(rows):
    # Print leading spaces
    for j in range(i):
        print(' ', end='')
    
    # Print stars
    for k in range(rows - i):
        print('*', end='')
    
    # Move to the next line
    print()


print("----------------------")
