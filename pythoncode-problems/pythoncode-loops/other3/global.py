a = 69

def fun():
    global a
    a = 3
    print(a)

print(a)
fun()
print(a)