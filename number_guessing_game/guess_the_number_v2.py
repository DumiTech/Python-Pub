import lib
import random

print(lib.logo)

easy_game_difficulty = 10
hard_game_difficulty = 5


def choice():
	game_difficulty = input("Choose a difficulty. Type 'hard' either 'easy': ")

	if game_difficulty == 'hard':
		return hard_game_difficulty
	elif game_difficulty == 'easy':
		return easy_game_difficulty
	else:
		print("You lose, and all of this because of bad typo")
		quit()

def check_input(winner_number, guess, turns):
	if guess > winner_number:
		print(f'Too high.')
		return turns - 1
	elif guess < winner_number:
		print('Too low.')
		return turns - 1
	else:
		print(lib.win)

  
def game():
	print("##### Welcome, once you're in, you cannot exit until you won #####")
	print("Hope you will survive\n")
	print("I'm thinking of a number between 1 and 100.")

	winner_number = random.randrange(1, 101)
	turns = choice()

	guess = 128
	while guess != winner_number:
		print(f"\nYou have {turns} attempts remaining.")
		guess = int(input("Make a guess: "))
  
		turns = check_input(winner_number, guess, turns)
		if turns == 0:
			print("\n ### You've run out of guesses, you lose. ###")
			play_again = input("\nType 'yes' to play again, or 'no' in order to give up: ")
			if play_again == 'yes':
				game()
			else:
				print(lib.lose)
				quit()
		elif guess != winner_number:
			print("Guess again!")

game()