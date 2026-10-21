from art import logo,vs
from game_data import data
import random

""" Format account data into printable format."""
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Check if guess is correct. Take the user guess and follower counts."""
    ## If Statement
    if a_followers > b_followers:
         return user_guess=="a"
    else:
         return user_guess=="b"


# Add art.
print(logo)
score=0
game_should_continue =True
account_b = random.choice(data)
# Make game repeatable.
while game_should_continue:
    # Generate a random account from the game data.
    # Make B become the next A.
    account_a=account_b
    account_b=random.choice(data)

    while account_a==account_b:
        account_b=random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
        # Ask user for a guess.
    guess=input("Who has more followers? 'A' or 'B': ").lower()
        # Check if user is correct.
        ## Get follower count.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct =check_answer(guess, a_follower_count,b_follower_count)

        # Feedback.
    if is_correct:
        score+=1
        print(f"You are right! Current Score: {score}")

     # Score Keeping.
    else:
        game_should_continue =False
        print(f"Sorry,that's wrong. Final score: {score}")


    # Clear screen between rounds.
