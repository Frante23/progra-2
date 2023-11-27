import pygame
import random

class Organismo:
    def __init__(self, posicion, vida, energia):
        self.posicion = posicion
        self.vida = vida
        self.energia = energia

    def mover(self):
        # Implementación de movimiento genérico
        pass

    def reproducir(self, pareja):
        # Implementación genérica de reproducción
        pass

    def morir(self):
        # Implementación genérica de muerte
        pass

class Animal(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta, imagen_path):
        super().__init__(posicion, vida, energia)
        self.velocidad = velocidad
        self.especie = especie
        self.dieta = dieta
        self.imagen = pygame.image.load(imagen_path)

    def cazar(self, presa):
        # Implementación de la acción de cazar
        pass
    
    def mover(self, limites_columnas, limites_filas):
        # Mover el animal en una dirección aleatoria dentro de los límites
        nueva_posicion = (
            self.posicion[0] + random.choice([-1, 0, 1]) * self.velocidad,
            self.posicion[1] + random.choice([-1, 0, 1]) * self.velocidad
        )

        # Aplicar límites de movimiento
        nueva_posicion = (
            max(0, min(nueva_posicion[0], limites_columnas - 1)),
            max(0, min(nueva_posicion[1], limites_filas - 1))
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
            planta.morir()  # Puedes implementar la lógica específica de morir para plantas
            print(f"{self.__class__.__name__} se ha alimentado y ganó energía.")
        else:
            print(f"{self.__class__.__name__} no puede alimentarse de esta planta.")
            
    def mover(self, limites_columnas, limites_filas):
        # Mover el animal en una dirección aleatoria dentro de los límites
        nueva_posicion = (
            self.posicion[0] + random.choice([-1, 0, 1]) * self.velocidad,
            self.posicion[1] + random.choice([-1, 0, 1]) * self.velocidad
        )

        # Aplicar límites de movimiento
        nueva_posicion = (
            max(0, min(nueva_posicion[0], limites_columnas - 1)),
            max(0, min(nueva_posicion[1], limites_filas - 1))
        )

        self.posicion = nueva_posicion
        
        
        
        
class Planta(Organismo):
    def __init__(self, posicion, vida, energia, especie, imagen_path):
        super().__init__(posicion, vida, energia)
        self.especie= especie
        self.imagen = pygame.image.load(imagen_path)

    def fotosintesis(self):
        # Implementación de la fotosíntesis
        pass

    def reproducir_por_semillas(self):
        # Implementación de reproducción por semillas
        pass

#Posicion, vida, energia, velocidad
planta1 = Planta((20, 20), 50, 30, "Cactus", "cactus.png")
planta2 = Planta((30, 30), 60, 40, "Artemisa","artemisa.png")
planta3 = Planta((20, 20), 50, 30, "Salsola","salsola.png")
planta4 = Planta((30, 30), 60, 40, "Yuca","yuca.png")
planta5 = Planta((20, 20), 50, 30, "Atriplex","atriplex.png")


#Posicion, vida, energia, velocidad, especie, dieta, imagen
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
