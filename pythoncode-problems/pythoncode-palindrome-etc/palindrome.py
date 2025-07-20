# #palindrome
# def pallindrome(n):
#     if n == n[::-1]:
#         print("Palindrome")
#     else:
#         print("Not a palindrome")

# pallindrome('nitin')

# left = 5
# right = 5

# while left  < right:
#     # count = count +1
#     # count += 1

  
#     print(left)
#     print(right)


def is_palindrome(s):
    left = 0
    right = len(s) - 1

    print("Left pointer:", left)
    print("Right pointer:", right)

    # Continue looping while the two pointers
    # have not crossed
    while left < right:
      
        # If the characters at the current positions
        # are not equal
        if s[left] != s[right]:
            return 0

        # Move the left pointer to the right and
        # the right pointer to the left
        left += 1
        right -= 1

    # If no mismatch is found, return 1 (palindrome)
    return 1

# Driver code
s = "abba"
print(is_palindrome(s))



s = 'mohan'
left = 0
right = len(s) - 1

def m(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return 0
        
        left = left + 1  # left += 1
        right = right - 1  # right -= 1

    return 1

print(m(s, left, right))

s = '111'
left = 0
right = len(s) - 1

def m(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return 0
        
        left = left + 1
        right = right - 1
        
    return 1

print(m(s, left, right))
