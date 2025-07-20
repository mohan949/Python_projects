
numbers = [10, 2, 3]
# smallest = min(numbers)
# print(smallest)

# Alternative approach using loop
smallest = numbers[0]
for num in numbers:
    print('before num',num)
    print('before smallest',smallest)
    if num < smallest:
        smallest = num
        print('assigned smallest---> ', smallest)
    print('Num ->',num)
    print('Smallest ->', smallest)
print(smallest)
