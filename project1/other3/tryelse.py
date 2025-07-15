try :
    a = int(input())
    print(a)

except Exception as e:
    print(e)

if a>0:
    print(a)
elif a>4:
    print(a)
else:
    print('a')
