# Borrar scenes
from start import *
from baraja import Baraja
from muestra import Muestra

from repartir_inicial import RepartirInicial
scenes = {
    'start': Start(),
    'baraja': Baraja(),
    # 'repartir_inicial': RepartirInicial(),
    # 'game_loop': GameLoop(),
    # 'recuento_puntos': RecuentoPuntos(),
    # 'ganador': Ganador()
}

Start() #Se pregunta al usuario si quiere jugar a brisca.

mazo_robo = Baraja() #Se crea el mazo del que se robará, y se ordena de manera aleatoria

# print(deck_list) #Ya es usable el vector de la baraja

instancia = Muestra(mazo_robo.deck) #Se crea una instancia llamada instancia de la clase

la_muestra = instancia.extraer_muestra()

print(la_muestra)
