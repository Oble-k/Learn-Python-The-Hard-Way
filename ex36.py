# Designing and debugging
from sys import exit

def dead(cause):
    print(cause, "\nWill you try again?")
    exit(0)

def tower():
    print("You walk northwards. As you approach the tower, a gate begins to take form.")
    print("You wait around the portculis for a a while. As you begin to wonder if you should leave, you hear a metalic clank")
    print("The gate begins to rise.")
    print("A corridor appears before you, an ominous noise can be heard.")
    print("\t1.-Enter the tower.")
    print("\t2.-Go back.")

    choice = input("> ")
    if choice == "1":
        print("You enter the corridor until...")
        exit(0)
    elif choice == "2":
        dead("You turn back, and you start making your way to the town. However, the path seems changed.\nAn impossibly long path which grows by the second.\nYou won't make it back.\nStarvation hits you, and you fall to the ground.")
    else
        dead("Your mind becomes a mush, and thus your body is unable to answer to whats slithering from the gate.")

def village():
    print("You go out the door.\nThe sun shines ever brightest.\nFar over the northern plains, an eerie looking tower looms over the realm")
    print("In the street there is a forge, an alchemist shop, and the wizards quarters")
    print("What should you do?")
    print("\t1.-Go north, towards the tower.")
    print("\t2.-Enter the blacksmith's forge")
    print("\t3.-Enter the alchemist's shop")
    print("\t4.-Visit the wizard")

    choice =input("> ")

    if choice == "1":
        tower()
    elif choice == "2":
        exit(0)
    elif choice == "3":
        exit(0)
    elif choice == "4":
        exit(0)
    else:
        dead("Your incapability to decide makes your anxiety to rise, leading to a heart attack.")

pain = 60

def start():
    print("The sun rises upon the village.\nYou can hear the crowings of roosters.\nIt's time to go on an adventure!\n\nYou should go out!")
    print("\t1.-Go out the door, to have an adventure")
    print("\t2.-Stay at bed.")
    oversleep = 0
    while True:
        choice = input("> ")

        if choice == "1":
            village() #Important to define the village function
        elif choice == "2" and oversleep == 0:
            oversleep += 1
            print("You should get going!")
        elif choice == "2" and oversleep == 1:
            oversleep += 1
            print("You should REALLY get going!")
        elif choice == "2" and oversleep == 2:
            dead("You where warned. You fall on an eternal slumber from which you are never awoken.\nYou die of old age, surrounded by your loved ones, who will only remember how lazy you were.")
        else:
            print("Sorry, but {} isn't an option, try again".format(choice))

start()