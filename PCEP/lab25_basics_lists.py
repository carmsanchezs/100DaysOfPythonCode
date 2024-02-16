my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

temp_list = []

for element in my_list:
    if element in temp_list:
        continue
    else:
        temp_list.append(element)

print("The list with unique elements only:")
print(temp_list)
