# Basic Object-Oriented Analysis and Design
from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)
        pass


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):
    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
        ]
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            Some description of the Corridor
            There is a Gothon blablabla.
            You must defeat it to get to Armory.
            His blaster aiming at your face.
            How will you fare against him?
            """))
        action = input("> ")
        if action == "1":
            return "death"
        if action == "2":
            return "death"
        if action == "3":
            return "laser_weapon_armory"
        else:
            print("Does not Compute!")
            return "central_corridor"


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            After miraculously surviving the encounter with the Gothon, you enter the armory.
            So far no Gothons in sight, but there is an eerie feeling that something evil is lurking.
            Looking around the room you find the container that holds the neutron bomb.
            But you require a three-digit code to open it.
            A three digit code you just forgot!
            You are going to guess it...
            And you only got 10 attempts.
            I would not want to be you right now."""))
        code = f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}"
        guess = input("[keypad]> ")
        guesses = 1

        print("Code: ", code)
        while guess != code and guesses < 10:
            print("BZZZZZZ!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                The container clicks and you open it. You take the neutron bomb, which is
                lighter than expected. Now you rush into the bridge where you should place it
                to destroy the ship.
                """))
            return "the_bridge"
        else:
            print(dedent(""" 
                The lock buzzes for the last time and then you realize you wont be able to open it.
                You blew it. And i don't mean the bomb. You can't blow the bomb for it is in the box.
                The box right in front of you that you failed to open? Yes, that box.
                I meant the situation, the emergency. You failed man.
                You wait for your unavoidable demise. The Gothon mothership is reading its laser cannons.
                You will not live to see another day.
                """))
            return "death"

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
        You burst onto the Bridge with the neutron destruct bomb
        under your arm and surprise 5 Gothons who are trying to
        take control of the ship. Each of them has an even uglier
        clown costume than the last. They haven't pulled their
        weapons out yet, as they see the active bomb under your
        arm and don't want to set it off.
        """))

        action = input("> ")
        if action == "throw bomb":
            return "death"
        elif action == "slowly place the bomb":
            return "escape_pod"
        else:
            print("Does not Compute!")
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            You rush through the ship desperately trying to make it to
            the escape pod before the whole ship explodes. It seems
            like hardly any Gothons are on the ship, so your run is
            clear of interference. You get to the chamber with the
            escape pods, and now need to pick one to take. Some of
            them could be damaged but you don't have time to look.
            There's 5 pods, which one do you take?
            """))
        good_pod = randint(1, 5)

        guess = input("[pod #]> ")

        if int(guess) == good_pod:
            print(dedent(f"""
            You jump into pod {guess} and hit the eject button.
            The pod escapes out into the void of space, then
            implodes as the hull ruptures, crushing your body into
            jam jelly.
            """))
            return 'death'
        else:
            print(dedent(f"""
            You jump into pod {guess} and hit the eject button.
            The pod easily slides out into space heading to the
            planet below. As it flies to the planet, you look
            back and see your ship implode then explode like a
            bright star, taking out the Gothon ship at the same
            time. You won!
            """))

            return 'finished'

class Finished(Scene):
    def enter(self):
        print("You won! Good job.")
        return "finished"

class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()