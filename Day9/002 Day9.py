programming_dictionary = {"bug": "An error that a prevents the program from running aas expected.",
                          "Function": "A piece of code that you can call over and over again.",
                          "loop": "The Action of doing something over and over again. ",
                          "for loop": "The most popular and useful loop in python"}

print(programming_dictionary["bug"])

print(programming_dictionary)
# define an empty dictionary
# empty_dictionary={}

#wipe an existing dictionary
# programming_dictionary ={}
# print(programming_dictionary)

# edit an item in a dictionary
# programming_dictionary["bug"]= "A moth in your computer. "
# print(programming_dictionary)


#loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


