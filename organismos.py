import pygame
import random

ancho_imagen = 30
alto_imagen = 30
filas = 20
columnas = 30
class Organismo:
    def __init__(self, posicion, vida, energia, filas=None, columnas=None):
        self.posicion = posicion
        self.vida = vida
        self.energia = energia
        self.filas = int(filas) if filas is not None else None
        self.columnas = int(columnas) if columnas is not None else None

    def mover(self, filas, columnas):  
        direccion = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        nueva_posicion = (self.posicion[0] + direccion[0], self.posicion[1] + direccion[1])

        if (
            self.columnas is not None and
            self.filas is not None and
            0 <= nueva_posicion[0] < self.columnas and
            0 <= nueva_posicion[1] < self.filas
        ):
            self.posicion = nueva_posicion



    def reproducir(self, pareja):
        pass

    def morir(self):
        pass

class Animal(Organismo):
    imagen_path = None  # Esto debe ser definido por las subclases

    def __init__(self, posicion, vida, energia, velocidad, dieta, id_animal, imagen_path, filas=None, columnas=None):
        super().__init__(posicion, vida, energia, filas=filas, columnas=columnas)
        self.velocidad = velocidad
        self.dieta = dieta
        self.id_animal = id_animal

        # Escala la imagen al tamaño deseado
        original_image = pygame.image.load(imagen_path)
        self.imagen = pygame.transform.scale(original_image, (ancho_imagen, alto_imagen))  # Reemplaza nuevo_ancho y nuevo_alto con tus valores deseados

        if Animal.imagen_path is not None:
            self.imagen_path = Animal.imagen_path

        self.imagen = pygame.transform.scale(pygame.image.load(self.imagen_path), (ancho_imagen, alto_imagen))

    def reproducir(self, pareja, imagen_path):
        pass
class Leon(Animal):
    imagen_path = "leon.png"

    def __init__(self, posicion, vida, energia, velocidad, dieta, id_leon, imagen_path, filas=20, columnas=30):
        super().__init__(posicion, vida, energia, velocidad, dieta, id_leon, imagen_path, filas=filas, columnas=columnas)

    def reproducir(self, pareja):
        if isinstance(pareja, Leon):
            nuevo_leon = Leon(posicion=(0, 0), vida=100, energia=50, velocidad=8, dieta='carnivoro', id_leon=21, imagen_path="leon.png", filas=self.filas, columnas=self.columnas)
            nuevo_leon.imagen = pygame.transform.scale(pygame.image.load("leon.png"), (ancho_imagen, alto_imagen))
            return nuevo_leon
        else:
            return None

        
class Coyote(Animal):
    imagen_path = "coyote.png"

    def __init__(self, posicion, vida, energia, velocidad, dieta, id_coyote, imagen_path=None, filas=None, columnas=None):
        super().__init__(posicion, vida, energia, velocidad, dieta, id_coyote, imagen_path, filas=filas, columnas=columnas)
        self.id_coyote = id_coyote

    def cazar(self, presa):
        pass

    def reproducir(self, pareja):
        if isinstance(pareja, Coyote):
            nuevo_coyote = Coyote(posicion=(0, 0), vida=100, energia=50, velocidad=10, dieta='carnivoro', id_coyote=21, imagen_path="coyote.png", filas=self.filas, columnas=self.columnas)
            nuevo_coyote.imagen = pygame.transform.scale(pygame.image.load("coyote.png"), (ancho_imagen, alto_imagen))
            return nuevo_coyote
        else:
            return None


class Serpiente(Animal):
    imagen_path = "serpiente.png"

    def __init__(self, posicion, vida, energia, velocidad, dieta, id_serpiente, imagen_path=None, filas=None, columnas=None):
        super().__init__(posicion, vida, energia, velocidad, dieta, id_serpiente, imagen_path, filas=filas, columnas=columnas)
        self.id_serpiente = id_serpiente

    def cazar(self, presa):
        pass

    def reproducir(self, pareja):
        if isinstance(pareja, Serpiente):
            nuevo_serpiente = Serpiente(posicion=(0, 0), vida=80, energia=40, velocidad=5, dieta='carnivoro', id_serpiente=21, imagen_path="serpiente.png", filas=self.filas, columnas=self.columnas)
            nuevo_serpiente.imagen = pygame.transform.scale(pygame.image.load("serpiente.png"), (ancho_imagen, alto_imagen))
            return nuevo_serpiente
        else:
            return None



    
class Escorpion(Animal):
    imagen_path = "escorpion.png"

    def __init__(self, posicion, vida, energia, velocidad, dieta, id_escorpion, imagen_path=None, filas=None, columnas=None):
        super().__init__(posicion, vida, energia, velocidad, dieta, id_escorpion, imagen_path, filas=filas, columnas=columnas)
        self.id_escorpion = id_escorpion

    def cazar(self, presa):
        pass

    def reproducir(self, pareja):
        if isinstance(pareja, Escorpion):
            nuevo_escorpion = Escorpion(posicion=(0, 0), vida=70, energia=35, velocidad=8, dieta='carnivoro', id_escorpion=11, imagen_path="escorpion.png", filas=self.filas, columnas=self.columnas)
            nuevo_escorpion.imagen = pygame.transform.scale(pygame.image.load("escorpion.png"), (ancho_imagen, alto_imagen))
            return nuevo_escorpion
        else:
            return None



    
class Caracal(Animal):
    imagen_path = "caracal.png"

    def __init__(self, posicion, vida, energia, velocidad, dieta, id_caracal, imagen_path=None, filas=None, columnas=None):
        super().__init__(posicion, vida, energia, velocidad, dieta, id_caracal, imagen_path, filas=filas, columnas=columnas)
        self.id_caracal = id_caracal

    def cazar(self, presa):
        pass

    def reproducir(self, pareja):
        if isinstance(pareja, Caracal):
            nuevo_caracal = Caracal(posicion=(0, 0), vida=90, energia=45, velocidad=12, dieta='carnivoro', id_caracal=21, imagen_path="caracal.png", filas=self.filas, columnas=self.columnas)
            nuevo_caracal.imagen = pygame.transform.scale(pygame.image.load("caracal.png"), (ancho_imagen, alto_imagen))
            return nuevo_caracal
        else:
            return None


class Presa(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, plantas_alimento, imagen_path):
        super().__init__(posicion, vida, energia)
        self.velocidad = velocidad
        self.plantas_alimento = plantas_alimento
        self.imagen = pygame.image.load(imagen_path)

    def mover(self, filas, columnas):
        direccion = random.choice(['horizontal', 'vertical'])
        paso = 1

        if direccion == 'horizontal':
            nueva_posicion = (self.posicion[0] + random.choice([-1, 1]) * paso, self.posicion[1])
        else:
            nueva_posicion = (self.posicion[0], self.posicion[1] + random.choice([-1, 1]) * paso)

        nueva_posicion = (
            max(0, min(nueva_posicion[0], filas - 1)),
            max(0, min(nueva_posicion[1], columnas - 1))
        )

        self.posicion = nueva_posicion
    
    def reproducir(self, pareja):
        # Implementa la lógica de reproducción aquí
        pass
    
class Raton(Presa):
    def __init__(self, posicion, vida, energia, velocidad, plantas_alimento, imagen_path, id_raton):
        super().__init__(posicion, vida, energia, velocidad, plantas_alimento, imagen_path)
        self.id_raton = id_raton

    def reproducir(self, pareja):
        if isinstance(pareja, Raton):
            # Lógica de reproducción de ratones
            nuevo_raton = Raton(posicion=(0, 0), vida=30, energia=20, velocidad=5, plantas_alimento=(planta1, planta2, planta3, planta4, planta5), imagen_path="raton.png", id_raton=22)
            nuevo_raton.imagen = pygame.transform.scale(pygame.image.load("raton.png"), (ancho_imagen, alto_imagen))  # Ajusta las dimensiones
            return nuevo_raton
        else:
            return None

class Lagartija(Presa):
    def __init__(self, posicion, vida, energia, velocidad, plantas_alimento, imagen_path, id_lagartija):
        super().__init__(posicion, vida, energia, velocidad, plantas_alimento, imagen_path)
        self.id_lagartija = id_lagartija

class Pajaro(Presa):
    def __init__(self, posicion, vida, energia, velocidad, plantas_alimento, imagen_path, id_pajaro):
        super().__init__(posicion, vida, energia, velocidad, plantas_alimento, imagen_path)
        self.id_pajaro = id_pajaro

class Gacela(Presa):
    def __init__(self, posicion, vida, energia, velocidad, plantas_alimento, imagen_path, id_gacela):
        super().__init__(posicion, vida, energia, velocidad, plantas_alimento, imagen_path)
        self.id_gacela = id_gacela

class Tortuga(Presa):
    def __init__(self, posicion, vida, energia, velocidad, plantas_alimento, imagen_path, id_tortuga):
        super().__init__(posicion, vida, energia, velocidad, plantas_alimento, imagen_path)
        self.id_tortuga = id_tortuga


class Planta(Organismo):
    def __init__(self, posicion, vida, energia, filas, nombre, imagen_path):
        super().__init__(posicion, vida, energia, filas)
        self.nombre = nombre
        self.imagen_path = imagen_path
        try:
            self.imagen = pygame.image.load(imagen_path)
        except pygame.error as e:
            print(f"Error cargando la imagen {imagen_path}: {e}")


    def fotosintesis(self):
        # Lógica de la fotosíntesis
        pass

    def reproducir_por_semillas(self):
        # Lógica de la reproducción por semillas
        pass


planta1 = Planta((20, 20), 50, 30, 20, "Cactus", "cactus.png")
planta2 = Planta((15, 25), 40, 25, 20, "Artemisa", "artemisa.png")
planta3 = Planta((20, 20), 50, 30, 20, "Salsola","salsola.png")
planta4 = Planta((30, 30), 40, 25, 20, "Yuca","yuca.png")
planta5 = Planta((20, 20), 40, 25, 20, "Atriplex","atriplex.png")

leon1 = Leon((20, 20), 100, 50, 8, 'carnivoro', 1, "leon.png", filas=30, columnas=columnas)
leon2 = Leon((15, 15), 100, 50, 8, 'carnivoro', 2, "leon.png", columnas=columnas)
coyote1 = Coyote((8, 8), 100, 50, 10, 'carnivoro', 3, "coyote.png", filas=filas, columnas=columnas)
coyote2 = Coyote((12, 12), 100, 50, 10, 'carnivoro', 4, "coyote.png", filas=filas, columnas=columnas)
serpiente1 = Serpiente((5, 5), 80, 40, 5, 'carnivoro', 5, "serpiente.png", filas=filas, columnas=columnas)
serpiente2 = Serpiente((10, 10), 80, 40, 5, 'carnivoro', 6, "serpiente.png", filas=filas, columnas=columnas)
caracal1 = Caracal((7, 7), 90, 45, 12, 'carnivoro', 7, "caracal.png")
caracal2 = Caracal((15, 15), 90, 45, 12, 'carnivoro', 8, "caracal.png")
escorpion1 = Escorpion((3, 3), 70, 35, 8, 'carnivoro', 9, "escorpion.png")
escorpion2 = Escorpion((18, 18), 70, 35, 8, 'carnivoro', 10, "escorpion.png")

raton1 = Raton((2, 2), 30, 20, 5, (planta1, planta2, planta3, planta4, planta5), "raton.png", 11)
raton2 = Raton((18, 18), 30, 20, 5, (planta1, planta2, planta3, planta4, planta5), "raton.png", 12)
lagartija1 = Lagartija((4, 4), 40, 25, 8, (planta1, planta2, planta3, planta4, planta5), "lagartija.png", 13)
lagartija2 = Lagartija((16, 16), 40, 25, 8, (planta1, planta2, planta3, planta4, planta5), "lagartija.png", 14)
pajaro1 = Pajaro((6, 6), 50, 30, 10, (planta1, planta2, planta3, planta4, planta5), "pajaro.png", 15)
pajaro2 = Pajaro((14, 14), 50, 30, 10, (planta1, planta2, planta3, planta4, planta5), "pajaro.png", 16)
gacela1 = Gacela((8, 8), 60, 35, 15, (planta1, planta2, planta3, planta4, planta5), "gacela.png", 17)
gacela2 = Gacela((12, 12), 60, 35, 15, (planta1, planta2, planta3, planta4, planta5), "gacela.png", 18)
tortuga1 = Tortuga((10, 10), 70, 40, 5, (planta1, planta2, planta3, planta4, planta5), "tortuga.png", 19)
tortuga2 = Tortuga((20, 20), 70, 40, 5, (planta1, planta2, planta3, planta4, planta5), "tortuga.png", 20)