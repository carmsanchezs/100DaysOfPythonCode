def is_prime(num):
    yes_it_is = True
    for d in range(2, num):
        if num % d == 0:  # num is divisible by d 
            yes_it_is = False
            break
    return yes_it_is


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
