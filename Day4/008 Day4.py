import random

rock='''
    _____
---`  ___)
      (____)
      (____)
      (___)
---.__(__)
'''
paper= '''

    _____
---`  ___)___
        _____)
        ______)
       ______)
---._______)
'''
scissors= '''

    ______
---`   ___)___
         _____)
       ________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors]
user_choice=int(input("What do you want to choose? Press 1 for 'Rock',Press 2 for 'Paper',Press 3 for 'Scissors' "))
if user_choice>=3 or user_choice<0:
    print("You chose a wrong option, You lose!")
else:
    print(f"You chose {game_images[user_choice]}")

    computer_choice=random.randint(0,2)
    print("Computer chose",game_images[computer_choice])
    if user_choice ==0 and computer_choice==2:
        print("you win !")
    elif computer_choice==0 and user_choice==2:
        print("You lose !")
    elif computer_choice==user_choice:
        print("It is a Draw! ")
    elif computer_choice >user_choice:
        print("You lose !")
    elif user_choice > computer_choice:
        print("You Win! ")




