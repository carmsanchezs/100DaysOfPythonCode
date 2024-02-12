hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat

# Step 1. Write a line of code that prompts the user 
# to replace the middle number with an integer number entered
# by the user
number = int(input("Enter the new number: "))
hat_list[2] = number

# Step 2: Write a line of code that removes the last element from the list
del hat_list[-1]

# Step 3: write the line of code that prints the lengh of the existing list.
print(len(hat_list))

print(hat_list)
