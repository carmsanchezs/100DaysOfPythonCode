import random
from hangman_art import logo, stages
from hangman_words import word_list

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
display = ["_" for letter in chosen_word]
lives = 6
end_of_game = False

print(logo)

# testing
print(f"Psssst, the solution is {chosen_word}")

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for index in range(len(chosen_word)):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    if not "_" in display:
        end_of_game = True
        print("You win.")

    if not lives:
        end_of_game = True
        print("You lose. Try again.")

    print(stages[lives])

    print(' '.join(display))
