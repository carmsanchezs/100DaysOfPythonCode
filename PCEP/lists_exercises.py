list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2  # borra la referencia

print(list_3)


my_list = [1, 2, "in", True, "ABC"]
print(1 in my_list)
print("A" not in my_list)
print(3 not in my_list)
print(False in my_list)