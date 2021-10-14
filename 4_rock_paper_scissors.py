import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
print(rock, paper, scissors)

user_input = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n'))

computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")

if 0 < user_input > 2:
    print("Bad decision! Your input crashed the program. Please read the instructions. ")
    quit()

if computer_choice == 0 and user_input == 0 or computer_choice == 1 and user_input == 1 or computer_choice == 2 and user_input == 2:
    print('Draw')
elif computer_choice == 0 and user_input == 1 or computer_choice == 1 and user_input == 2 or computer_choice == 2 and user_input == 0:
    print("You win!!! Congrats xD")
else:
    print(
        '01000011 01101111 01101101 01110000 01110101 01110100 01100101 01110010 00100000 01110111 01101111 01101110 00100001')
