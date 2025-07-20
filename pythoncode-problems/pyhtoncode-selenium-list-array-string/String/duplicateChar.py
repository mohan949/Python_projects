

# # l = []
# # for i in  s:
# #     l.append(i)

# # print(l)

# from collections import Counter


# s = 'Mohaaan'
# s = set(s)

# def duplicate(s):
#     a = ''.join(s)
#     return a

# print(duplicate(s))


# def print_duplicates(input_string):
    
#     # Count the occurrences of each character
#     char_count = Counter(input_string)
    
#     # Iterate through the count dictionary and print duplicates
#     print("Duplicate characters:")
#     for char, count in char_count.items():
#         if count > 1:
#             print(f"'{char}' occurs {count} times")

# # Example usage
# string = "programming"
# print_duplicates(string)



# using loop
def remove_duplicates(input_string):
    result = ""
    for char in input_string:
        if char not in result:
            result += char
            print('result',result)
            print('char',char)
    return result

# Example usage
# string = "programming"
# result = remove_duplicates(string)
# print("Result:", result)  # Output: "progamin"


def dup(s):
    a = ''
    for char in s:
        if char not in a:
           # a += char
           a = a + char

    return a       


s = "programming"
result = dup(s)
print("Result:", result)  # Output: "progamin"
