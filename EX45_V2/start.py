# Pregunta al usuario si quiere jugar a la brisca.a

class Start(object):
    print("Do you want to play a game of brisca?")
    var = "Yes"
    # var = input("> ")
    if var == "Yes":
        print("Let's get it started!")
    elif var == "No":
        print("Okay, bye!")
        exit()