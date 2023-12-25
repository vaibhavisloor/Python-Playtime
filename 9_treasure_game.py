print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************''')
print("Welcome to Treasure Hunt Game")
print("You have 2 paths infront of you. Which will you take ? left or right")
decision1 = input()
if (decision1 == "right"):
    print("Now you have reached the banks of a river. Will you wait for the boat or go swimming ? wait or swim\n[CAUTION: Crocodiles can be present in the river]" )
    decision2 = input()
    if(decision2 == 'wait'):
        print("Very Good ! You have reached the final level !!\nNow you see 3 doors ahead of you and one of them contains the treasure. Choose one\nred or blue or yellow")
        decision3 = input()
        if(decision3 == "blue"):
            print("Congratulations ! You have won the treasure !")
        elif (decision3 == "red"):    
            print("Bad Luck. YOu entered an empty room")
        else:
            print("You were eaten by a demon")    
    else:
        print("You were eaten by a Crocodile") 
        exit()

else:
    print("You fell in a pot hole. Game Over") 
    exit()   