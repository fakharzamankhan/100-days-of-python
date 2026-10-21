# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
    #Access key and value
    # print(key, value)
    # pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    # print(row.student)
    # print(row.score)
    # print(index)
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


"""catching the exception in nato_phonetic_Alphabet.py"""
phonetic_dict={}
import pandas as pd
#TODO 1. Create a dictionary in this format:
data=pd.read_csv("nato_phonetic_alphabets.csv")
print(data)
phonetic_dict={row.letter:row.code for (ind, row) in data.iterrows()}
print(phonetic_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic_dict():
    word=input("Enter a word:").upper()
    try:
        output_list=[phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters accepted")
        generate_phonetic_dict()
    else:
        print(output_list)

generate_phonetic_dict()
