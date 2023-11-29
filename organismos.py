import pygame
import random
import time
import sys

class Organismo:
    def __init__(self, posicion, vida, energia):
        self.posicion = posicion
        self.vida = vida
        self.energia = energia

    def mover(self):
        pass

    def reproducir(self, pareja):
        pass

    def morir(self):
        self.posicion = (-1, -1)
        time.sleep(5)
        self.posicion = (random.randint(0, columnas - 1), random.randint(0, filas - 1))

class Animal(Organismo):
    filas = 20
    columnas = 30

    def __init__(self, posicion, vida, energia, velocidad, especie, dieta, imagen_path):
        super().__init__(posicion, vida, energia)
        self.velocidad = velocidad
        self.especie = especie
        self.dieta = dieta
        self.imagen = pygame.image.load(imagen_path)

    def cazar(self, presas):
        nueva_posicion = (
            self.posicion[0] + random.choice([-1, 0, 1]),
            self.posicion[1] + random.choice([-1, 0, 1])
        )

        if 0 <= nueva_posicion[0] < self.filas and 0 <= nueva_posicion[1] < self.columnas:
            self.posicion = nueva_posicion

        for presa in presas:
            nueva_posicion_presa = (
                presa.posicion[0] + random.choice([-1, 0, 1]),
                presa.posicion[1] + random.choice([-1, 0, 1])
            )

            if 0 <= nueva_posicion_presa[0] < self.filas and 0 <= nueva_posicion_presa[1] < self.columnas:
                presa.posicion = nueva_posicion_presa
        def mover(self):
            nueva_posicion = (
                self.posicion[0] + random.choice([-1, 0, 1]),
                self.posicion[1] + random.choice([-1, 0, 1])
            )

            if 0 <= nueva_posicion[0] < self.filas and 0 <= nueva_posicion[1] < self.columnas:
                self.posicion = nueva_posicion


class Presa(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, especie, plantas_alimento, imagen_path):
        super().__init__(posicion, vida, energia)
        self.velocidad = velocidad
        self.especie = especie
        self.plantas_alimento = plantas_alimento
        self.imagen = pygame.image.load(imagen_path)

    def alimentarse(self, planta):
        if planta.posicion == self.posicion:
            self.energia += planta.energia
            planta.morir()
            print(f"{self.__class__.__name__} se ha alimentado y ganó energía.")
        else:
            print(f"{self.__class__.__name__} no puede alimentarse de esta planta.")

    def mover(self, filas, columnas):
        nueva_posicion = (
            self.posicion[0] + random.choice([-1, 0, 1]),
            self.posicion[1] + random.choice([-1, 0, 1])
        )

        if 0 <= nueva_posicion[0] < filas and 0 <= nueva_posicion[1] < columnas:
            self.posicion = nueva_posicion

class Planta(Organismo):

    
    def __init__(self, posicion, vida, energia, especie, imagen_path):
        super().__init__(posicion, vida, energia)
        self.especie = especie
        self.imagen = pygame.image.load(imagen_path)

    def fotosintesis(self):
        pass

    def reproducir_por_semillas(self):
        pass

planta1 = Planta((20, 20), 50, 30, "Cactus", "cactus.png")
planta2 = Planta((30, 30), 60, 40, "Artemisa","artemisa.png")
planta3 = Planta((20, 20), 50, 30, "Salsola","salsola.png")
planta4 = Planta((30, 30), 60, 40, "Yuca","yuca.png")
planta5 = Planta((20, 20), 50, 30, "Atriplex","atriplex.png")


animal1 = Animal((10, 10), 100, 50, 5, "León", "Carnívoro", "leon.png")
animal2 = Animal((10, 10), 100, 50, 5, "Coyote", "Carnívoro", "coyote.png")
animal3 = Animal((10, 10), 100, 50, 5, "Serpiente", "Carnívoro", "serpiente.png")
animal4 = Animal((10, 10), 100, 50, 5, "Escorpion", "Carnívoro", "escorpion.png")
animal5 = Animal((10, 10), 100, 50, 5, "Caracal", "Carnívoro", "caracal.png")
presa1 = Presa((40, 40), 80, 50, 4, "Raton", [planta1, planta2], "raton.png")
presa2 = Presa((40, 40), 80, 50, 4, "Lagartija", [planta1, planta2], "lagartija.png")
presa3 = Presa((40, 40), 80, 50, 4, "Pajaro", [planta1, planta2], "pajaro.png")
presa4 = Presa((40, 40), 80, 50, 4, "Gacela",[planta1, planta2], "gacela.png")
presa5 = Presa((40, 40), 80, 50, 4, "Tortuga",[planta1, planta2], "tortuga.png")




print(animal1.vida)
animal1.cazar(planta1)
