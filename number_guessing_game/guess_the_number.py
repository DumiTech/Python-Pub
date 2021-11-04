import lib
import random

print(lib.logo)

print("##### Welcome, once you're in, you cannot exit until you won #####")
print("Hope you will survive\n")

print("I'm thinking of a number between 1 and 100.")

winner_number = random.randrange(1, 101)

def choice():
	game_difficulty = input("Choose a difficulty. Type 'hard' either 'easy': ")

	if game_difficulty == 'hard':
		attempts = 5
		print(f'You have {attempts} attempts')
	elif game_difficulty == 'easy':
		attempts = 10
		print(f'You have {attempts} attempts')
	else:
		print("You lose, and all of this because of bad typo")
		quit()
  
	while attempts > 0:
		guess = int(input("\nMake a guess: "))
		if guess == winner_number:
			print("##### You won! #####")
			quit()
		elif guess > winner_number:
			attempts -= 1
			print(f"Too high!\nGuess again.\nYou have {attempts} attempts remaining to guess the number")
		elif guess < winner_number:
			attempts -= 1
			print(f"Too low!\nGuess again.\nYou have {attempts} attempts remaining to guess the number")
  
	if attempts == 0:
		print("### Game over ###")
  
	again = input("\nWanna play again? Type 'y' or 'n': ")
	if again == 'y':
		choice()
	elif again == 'n':
		print('Good luck next time!')
		quit()
	else:
		print("You lose, and all of this because of bad typo")
		quit()
  
      
choice()
