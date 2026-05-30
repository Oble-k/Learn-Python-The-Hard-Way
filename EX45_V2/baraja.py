# Genera la baraja, y hace el shuffle original.
import random
class Baraja(object):
    def __init__(self):
        print("I'm shuffling the deck...")
        self.deck = [] #Recuerda, el self. hace que la variable deje de ser local al init, y así poder ser devuelta al main.
        palos = ["oros", "espadas", "copas", "bastos"]

        for palo in palos:
            for num in range (1, 13):
                card = str(num) + " de " + palo
                self.deck.append(card)
        random.shuffle(self.deck)


    def __str__(self):
        return str(self.deck)