import random

def deal_card():
    """Returns a random card from the deck."""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return a score."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_s, computer_s):
    if user_s==computer_s:
        return "Draw"
    elif computer_s==0:
        return "Lose, opponent has a blackjack"
    elif user_s==0:
        return "Win, with blackjack"
    elif user_s>21:
        return "You went over, you lose"
    elif computer_s>21:
        return "Opponent went over, you win"
    elif user_s>computer_s:
        return "You win"
    else:
        return "You lose"

def play_game():
    user_card=[]
    computer_card=[]
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    is_game_over=False
    while not is_game_over:

        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)

        print(f"Your cards are {user_card} Current score is  {user_score}")
        print(f"Computer's first card is {computer_card[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("Type y to get another card, type 'n' to pass: ")
            if  user_should_deal=="y":
                user_card.append(deal_card())
            else:
                is_game_over=True

    while computer_score!=0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your final hand is {user_card} Current score is  {user_score}")
    print(f"Computer's final hand is {computer_card} computer's final score is  {computer_score}")
    print(compare(user_score,computer_score))


while input("Do you want to play Blackjack? Type 'y' or 'n'")=='y':
    play_game()







