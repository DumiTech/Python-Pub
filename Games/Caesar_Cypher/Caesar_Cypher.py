import logo_Caesar_Cypher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

logo_Caesar_Cypher
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")



text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

        
def encrypt(plain_text, shift_amount):
    cypher = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position >= len(alphabet):
            new_position -= len(alphabet)
        cypher += alphabet[new_position]
    print(f"### The encoded text is: '{cypher}' ###") 

           
def decrypt(plain_text, shift_amount):
    decipher = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        decipher += alphabet[new_position]
    print(f"### The decoded text is '{decipher}' ###")
    
def check(direction):
    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)
    else:
        print("An error occurred, check the instruction manual\n", "Please try again later")
        quit()
            
check(direction)
