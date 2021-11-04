import art
import random

Jack = 10
Queen = 10
King = 10
Ace = 11

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace]

print(art.logo)


def play_blackjack(your_amount, computer_amount):
    your_cards = random.choices(cards, k=2)
    your_amount = your_cards[0] + your_cards[1]
    print(f"Your cards: {your_cards}")
    # print(your_amount)    #test

    computer_cards = random.choices(cards, k=2)
    computer_amount = computer_cards[0] + computer_cards[1]
    print(f"Computer's cards [{computer_cards[0]}, X]")

    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == 'y':
        your_cards += random.choices(cards, k=1)
        print(f"Your cards: {your_cards}")
        your_amount += your_cards[2]
        computer_cards += random.choices(cards, k=1)
        print(f"Computer's hand: {computer_cards}")
        computer_amount += computer_cards[2]
        winner(your_amount, computer_amount)
    elif another_card == 'n':
        if computer_amount <= 11:
            computer_cards += random.choices(cards, k=1)
            computer_amount += computer_cards[2]
            if computer_amount <= 14:
                computer_cards += random.choices(cards, k=1)
                computer_amount += computer_cards[3]
        print(f"Computer's final hand: {computer_amount}")
        print(f"Computer`s cards: {computer_cards}")
        winner(your_amount, computer_amount)
    else:
        print("You lost.. Bad typo!")


def winner(your_amount, computer_amount):
    if your_amount == 21 and computer_amount == 21:
        print("Equality! <<Jackpot>>")
    elif your_amount == computer_amount:
        print("Equality")
    elif your_amount == 21:
        print("Jackpot! You win!!!")
    elif your_amount <= 21 and computer_amount > 21:
        print("You win!")
    elif your_amount > 21 and computer_amount <= 21:
        print("Bust!")
        print("Computer win!")
    elif your_amount > 21 and computer_amount > 21:
        if your_amount < computer_amount:
            print("You win!")
        elif your_amount > computer_amount:
            print("Bust!")
            print("Computer win!")
    elif your_amount < 21 and computer_amount < 21:
        if your_amount > computer_amount:
            print("You win!")
        elif your_amount < computer_amount:
            print("Bust!")
            print("Computer win!")


play_blackjack(your_amount='', computer_amount='')
