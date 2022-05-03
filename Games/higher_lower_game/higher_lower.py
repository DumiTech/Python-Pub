import art, game_data
import random

lives = 1
score = 0
data = game_data.data

def game_logic(lives, score, data):
 
    while lives == 1:
        print(art.logo)
        first_item = random.choice(data)
        print(f"Compare A: {first_item['name']}, a {first_item['description']}, from {first_item['country']}.")
                
                
        print(art.vs)
        second_item = random.choice(data)
        while second_item == first_item:
            second_item = random.choice(data)
        print(f"Against B: {second_item['name']}, a {second_item['description']}, from {second_item['country']}.")
        
        
        # assume first item has the max followers: 
        max_followers = first_item['follower_count']
  
        first_item_followers = first_item['follower_count']
        second_item_followers = second_item['follower_count']
        

        answer = input("\nWho has more followers? Type 'A' or 'B': ")
        if answer == 'A' or answer == 'a':
            answer = first_item_followers
        elif answer == 'B' or answer == 'b':
            answer = second_item_followers
        else:
            print(art.wrong_input)
            # print("\nWrong input.. You lost")
            quit()
        
        
        if first_item_followers < second_item_followers:
            max_followers = second_item_followers


        if answer == max_followers:
            score += 1
            if score >= 1:
                print("\n"*40)
                print("#"*65)
                print(f"       You're right! Current score: {score}.")
                print("#"*65)
        else:
            print(art.lose)
            print("#"*65)
            print("                          Score: ", score)
            print("#"*65)
            lives -= 1
        
    
game_logic(lives, score, data)