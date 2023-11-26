import pygame
from organismo import Organismo

class Animal(Organismo):
    def __init__(self, x, y, margin):
        super().__init__("cazador.png", x, y, margin)
        self.detectado = False

    def escanear(self, presa, screen):
        cuadros_escaneados = pygame.sprite.Group()

        for dx in range(-2 * CELL_SIZE, 3 * CELL_SIZE, CELL_SIZE):
            for dy in range(-2 * CELL_SIZE, 3 * CELL_SIZE, CELL_SIZE):
                cuadro = pygame.Rect(self.rect.x + dx, self.rect.y + dy, CELL_SIZE, CELL_SIZE)
                cuadros_escaneados.add(cuadro)

                if presa.rect.colliderect(cuadro):
                    self.detectado = True
                    pygame.draw.rect(screen, (255, 0, 0), cuadro, 2)  # Dibujar cuadro rojo si la presa está en el cuadro
                else:
                    pygame.draw.rect(screen, (0, 255, 0), cuadro, 2)  # Dibujar cuadro verde en el escaneo

    def mover_hacia(self, objetivo):
        dx = objetivo.rect.x - self.rect.x
        dy = objetivo.rect.y - self.rect.y
        distancia = pygame.math.Vector2(dx, dy).length()

        if distancia > 0:
            velocidad = 1
            direccion = pygame.math.Vector2(dx, dy).normalize()
            movimiento = direccion * velocidad * CELL_SIZE
            self.rect.x += int(movimiento.x)
            self.rect.y += int(movimiento.y)
