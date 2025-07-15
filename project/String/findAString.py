def count_substring(string, sub_string):
    count = 0
    print(len(string), len(sub_string))
    print('len --> ',len(string) - len(sub_string)+1)
    for i in range(len(string) - len(sub_string) + 1):
        # Check if the substring matches starting from the current position
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = 'abcdcdc'
    sub_string = 'cdc'
    print(count_substring(string, sub_string))
