print("Welcome to the Rollercoaster!")
height= int(input("Enter your height in m: "))
bill=0
if height>=120:
    print("You can ride the Rollercoaster!")
    print("Enter your Age.")
    age= int(input("What is your Age? : "))
    if age<=12:
        bill=5
        print("Child tickets are $5")
    elif 12 <= age <= 18:
        bill=7
        print("Youth tickets are $7")
    else:
        bill=12
        print("Adult tickets are $12")
    want_photo=input("Do you want your Photo? Yes or No: ")
    if want_photo=="y":
        bill+=3
    print("Your Bill is: $"+str(bill))
else:
        print("Sorry You have to Grow taller to ride the Rollercoaster!")



































