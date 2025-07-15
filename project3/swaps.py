
# # a = ['m','o','h','a','n']
# # b = ['k','a', 'v', 'i', 't', 'a']



# # # a, b = b ,a
# # # print(a)
# # # print(b)
# # print('-----')
# # a[0] , b[len(b)-1] = b[0], a[len(a)-1]


# # print(a)
# # print(b)



# def reverse_list(numbers):
#     start = 0
#     end = len(numbers) - 1

#     while start < end:
#         # Swap the elements
#         numbers[start], numbers[end] = numbers[end], numbers[start]
        
#         # Move the pointers
#         start += 1
#         end -= 1

#     return numbers

# # Example usage
# nums = [1, 2, 3, 4, 5]
# print("Original list:", nums)
# reversed_nums = reverse_list(nums)
# print("Reversed list:", reversed_nums)




a = input()
# b = a.split()
# print(b)
# print(b[1])
# for i in b:
#     print(i)
b = a.split()

a_list = list(b)
print(a_list)