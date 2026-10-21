print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
price=0
if size == "S":
    price+=15
elif size == "M":
    price+=20
elif size == "L":
    price+=25
else:
    print("Sorry You have to choose a size of Pizza!")
add_pepperoni=input("Do you want pepperoni?: y or n: ")
if add_pepperoni == "y" and size == "S":
    price+=2
elif add_pepperoni == "y" and (size == "M" or size == "L"):
    price+=3
else:
    print("Sorry You have to choose a size of Pizza!")

extra_cheese=input("Do you want extra cheese?: y or n: ")
if extra_cheese == "y":
    price+=1
print(f"Your Total Bill is: ${price}")
