word_list=["aardvark", "baboon", "camel"]


import random
stages = [ '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']

end_of_game= False
lives=6
chosen_word=random.choice(word_list)
print(f"The randomly chosen word is {chosen_word}")

display=[]
word_length =len(chosen_word)
for _ in range(word_length):
    display+="_"
print(display)



while not end_of_game:
    guess=input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")

        if letter == guess:
            display[position]=letter

    if guess is not chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print(f"You lost! The word was {chosen_word}")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game=True
        print("You Win")


    print(stages[lives])






