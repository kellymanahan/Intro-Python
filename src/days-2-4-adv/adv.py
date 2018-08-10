from room import Room
from player import Player
from item import Item, Treasure


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}

#Add Items
item = {
    'sword' : Item("small sword", "small sword to fight with"),
    'shield' : Item("wooden shield", "durable shild to protect you")
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#Add to item room
room['outside'].addItem(item['sword'])
room['overlook'].addItem(item['shield'])

#treasure gold, silver

# Make a new player object that is currently in the 'outside' room.
newPlayer = Player(room['outside'])

dir = ""
# Write a loop that:
while not dir == "q":
    def room_info():
# * Prints the current room name
        print(newPlayer.room.name)

# * Prints the current description (the textwrap module might be useful here).
        print(newPlayer.room.description)
# see items in the room
    
    if len( newPlayer.room.items ) == 0:
        print("  nothing")
    else:
        print("There is an item in this room: ")
        for i in newPlayer.room.items:
            print("  " + str(i))

# * Waits for user input and decides what to do.
    dir = input("Where would you like to go? Enter n, w, e, s or q to quit")
    splt_cmd = dir.split()
    if len(splt_cmd) > 1:
            action = splt_cmd[0]
    for i in range(1, len(splt_cmd[i])):
            item += splt_cmd[i] + " "
            item = item.strip()

#grabbing or dropping
if action =="g" or action == "grab":
    for i in newPlayer.room.items:
            if splt_cmd[1] == i.name:
                i.on_grab( newPlayer )
                
    cmd = input("you grabbed an item")
    # else:
    #         print("invalid selection")

#drop  
if action == "d" or action == "drop":
    for i in newPlayer.room.items:
            if splt_cmd[1] == i.name:
                i.on_grab( newPlayer )
                
    cmd = input("you dropped an item")
    # else:
    #         print("invalid selection")
#inventory
if cmd == "i" or cmd == "inventory":
        print("inventory: ")
        if len(newPlayer.items ) == 0:
            print("you don't have anything in your inventory")
        for i in newplayer.item:
            print("\t" + str(i))
#score
if cmd == "score":
        print("score: " + str(newPlayer.score) + "\n")
# If the user enters a cardinal direction, attempt to move to the room there.
if dir == "n":
        if hasattr(newPlayer.room, "n_to"):
            newPlayer.room = newPlayer.room.n_to
        else:
            print("Try another direction")
elif dir == "s":
        if hasattr(newPlayer.room, "s_to"):
            newPlayer.room = newPlayer.room.s_to
        else:
            print("Try another direction")
elif dir == "e":
        if hasattr(newPlayer.room, "e_to"):
            newPlayer.room = newPlayer.room.e_to
        else:
            print("Try another direction")
elif dir == "w":
        if hasattr(newPlayer.room, "w_to"):
            newPlayer.room = newPlayer.room.w_to
        else:
            print("Try another direction")
  
   # Check inventory
elif command[1] in ["i", "inventory"]:
        if len(newplayer.inventory) > 0:
            print("Your inventory is:")
            for i in newPlayer.inventory:
                print(" " + i.description)
        else:
            print("There is nothing in your inventory")
# Print an error message if the movement isn't allowed.
# If the user enters "q", quit the game.
elif dir == "q":
        print("Thank you, come again!")
else:
        print("This movement isn't allowed")