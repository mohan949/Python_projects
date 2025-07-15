
a = int(input('enter the number'))

def star(a):
    if(a==0):
      return
    print('*' * a)
    star(a-1)

star(a)