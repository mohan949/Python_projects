def find_substring(main_string, sub_string):
    """
    Check if a substring exists in the main string and return its position.
    """
    
    if sub_string in main_string:
        position = main_string.find(sub_string)
        
        return f"Substring '{sub_string}' found at index {position}."
    else:
        return f"Substring '{sub_string}' not found."

# Example usage
main_string = "Hello, welcome to the world of Python programming!"
sub_string = "l"

result = find_substring(main_string, sub_string)
print(result)

m = 'mohan'
print(m.isdigit())