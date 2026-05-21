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

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Mapa.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
