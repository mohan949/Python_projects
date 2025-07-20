# s = 'mohan'
# l = []
# for i in s:
#     i = l.append(i)
# print(l)


# n = [1, 2,3,4,5]
# start = 0
# end = len(n)-1
# print(end)


# a = 'mohan'
# b = ''
# s = 0
# p = len(a)-1    
# while  s < p:
#     a , b = b, a

#     s += 1
#     p -=1
# print(b)     


# a = 'mohan'
# b = ''
# print(a[1::-1])
# s = len(a)-1
# while s >=0:
#     b = b + a[s]
#     s = s - 1
# print(b)    



# s = 5
# while s>=0:
#     print('*')
#     s = s - 1

def reverse_list(numbers):
    start = 0
    end = len(numbers) - 1

    while start < end:
        # Swap the elements
        numbers[start], numbers[end] = numbers[end], numbers[start]
        
        # Move the pointers
        start += 1
        end -= 1

    return numbers

# Example usage
nums = [1, 2, 3, 4, 5]
print("Original list:", nums)
reversed_nums = reverse_list(nums)
print("Reversed list:", reversed_nums)
