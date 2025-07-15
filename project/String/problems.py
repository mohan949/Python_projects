import re

def extract_emails(text):
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

text = "Please contact us at support@example.com or sales@company.org."
print(extract_emails(text))  # Output: ['support@example.com', 'sales@company.org']

def word_frequency(s):
    words = s.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


print(word_frequency('hello my name is mohan'))


import re

def is_valid_url(s):
    pattern = re.compile(r"https?://(?:www\.)?[a-zA-Z0-9./]+")
    return bool(pattern.match(s))

print(is_valid_url("https://example.com"))  # Output: True
print(is_valid_url("example.com"))          # Output: False
