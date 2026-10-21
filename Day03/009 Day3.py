print("Welcome to the rollercoaster!")
height=int(input("What is your height in Cm?"))
bill=0
if height>=120:
    print("You can ride the rollercoaster!")
    print("Enter your age!")
    Age=int(input("What is your age?"))
    if Age<=12:
        bill=5
        print("Child tickets are $5 ")
    elif 12 <= Age <= 18:
        bill=7
        print("Youth tickets are $7")
    elif 45 <= Age <= 55:
        print("Everything is going to ok. Have a free ride on us! ")

    else:
        bill=12
        print("Adult tickets are $12")
    want_photo=input("Do you want a photo taken ?Yes Or NO.")

    if want_photo=="y":
        bill=bill+3
    print(f"Your Final bill is {bill}")
else:
    print("Sorry You have to grow taller before you can ride. ")

# >
# >
# >=
# <=
# ==
# !=

