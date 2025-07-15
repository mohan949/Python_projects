# Writing to a file
with open('test11.txt', 'w') as f:
    f.write("Hello, World!")

# Reading from a file
with open('test.txt', 'r') as f:
    content = f.read()
    print(content)  # Output: Hello, World!


with open('prezentai.txt', 'w') as f:
    f.write("This is my presentation.")

with open('prezentai.txt', 'r') as f:
    content = f.read()
    print(content)