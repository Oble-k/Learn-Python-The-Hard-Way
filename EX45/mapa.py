# Define las escenas que van a ir sucediendo

class Mapa(object):

    scenes = {
        'start' : Start(),
        'baraja' : Baraja(),
        'repartir_inicial' : RepartirInicial(),
        'game_loop' : GameLoop(),
        'recuento_puntos' : RecuentoPuntos(),
        'ganador' : Ganador()
    }