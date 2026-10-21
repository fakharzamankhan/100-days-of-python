
print("Welcome to the leap year calculator.")
year=int(input("Enter a leap year.\n"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"The Year {year}, is a leap year.")
        else:
            print(f"The Year {year}, is not a Leap year.")
    else:
        print(f"The Year {year}, is Leap year.")
else:
    print(f'The Year {year}, is not a Leap year.')
