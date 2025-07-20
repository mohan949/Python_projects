# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number : "))

# x = a+b
# y = a-b
# z = a*b

# print('''Choose which operation to be peformed2
#             x = add 
#             y = sub
#             z = mult
#              ''') 


# def exit(): 
#         print("exit")

# c = (input("Choose : "))
# # if c == "add": print(x)
# # if c == "sub": print(y)
# # if c == "mut": print(y)
# i = False
# while i == False :
#     if c == "add": print(x)
#     elif c == "sub": print(y)
#     elif c == "mut": print(y)
#     elif c == "exit" : exit()
#     break


def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    x = a + b
    y = a - b
    z = a * b

    print('''Choose which operation to be performed:
    add - Addition
    sub - Subtraction
    mult - Multiplication
    exit - Exit
    ''')

    while True:
        c = input("Choose an operation: ").lower()
        if c == "add":
            print(f"The result of addition is: {x}")
        elif c == "sub":
            print(f"The result of subtraction is: {y}")
        elif c == "mult":
            print(f"The result of multiplication is: {z}")
        elif c == "exit":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid operation.")

# Run the main function
main()







