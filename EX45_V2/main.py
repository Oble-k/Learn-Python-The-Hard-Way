# Borrar scenes
from start import *
from baraja import Baraja
scenes = {
    'start': Start(),
    'baraja': Baraja(),
    # 'repartir_inicial': RepartirInicial(),
    # 'game_loop': GameLoop(),
    # 'recuento_puntos': RecuentoPuntos(),
    # 'ganador': Ganador()
}
Start()
deck_list = Baraja()
print(deck_list) #Ya es usable el vector de la baraja