# s ={1,2,3,4}
# s.add(6)
# print(s)

# u =set()
# n = input("enter the name")

# for _ in range(8):
#   u.add(int(n))

# n=9
# # for _ in range(10):
# #     a = n*_
# #     print(a)

# s = set()
# for _ in range(8):
#     n = input('enter the number ')
#     s.add(int(n))
# print(s)

d = {}


for _ in range(3):
    name = input('enter name ')
    lang = input('enter language ')
    d.update({name:lang})
print(d)
