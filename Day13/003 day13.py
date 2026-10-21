year = int(input("which year do you want to check? "))
print(type(year))

if year%4 ==0:
    if year%100 == 0:
        if year %400 ==0:
            print("Its a leap year. ")
        else:
            print("Not leap year. ")
    else:
        print("Leap year. ")
else:
    print("Not a leap year. ")
