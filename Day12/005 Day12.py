from random import randint
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

def check_answer(guess,ans,turns):
    """Checks answer against. Return the number of turns left"""
    if guess>ans:
        print("You guessed too high")
        return turns -1
    elif guess<ans:
        print("You guessed too low")
        return turns -1
    else:
        print("You guessed correct")

def set_difficulty():
    level=input("Chose a difficulty level 'easy' or 'hard: ")
    if level=="easy":
         return EASY_LEVEL_TURNS
    else:
         return HARD_LEVEL_TURNS


def game():
    from art import logo
    print(logo)
    print("Welcome to the Guessing game!")
    print("I am thinking of a Guessing game between 1 and 100.")
    answer=randint(1,100)
    print(f"Psst, the correct answer {answer} ")

    turns=set_difficulty()

    user_guess=0
    while user_guess!=answer:
        print(f"You have {turns} attempts remaining to guess")
        user_guess=int(input("Make a guess: "))
        turns=check_answer(user_guess,answer,turns)
        if turns==0:
            print("you run out of guesses. you lose")
            return
        elif user_guess!=answer:
            print("Guess again")

game()
