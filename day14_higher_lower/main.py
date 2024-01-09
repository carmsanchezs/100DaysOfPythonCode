from random import choice
from game_data import data
from art import logo, vs
from replit import clear


# get a random famous person
def get_random_item():
    return choice(data)
    

# compare if the famous person is not the same
def get_item_B(dictA):
    dictB = get_random_item()
    while dictA['name'] == dictB['name']:
        dictB = get_random_item()
    return dictB

    
# compare followers count
def check_is_user_right(user_answer, dictA, dictB):
    "Return True if the user_answer is correct, and A or B has more followers"
    if user_answer == 'A':
        return dictA['follower_count'] > dictB['follower_count']
    else:
        return dictB['follower_count'] > dictA['follower_count']
        
# global variables
is_user_right = True
score = 0
user_answer = ''
A = B = {}
A = get_random_item()
B = get_item_B(A)

while is_user_right:
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {A['name']}, {A['description']}, {A['country']}, {A['follower_count']} ")
    print(vs)
    print(f"Against B: {B['name']}, {B['description']}, {B['country']}, {B['follower_count']}") 
    user_answer = input("Who has more followers? Type 'A' or 'B': ")
    is_user_right = check_is_user_right(user_answer, A, B)
    print(user_answer)
    clear()
    
    #print(is_user_right(user_answer))
    if is_user_right:
        A = B
        B = get_item_B(A)
    else:
        print(logo)
        print(f"Sorry, that's wrong. final score: {score}")

