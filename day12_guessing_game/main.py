#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo


def random_number():
    return random.randint(1, 101)


def decrease_attempts(current_attempt):
    return current_attempt - 1


level = "easy"
attempts = 0
is_game_continued = True

print(logo)
print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")
random_number = random_number()

print(f"Pssst, the correct answer is: {random_number}")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == 'easy':
    attempts = 10
else:
    attempts = 5

print(f"You have {attempts} remaining to guess the number.")

while attempts > 0:
    attempts = decrease_attempts(attempts)
    number_guessed = int(input("Make a guess: "))

    if number_guessed == random_number:
        print(f"You got it! The answer was: {random_number}")
        break
    elif number_guessed > random_number:
        print("Too high.")
    else:
        print("Too low.")
        
    print(f"You have {attempts} remaining to guess the number.")


