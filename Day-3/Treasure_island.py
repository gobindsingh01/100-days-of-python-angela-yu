#Day 3
skull='''
     _.--""--._
    /  _    _  \\
 _  ( (_\  /_) )  _
{ \._\   /\   /_./ }
/_"=-.}______{.-="_\\
 _  _.=("""")=._  _
(_'"_.-"`~~`"-._"'_)
 {_"            "_}
 '''
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to the Treasure Island.")
print("Your mission is to find the Treasure.")
choice=input("You're at a cross road. Where do you want to go?\n\tType \"left\" or \"right\"\n>>>")
if choice.lower()=="left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice=input("\tType \"wait\" to wait for a boat. Type \"swim\" to swim across.\n>>>")
    if choice.lower()=="wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        choice=input("\tOne red, One yellow and one blue. Which colour do you choose?\n>>>")
        if choice.lower()=="yellow":
            print("You went into the yellow door. You found the treasure. Game Over. You Win.")
            print('''
                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`''')
        elif choice.lower()=="red":
            print("You went into the red door. you got burned by fire. Game Over.")
            print(skull)
        elif choice.lower()=="blue":
            print("You went into the blue door. You got eaten by beasts. Game Over.")
            print(skull)
        else:
            print("Game Over.")
            print(skull)
    else:
        print("You decided to swim and got attacked by the crocodiles in the water. Game Over.")
        print(skull)
else:
    print("You fell into a hole. Game Over.")
    print(skull)