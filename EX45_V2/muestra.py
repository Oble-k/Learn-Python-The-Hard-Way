# La primera carta se convierte en la muestra
class Muestra(object):
    def __init__(self, deck_whole):
        self.deck = deck_whole
        # print("Muestra, __init__")

    def extraer_muestra(self):
        print("Extraemos la muestra...")
        print(self.deck)
        return self.deck.pop(0)
