from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program.")

bidders = []
continue_program = True


def add_dic():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders.append({"name": name, "bid": bid})


while continue_program:
    add_dic()
    answer = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if answer == "no":
        continue_program = False
    clear()


winner = ""
max_bid = 0
for element in bidders:
    if element["bid"] > max_bid:
        max_bid = element["bid"]
        winner = element["name"]

print(f"The winner is {winner} with a bid of {max_bid}")

# see pythontutor, or thonny