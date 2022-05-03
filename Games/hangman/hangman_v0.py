import random
import os

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                     
                   |___/    '''
                   
                   
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']        

print(logo)

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


game_is_finished = False
lives = len(stages) - 1

#list of words from the same family: locations/capitals/countries/domain - CS, eg: Python theory
countries = [
    "Albania",	"Andorra",	"Armenia",	"Austria",	"Azerbaijan",	"Belarus",	"Belgium",
    "Bosnia and Herzegovina",	"Bulgaria",	"Croatia",	"Cyprus",	"Czechia",	"Denmark", "Estonia", 
    "Finland",	"France",	"Georgia",	"Germany",	"Greece",	"Hungary",	"Iceland",	"Ireland",	
    "Italy",	"Kazakhstan",	"Kosovo",	"Latvia",	"Liechtenstein",	"Lithuania",	"Luxembourg",
    "Malta",	"Moldova",	"Monaco",	"Montenegro",	"Netherlands",	"Macedonia",	 "Norway",	
    "Poland",	"Portugal",	"Romania",	"Russia",	"San Marino",	"Serbia",	"Slovakia",	"Slovenia",	
    "Spain",	"Sweden",	"Switzerland",	"Turkey",	"Ukraine",	"United Kingdom", "Vatican City"
]

random_country = random.choice(countries).lower()
country_length = len(random_country)

#make an empty list to update the user input
display = []

#display in this format: _ y _ o _ u _ _ c _ a _ n _ ! _
print("hint: Length of the secret country is: ", country_length)
for _ in range(country_length):
    display += "_"


while not game_is_finished:

    guess_increment = 0

    guess = input("Guess a letter: ").lower()
    clearConsole()     
        
    if guess in display:
        print(f"You already guessed {guess}")

    for position in range(country_length):
        letter = random_country[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")
    
    if guess not in random_country:
        print(f"You lose a life by choosing {guess}, that's not the letter")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose!")
    
    
    if not "_" in display:
        game_is_finished = True
        print('Congrats! You won!!!')
        
    print(stages[lives])
