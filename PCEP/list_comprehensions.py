squares = [x ** 2 for x in range(10)]
print(squares)

twos = [2 ** i for i in range(10)]
print(twos)

odds = [x for x in squares if x % 2 != 0]
print(odds)