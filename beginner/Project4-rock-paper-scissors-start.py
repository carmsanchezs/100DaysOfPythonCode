rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
options = ["R", "P", "S"]
images = [rock, paper, scissors]

# computer option 
computer_option = random.randint(0,2)

# user option
user_input = input("""
[R] - Rock
[P] - Paper
[S] - Scissors
""")
user_option = options.index(user_input)

print("Computer choise:")
print(images[computer_option])

print("User choise:")
print(images[user_option])

# whe the computer win
if (computer_option == 0 and user_option == 2) or (computer_option == 2 and user_option == 1) or (computer_option == 1 and user_option == 0):
    print("Computer Win.")
elif (user_option == 0 and computer_option == 2) or (user_option == 2 and computer_option == 1) or (user_option == 1 and computer_option == 0):
    print("User Win.")
else:
    print("Draw. Try again.")
    
