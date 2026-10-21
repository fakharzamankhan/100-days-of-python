
#Python does not have the block scope
game_level=3

def create_enemy():
    new_enemy=""
    enemies=["skeleton","Zombie","Alien"]
    if game_level < 5:
        new_enemy=enemies[0]
    print(new_enemy)
