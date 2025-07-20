list1 = ['mango', 'apple','pineapple','grapes']

# i =0
# while(i<len(list1)):
#     print(list1[i])
#     i+=1

# list2 = list(reversed(list1))
# print(list2)

# for _ in list1:
#       print(_)

# enter user input in list

list2 =[]

for _ in range(3):
    x = input(f'Enter the {_} in the list : ')
    list2.append(x)

print(list2)

reversed_list =[]
for i in range(len(list2)-1,-1,-1):
    reversed_list.append(list2[i])

print(reversed_list)

print('Length of list is ',len(reversed_list))

# using while loop

whilelist = []  # Initialize an empty list

while True:  # Infinite loop, will stop with 'break'
    x = input(f'Enter the element in list: ')
    
    if x == '999':  # Check if the input is '999'
        break  # Exit the loop
    
    whilelist.append(x)  # Add the input to the list

# Print the final list
print("Your list:", whilelist)

