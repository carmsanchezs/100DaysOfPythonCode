from coffee_data import MENU, resources


# TODO: Asking user
def asking_user():
    answer = input("What would you like? (espresso/latte/cappuccino): ")
    return answer


# TODO: Print Report
def print_report(total_water, total_milk, total_coffee, total_money):
    print(f"Water: {total_water}ml")
    print(f"Milk: {total_milk}ml")
    print(f"Coffee: {total_coffee}g")
    print(f"Money: ${total_money}")

# TODO: Turn off cofee machine

# TODO: Check resources sufficient
def enough_resources(total_water, total_milk, total_coffee, drink):
    if total_water < MENU[drink]['ingredients']['water']:
        print("Sorry there is not enough water")
        return False
    elif total_milk < MENU[drink]['ingredients']['milk']:
        print("Sorry there is not enough milk")
        return False
    elif total_coffee < MENU[drink]['ingredients']['coffee']:
        print("Sorry there is not enough coffee")
        return False
    else:
        return True


# TODO: Process coins
def process_coins(drink):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    quarters *= 0.25
    dimes *= 0.1
    nickles *= 0.05
    pennies *= 0.01

    return quarters + dimes + nickles + pennies


# TODO: Check transaction successful
def transaction_successful(drink, money_inserted):
    if money_inserted >= MENU[drink]['cost']:
        change = round(money_inserted - MENU[drink]['cost'], 2)
        print(f"Here is {change} in change")
        return True
    else: 
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO: make coffee
def make_coffee(total_water, total_milk, total_coffee, drink):
    total_water -= MENU[drink][]
    

total_water = resources['water']
total_milk = resources['milk']
total_coffee = resources['coffee']
total_money = 0

print_report(total_money)
