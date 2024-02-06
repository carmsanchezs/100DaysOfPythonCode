c0 = int(input("Enter the number: "))

if c0 <= 0:
    print("Enter an integer and positive number, grater than zero.")
    
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 /= 2
    else:
        c0 = 3 * c0 + 1
    steps += 1
    print(round(c0))

print("steps =", steps)
