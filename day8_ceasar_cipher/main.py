from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

len_alphabet = len(alphabet)

def ceasar(some_text, shift_amount, direction):
    
    result_text = ""
    
    for letter in some_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if direction == "encode":
                new_index = index + shift_amount
                if (new_index >= len_alphabet):
                    new_index -= len_alphabet
            elif direction == "decode":
                new_index = index - shift
            result_text += alphabet[new_index]
        else:
            result_text += letter

    print(f"The {direction}d text is: {result_text}")
    

answer = "yes"
while answer == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(text, shift, direction)
    answer = input("Types 'yes' if you want to go again. Otherwise type 'no'.\n")

print("Goodbye")




