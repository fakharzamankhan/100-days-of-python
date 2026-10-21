# List Comprehension

# numbers= [1,2,3]
# new_numbers=[n+1 for n in numbers]
# print(new_numbers)
#
name="Angela"

new_list =[letter for letter in name]
print(new_list)

range_list= [num*2 for num in range(1,5)]
print(range_list)

names = ["Alex","Healey","Sara","John","David","Queen","Beth"]
short_names=[name for name in names if len(name) <5]
print(short_names)

long_names=[name.upper() for name in names if len(name) >= 5 ]
print(long_names)

