
squares = [x**2 for x in range(10)]
print(squares)

my_list = []
for i in range(10):
    print(f'2 X {i} = {5*i}')
    my_list.append(5*i)
    even =  [x for x in my_list if x % 2 == 0]
print(my_list)
print(even)
    

    

my_list1 = [1   , 2 ,2,4,5,6,7,8] 
print(max(my_list1))

from collections import Counter
counts = Counter(my_list1)
print(counts)


result = list(set(my_list) & set(my_list1))
print(result)