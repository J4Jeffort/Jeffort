print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first = input("To the left is a river. To the right is a long dirt road. Which way will you go? Type Left or Right: ").lower()

if first == "left":
    second = input("You arrive at the river and you see that across the river is your crush waving you over!\nDo you swim to her or wait for a boat? Type Swim or Wait:  ").lower()
    if second == "wait":
        print("You chose to make her wait!? You're insane! She looks pissed! Good luck the rest of the way, you're gonna need it!")
        third = input("You take a boat across but your crush is no longer there. In the distance you see three portals. Your crush jumped into the left! Your treasure map says that only true love can guide you to the treasure. What portal do you choose?\nType Left Right or Middle:  ").lower()
        if third == "right":
            print("Congratulations! You found the treasure. You forget about your crush cause you're rich now!")
        elif third == "left":
            print("Why would you follow her you idiot!? You end up with her in your ex's bed. She shoots both of you. You died. Game Over.")
        else:
            print("You jump through the middle portal and get sent to outerspace. you die instantly Game Over.")
    else:
        print("You horny little bastard. The current was too strong. You drowned. Game Over.")

else:
    print("You went down the dirt road and died of thirst, should have just went back to the river dummy. Game Over.")
