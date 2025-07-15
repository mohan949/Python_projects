
def reverse_string(s):
    return s[::-1]
print(reverse_string('slicing'))



def reverse_string_for(s):
    reverse_string = ""
    for char in s[::-1]:
        reverse_string = reverse_string + char
    return reverse_string
    
s = 'ForLoop'
reverse_string_for = reverse_string_for(s)
print(reverse_string_for)


def reverse_string_while(s):
    reverse_string =''
    index = len(s) - 1
    while index >=0:
        reverse_string = reverse_string + s[index]
        index -= 1
    return reverse_string

s = 'while loop'
reverse_string_while = reverse_string_while(s) 
print(reverse_string_while)