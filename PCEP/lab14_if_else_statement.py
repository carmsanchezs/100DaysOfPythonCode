# no terminado, no entendí las reglas
income = float(input("Enter the annual income: "))

if income < 556.02:
    tax = 0
elif income < 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * .32

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
