
# Common string interview questions and solutions

def reverse_string(s):
    """Reverse a string"""
    return s[::-1]



def is_palindrome(s):
    """Check if string is palindrome"""
    # Remove non-alphanumeric chars and convert to lowercase
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

def first_unique_char(s):
    """Find first non-repeating character in string"""
    char_count = {}
    for c in s:
        char_count[c] = char_count.get(c, 0) + 1
    
    for i, c in enumerate(s):
        if char_count[c] == 1:
            return i
    return -1

def is_anagram(s1, s2):
    """Check if two strings are anagrams"""
    return sorted(s1.lower()) == sorted(s2.lower())

def longest_common_prefix(strs):
    """Find longest common prefix among array of strings"""
    if not strs:
        return ""
        
    shortest = min(strs, key=len)
    
    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]
    return shortest

def longest_substring_without_repeating(s):
    """Find longest substring without repeating characters"""
    char_pos = {}
    start = max_len = 0
    
    for i, char in enumerate(s):
        if char in char_pos and char_pos[char] >= start:
            start = char_pos[char] + 1
        else:
            max_len = max(max_len, i - start + 1)
        char_pos[char] = i
            
    return max_len

def valid_parentheses(s):
    """Check for valid parentheses in string"""
    stack = []
    pairs = {')':'(', '}':'{', ']':'['}
    
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0