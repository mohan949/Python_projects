# using slicing


def is_palindrone(s):
    s = s.lower().replace(" ","")
    return s == s[::-1]
    #return False
s = 'nnn'
if is_palindrone(s):
    print(f"{s} is a palindrome.")
else:
    print(f"{s} is not a palindrome.")
