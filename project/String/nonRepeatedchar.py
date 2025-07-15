

# def non_repeating_elements(s):
#     for char in s:
#         if s.count(char) ==1:
#          return char
#     return None
# print(non_repeating_elements('mohhan'))



def non_repeating_elements(s):
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
      #  print(char_counts[char])

    non_repeating_chars = []
    for char, count in char_counts.items():
        if count == 1:
            non_repeating_chars.append(char)

    return non_repeating_chars

print('---> ',non_repeating_elements('mohhan'))



