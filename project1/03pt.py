# try:
#     table = [7*i for i in range(1,11)]
#     s = "\n".join(str(x) for x in table)  # 1. Convert integers to strings before joining
#     print(s)
# except Exception as e:
#     print(e)

def reverse_string(s):
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string # Concatenate current character with reversed string
        print(reversed_string)
    return reversed_string

# Test the function
print(reverse_string("mohan"))  # Should print "olleh"



# def is_palindrome(s):
#     return s == reverse_string(s)   # Check if the string is equal to its reversed string

# print(is_palindrome("racecar"))  # Should print True


# queries = int(input())


