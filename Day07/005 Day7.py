word_list=["aardvark", "baboon", "camel"]


import random
chosen_word=random.choice(word_list)
print(f"The randomly chosen word is {chosen_word}")

display=[]
word_length=len(chosen_word)
for _ in range(word_length):
    display+="_"
print(display)
n=0
while not n>word_length:
    n+=1
    guess=input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position is {position}\n and letter is {letter}\n Guessed letter is {guess}")
        if letter == guess:
            display[position]=letter
    print(display)






