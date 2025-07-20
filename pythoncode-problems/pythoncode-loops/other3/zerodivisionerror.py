a = int(input())
b = int(input())

if(b==0):
    raise ZeroDivisionError("hey this is wrong") 
else:
    print(a/b)
