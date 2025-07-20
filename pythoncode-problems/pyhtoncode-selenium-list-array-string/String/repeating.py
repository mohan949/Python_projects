def first_repeating_char(s):
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
        if char_counts[char] > 1:
            return char
    return None

print(first_repeating_char('hello'))


def all_repeating_chars(s):
    char_counts = {}
    repeating_chars = []
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
        if char_counts[char] > 1 and char not in repeating_chars:
            repeating_chars.append(char)
    return repeating_chars

print(first_repeating_char('helloo'))
