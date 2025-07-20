


# for i in range(1, 11):

#     with open('tables.txt','w') as f:
#         f.write((f'2 X {i} = {2*i}\n'))

# f.close()

# with open('tables.txt', 'a') as f:  # Use 'a' to append to the file
#     for i in range(1, 11):
#         f.write(f'2 X {i} = {2*i}\n')  # Add a newline character after each line


def tablefiles(n):
# Open the file once, outside the loop, in append mode ('a')
 for n in range(3):
    with open(f'tables_{n}.txt', 'w') as f:  # Use 'w' if you want to overwrite the file initially
        for i in range(1, 11):
             f.write(f'{n} X {i} = {n*i}\n')  # Write each line with a newline character

tablefiles(3)
