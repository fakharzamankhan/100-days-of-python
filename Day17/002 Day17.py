
# defining class

class User:
    def __init__(self,user_id,user_name):  #constructor
        self.id= user_id                   #attribute
        self.username=user_name
        self.followers=0
        self.following=0
    def follow(self,user):
        user.followers +=1
        self.following +=1



user_1=User("001","Hassan")
user_2=User("002","Ali")
user_1.follow(user_2)
print(user_1.username)
print(user_1.id)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)



# class Car:
#     # def __init__(self,seats):
#     #     self.seats =seats
#     #     print(self.seats)
#     def enter_race_mode(self):
#         self.seats=4
#         print(self.seats)
# my_car=Car()
# my_car.enter_race_mode()




