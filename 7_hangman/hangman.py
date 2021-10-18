import random
import hangman_library 
from hangman_library import logo
from hangman_library import stages
from hangman_library import countries

print(logo)
print("""
      You had to guess a country name in Europe
      Some countries may contain two or more words as names
      As convention for this game, a country called 'United States of America' will be merged as 'UnitedStatesOfAmerica'
      Note that all words will be converted to lowercase
      """)

games_is_finished = False
lives = len(stages) - 1

random_country = random.choice(countries).lower()
country_len = len(random_country)

print("Country length: ", country_len)

display = []

for i in range(country_len):
    display += "_"
    
while not games_is_finished:
    guess_increment = 0
    
    guess = input("Guess a letter: ").lower()
    
    print(" \n"*50)
    
    if guess in display:
        print(f"You already guessed {guess}")
        
    for index in range(country_len):
        letter = random_country[index]
        if letter == guess:
            display[index] = letter
    print(f"{' '.join(display)}")
    
    if guess not in random_country:
        lives -= 1
        print(f"\nYou lose a life! The guess was not {guess}")
        if lives == 0:
            games_is_finished = True
            print("You lose!")
    
    if "_" not in display:
        games_is_finished = True
        print("You won!!! Congrats!!!")
        
    print(stages[lives])