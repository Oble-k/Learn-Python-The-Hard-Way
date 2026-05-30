# Se crea la baraja y se randomiza el orden
import random
class Baraja(object):
    def __init__(self):
        print("The deck is being shuffled...")

        palos = ["oros", "espadas", "copas", "bastos"]
        self.cartas = []  # Inicializamos la lista de cartas
        # i para num; j para palos,
        for palo in palos:
            i = 1
            for num in range (1, 13):
                numero_y_palo = f"{num} {palo}"
                self.cartas.append(numero_y_palo)
                i += 1
        random.shuffle(self.cartas)
        print("The deck has been shuffled successfully!")


