# #split string method
# import random
#
#
# names_string = input("Give me everybody's names separated by comma.")
# names = names_string.split(",")
# print(names)
#
# num_items=len(names)
# random_choice=random.randint(0,num_items-1)
# print(random_choice)
#
# person=names[random_choice]
# print(person+"is Going to buy the meal today.")
import random

names_string=input("Give me everybody's names separated by a comma. ")
names_list=names_string.split(",")
print(names_list)

num_items=len(names_list)
random_choice=random.randint(0,num_items-1)
print(random_choice)

person=names_list[random_choice]
print(person+"is going to pay the bill for meal")

