import pygame
import random

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

        pass

class Animal(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta, imagen_path):
        super().__init__(posicion, vida, energia)
        self.velocidad = velocidad
        self.especie = especie
        self.dieta = dieta
        self.imagen = pygame.image.load(imagen_path)

    def cazar(self, presa):

        pass

    def mover(self, filas, columnas):
        # Seleccionar una dirección aleatoria (horizontal o vertical)
        direccion = random.choice(['horizontal', 'vertical'])

        # Tamaño del paso
        paso = 1

        if direccion == 'horizontal':
            # Mover en la dirección horizontal
            nueva_posicion = (
                self.posicion[0] + random.choice([-1, 1]) * paso,
                self.posicion[1]
            )
        else:
            # Mover en la dirección vertical
            nueva_posicion = (
                self.posicion[0],
                self.posicion[1] + random.choice([-1, 1]) * paso
            )

        # Verificar límites
        nueva_posicion = (
            max(0, min(nueva_posicion[0], filas - 1)),
            max(0, min(nueva_posicion[1], columnas - 1))
        )

        self.posicion = nueva_posicion



class Presa(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, especie, plantas_alimento, imagen_path):
        super().__init__(posicion, vida, energia)
        self.velocidad = velocidad
        self.especie= especie
        self.plantas_alimento = plantas_alimento
        self.imagen = pygame.image.load(imagen_path)

    def alimentarse(self, planta):
        if planta in self.plantas_alimento:
            self.energia += planta.energia
            planta.morir() 
            print(f"{self._class.name_} se ha alimentado y ganó energía.")
        else:
            print(f"{self._class.name_} no puede alimentarse de esta planta.")

    def mover(self, filas, columnas):
        # Seleccionar una dirección aleatoria (horizontal o vertical)
        direccion = random.choice(['horizontal', 'vertical'])

        # Tamaño del paso
        paso = 1

        if direccion == 'horizontal':
            # Mover en la dirección horizontal
            nueva_posicion = (
                self.posicion[0] + random.choice([-1, 1]) * paso,
                self.posicion[1]
            )
        else:
            # Mover en la dirección vertical
            nueva_posicion = (
                self.posicion[0],
                self.posicion[1] + random.choice([-1, 1]) * paso
            )

        # Verificar límites
        nueva_posicion = (
            max(0, min(nueva_posicion[0], filas - 1)),
            max(0, min(nueva_posicion[1], columnas - 1))
        )

        self.posicion = nueva_posicion


class Planta(Organismo):
    def __init__(self, posicion, vida, energia, especie, imagen_path):
        super().__init__(posicion, vida, energia)
        self.especie= especie
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
animal6 = Animal((10, 10), 100, 50, 5, "León", "Carnívoro", "leon.png")
animal7 = Animal((10, 10), 100, 50, 5, "Coyote", "Carnívoro", "coyote.png")
animal8 = Animal((10, 10), 100, 50, 5, "Serpiente", "Carnívoro", "serpiente.png")
animal9 = Animal((10, 10), 100, 50, 5, "Escorpion", "Carnívoro", "escorpion.png")
animal10 = Animal((10, 10), 100, 50, 5, "Caracal", "Carnívoro", "caracal.png")



presa1 = Presa((40, 40), 80, 50, 4, "Raton", [planta1, planta2], "raton.png")
presa2 = Presa((40, 40), 80, 50, 4, "Lagartija", [planta1, planta2], "lagartija.png")
presa3 = Presa((40, 40), 80, 50, 4, "Pajaro", [planta1, planta2], "pajaro.png")
presa4 = Presa((40, 40), 80, 50, 4, "Gacela",[planta1, planta2], "gacela.png")
presa5 = Presa((40, 40), 80, 50, 4, "Tortuga",[planta1, planta2], "tortuga.png")
presa6 = Presa((40, 40), 80, 50, 4, "Raton", [planta1, planta2], "raton.png")
presa7 = Presa((40, 40), 80, 50, 4, "Lagartija", [planta1, planta2], "lagartija.png")
presa8 = Presa((40, 40), 80, 50, 4, "Pajaro", [planta1, planta2], "pajaro.png")
presa9 = Presa((40, 40), 80, 50, 4, "Gacela",[planta1, planta2], "gacela.png")
presa10 = Presa((40, 40), 80, 50, 4, "Tortuga",[planta1, planta2], "tortuga.png")





print(animal1.vida)
animal1.cazar(planta1)