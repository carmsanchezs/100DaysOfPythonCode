# Prompt the user to enter a word
user_word = input("Enter a word: ")
# and asign it ti the user_word variable.
user_word = user_word.upper()

for letter in user_word:
    # complete the body of the for loop
    if letter in ("A", "E", "I", "O", "U"):
        continue
    print(letter)
