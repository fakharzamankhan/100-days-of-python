height= float(input("enter your height in inches: "))
weight= int(input("enter your weight in pounds: "))


if height > 3:
    raise ValueError("Your height is too high")
bmi=weight/(height**2)
print(bmi)
