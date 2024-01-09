# Calculator
from art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    
    for symbol, function in operations.items():
        print(symbol)
    
    should_continue = True
    
    while should_continue:
        operation_symbol = input("Pick another operation: ")
        num2 = float(input("What's the next number?: "))
        result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if answer == 'n':
            should_continue = False
            calculator()
        else:
            num1 = result
        


calculator()