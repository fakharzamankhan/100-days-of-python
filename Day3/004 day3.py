print("Welcome to the rollercoaster!")
height=int(input("What is your height in Cm?"))

if height>=120:
    print("You can ride the rollercoaster!")
    print("Enter your age!")
    Age=int(input("What is your age?"))
    if Age<=18:
        print("Please pay $7 ")
    elif Age >=12 and Age <=18:
        print("Please pay $5")
    else:
        print("Please pay $12")
else:
    print("Sorry You have to grow taller before you can ride. ")

# >
# >
# >=
# <=
# ==
# !=

