

def are_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(are_anagram('listen', 'silent'))

s = 'mohan'
print(sorted(s))
my_list = []
for char in s:
    print(char)
    my_list.append(char)
print(my_list)
my_list.sort()
print(my_list)
