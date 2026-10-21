


import random
import hangman_words
chosen_word=random.choice(hangman_words.word_list)
end_of_game= False
lives=6
from hangman_art import logo,stages
print(logo)
print(f"The randomly chosen word is {chosen_word}")

display=[]
word_length =len(chosen_word)
for _ in range(word_length):
    display+="_"
print(display)



while not end_of_game:
    guess=input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have Already Guessed {guess}")


    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")

        if letter == guess:
            display[position]=letter
    if guess not in chosen_word:
        print(f"You Guessed {guess}, that's not in the word.You Lose a life ")
        lives -= 1
        if lives == 0:
            end_of_game =True
            print("You lose")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game=True
        print("You Win")

    print(stages[lives])






