class Organismo:
    def __init__(self, posicion, vida, energia, velocidad):
        self.posicion = posicion
        self.vida = vida
        self.energia = energia
        self.velocidad = velocidad

    def mover(self):
        # Lógica de movimiento del organismo
        pass

    def reproducir(self, pareja):
        # Lógica de reproducción
        pass

    def morir(self):
        # Lógica de muerte
        pass

class Animal(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad)
        self.especie = especie
        self.dieta = dieta

    def cazar(self, presa):
        # Lógica de caza
        pass

class Planta(Organismo):
    def __init__(self, posicion, vida, energia, velocidad):
        super().__init__(posicion, vida, energia, velocidad)

    def fotosintesis(self):
        # Lógica de fotosíntesis
        pass

    def reproducir_por_semillas(self):
        # Lógica de reproducción por semillas
        pass
