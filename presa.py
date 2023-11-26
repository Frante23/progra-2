import pygame
from organismo import Organismo
import random

class Presa(Organismo):
    def __init__(self, x, y, margin):
        super().__init__("presa.png", x, y, margin)

    def mover_a_nueva_posicion(self):
        self.rect.x = random.randrange(WIDTH // CELL_SIZE) * CELL_SIZE
        self.rect.y = random.randrange(HEIGHT // CELL_SIZE) * CELL_SIZE

    def arrancar(self):
        direccion = random.choice([(CELL_SIZE, 0), (-CELL_SIZE, 0), (0, CELL_SIZE), (0, -CELL_SIZE)])
        self.rect.x += direccion[0]
        self.rect.y += direccion[1]
