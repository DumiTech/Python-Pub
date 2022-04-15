# Instance attributes are accessed by: object.attribute
# Attributes are looked First in the instance and THEN in the class

import random


class Dice:
    """Closer number to the winner_number will win."""

    winner_number = random.randint(1, 6)  # class attribute

    def inp(self):
        self.user_input = int(input("\nEnter a number between 1 and 6: "))
        print("\nYou choose:", self.user_input)
        return self.user_input

    def computer(self):
        self.random_val = random.randint(1, 6)  # instance attribute
        print("Computer choose:", self.random_val)
        return self.random_val

    def winner(self):
        print(f"\nWinner number is: {self.winner_number}")
        if self.user_input >= 7 or self.user_input <= 0:
            return "\nYou cheated.. Computer won!"
        elif abs(self.user_input - self.winner_number) == abs(self.random_val - self.winner_number):
            return "\nDraw, no winner today!"
        elif abs(self.user_input - self.winner_number) > abs(self.random_val - self.winner_number):
            return "\nComputer won! Congrat!!!"
        else:
            return "\nHuman won! Congrat!!!"


obj = Dice()
obj.inp()
obj.computer()
print(obj.winner())
