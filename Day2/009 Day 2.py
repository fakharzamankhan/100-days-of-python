print("Welcome to the Tip Calculator!")
bill=float(input("What is your bill?\n"))
tip=int(input("What percentage tip would you like to give? 10, 12 or 15\n"))
people=int(input("How many people to split the bill? \n? "))
tip_percentage=tip/100
total_tip=bill*tip_percentage
total_bill=bill+total_tip
bill_per_person=total_bill/people
print(f"Each person should pay {bill_per_person:.2f}")


