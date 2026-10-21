total=0
print("The Even number with in the range of 100 are following\n")

for number in range(2,101,2):
    print(number)
    total+=number
print(f"The Sum of all the even numbers between 1 and 100 are: {total} ")

total2=0
for number in range(1,101):
    if number%2==0:
        total2+=number
print(f"The Sum of all the even numbers between 1 and 100 are: {total2} ")
