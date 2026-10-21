print("Welcome To Treasure Island.")
print("Your mission is to find the treasure.")
choice1=input('You\'re at the a crossroad, where do you want to go ? "Right" or "Left\n".').lower()
if choice1=="left":
    choice2=input('You have come to a lake. This is an island in the middle of the lake.Do you want to "swim" or "wait\n" .').lower()
    if choice2=="wait":
        choice3=input("Which door do you want to go? R ,B, Y? ")
        if choice3=="Y":
            print("Wow You win the Game!")
        elif choice3=="R" or choice3=="B":
            print("You enter a door of beasts. Game Over. Try Again")
        else:
            print("invalid input! Chose the Right door.")
    elif choice2=="swim":
        print("Game Over.Try again")
    else:
        print("Invalid Input!")
elif choice1=="right":
    print("You fell into the hole. Game over. Try Again")
else:
    print("Invalid Input!")
