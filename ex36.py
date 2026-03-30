# Designing and debugging
from sys import exit

def dead(cause):
    print(cause, "\nWill you try again?")
    exit(0)

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
        exit(0)
    elif choice == "2":
        exit(0)
    elif choice == "3":
        exit(0)
    elif choice == "4":
        exit(0)
    else:
        dead("Your incapability to decide makes your anxiety to rise, leading to a heart attack.")



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