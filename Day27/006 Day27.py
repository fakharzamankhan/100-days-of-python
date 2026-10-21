def calculate(n,**kwargs):
    print(kwargs ) #it's a dictionary
    for key, value in kwargs.items():
        print(key)
        print(value)

    #print(kwargs["add"])
    #print(kwargs["multiply")

    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)



calculate(2,add=3,multiply=5)

class Car:
    def __init__(self,**kw):
        self.make =kw["make"]
        # self.model = kw.("model")
        self.model=kw.get("model")
        self.color=kw.get("color")
        self.seats=kw.get("seats")


# my_car =Car(make="Nissan",model="GT-R")
my_car =Car(make="Nissan")

print(my_car.model)
print(my_car.make  )

