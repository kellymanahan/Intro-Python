class Item:
    def __init__(self, name, description):
        self.name = name 
        self.description = description

    def __str__(self):
        return f"{self.name}"

    def on_grab(self, player):
        print("item picked up")
        # player has item
        newPlayer.item.append(self)
        #remove item from room

        newPlayer.room.item.remove(self)

class Treasure(Item):
    def __init__ (self, name , descrition, value):
        super ().__init__(self, name, descrition)
        self.value = value
        self.picked_up = False
    
    def on_grab(self, player):
        super().on_grab(player)
        if self.picked_up == False:
         #score updated
            newPlayer.score += self.value
            self.pickeup_up == True