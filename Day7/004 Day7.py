word_list=["Aardvark", "baboon", "camel"]


#randomly choose a word from the word_list and
# assign it to a variable called chosen_word

import random
chosen_word = random.choice(word_list)

#TODO_2 -Ask the user to guess a letter and assign their answer to a variable
#called Guess. Make guess lowercase

guess=input("Enter your guess: ").lower()
print("You guessed", guess)

#TODO_3 _ check if the letter the user guessed is
# one of the letters in the chosen_word.
for letter in chosen_word:
    if letter == guess:
        print("Correct")
    else:
        print("Wrong")


