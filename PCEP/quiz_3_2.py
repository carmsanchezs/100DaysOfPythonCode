for i in range (1, 11):
    if i % 2:
        print(i)
    

x = 1
while x < 11:
    if x % 2:
        print(x)
    x += 1
    

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch)
    

modified_str = ""

for digit in "0165031806510":
    if digit == "0":
        modified_str += "x"
        continue
    modified_str += digit
    
print(modified_str)


n = 3
while n > 0:
    print(n + 1)
    n -= 1
else: 
    print(n)
    
print()

n = range(4)
for num in n:
    print(num - 1)
else:
    print(num) 
    
print()

for i in range(0, 6, 3):
    print(i)