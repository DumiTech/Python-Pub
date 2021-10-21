import logo_Caesar_Cypher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cypher_direction):
    end_text = ''
    if cypher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            if new_position >= len(alphabet) or new_position <= len(alphabet):
                new_position = new_position % len(alphabet)
            end_text += alphabet[new_position]
        else:    
            end_text += letter
    print(f"{cypher_direction}d result is: {end_text}")


is_finished = False
while not is_finished:
    
    direction = ''
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
        if direction == 'encode' or direction == 'decode':
            break

    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    
    caesar(start_text = text, shift_amount = shift, cypher_direction = direction)    
    
    restart = ''
    while True:
        restart = input("Type 'yes' if you want to go again, type 'no' if you want to quit.\n")
        if restart == 'yes':
            break
        elif restart == 'no':
            is_finished = True
            print("See you next time!")
            break
    
        