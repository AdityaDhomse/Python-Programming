import art
import random
import data

def random_choice():
    random_choice = random.choice(data.data)
    return random_choice

def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']

    return f"{account_name}, a {account_description}, from {account_country}"  

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
    
# Start

print(art.logo)

score = 0
game_should_continue = True
random_choice_B = random_choice()

while game_should_continue:
     
    random_choice_A = random_choice_B
    random_choice_B = random_choice()

    if random_choice_B == random_choice_A:
        random_choice_B = random_choice()

    print(f"Compare A: {format_data(random_choice_A)}")

    print(art.vs)

    print(f"Against B: {format_data(random_choice_B)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    print("\n" * 20)
    print(art.logo)

    A_followers = random_choice_A['follower_count']
    B_followers = random_choice_B['follower_count']

    is_correct = check_answer(guess, A_followers, B_followers)

    if is_correct:
        score += 1
        print(f"You're right! Current score = {score}")
    else:
        print(f"Sorry, that's wrong. Final score = {score}")
        game_should_continue = False