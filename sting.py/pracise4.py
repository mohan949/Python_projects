fruits = []  # Initialize an empty list

# Define the number of fruits you want to input
num_of_fruits = int(input("How many fruits do you want to enter? "))

# Loop to input fruit names
for _ in range(num_of_fruits):
    f1 = input('Enter the fruit name: ')
    fruits.append(f1)

# Print the list of fruits
print(fruits)
