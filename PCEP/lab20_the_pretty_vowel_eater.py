word_without_vowels = ""

# Prompt the user to enter a word
# and asign it ti the user_word variable.
user_word = input("Enter a word: ").upper()

for letter in user_word:
    # complete the body of the for loop
    if letter in ("A", "E", "I", "O", "U"):
        continue
    word_without_vowels += letter

# print the word assigned to word_without_vowels
print(word_without_vowels)
