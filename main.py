import pygame
import sys
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 40

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("la nieee")

fondo = pygame.image.load("fondo.png")
fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))

class Organismo(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Animal(Organismo):
    def __init__(self, x, y):
        super().__init__("cazador.png", x, y)
        self.detectado = False

    def escanear(self, presa):
        dx = presa.rect.x - self.rect.x
        dy = presa.rect.y - self.rect.y
        self.detectado = 0 < abs(dx) <= 6 * CELL_SIZE and 0 < abs(dy) <= 6 * CELL_SIZE

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

class Presa(Organismo):
    def __init__(self, x, y):
        super().__init__("presa.png", x, y)

    def mover_a_nueva_posicion(self):
        self.rect.x = random.randrange(WIDTH // CELL_SIZE) * CELL_SIZE
        self.rect.y = random.randrange(HEIGHT // CELL_SIZE) * CELL_SIZE

all_sprites = pygame.sprite.Group()

cazador = Animal(2 * CELL_SIZE, 2 * CELL_SIZE)
presa = Presa(3 * CELL_SIZE, 3 * CELL_SIZE)

all_sprites.add(cazador, presa)

tiempo_presa = pygame.time.get_ticks()
tiempo_cazador = pygame.time.get_ticks()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tiempo_actual_cazador = pygame.time.get_ticks()
    if tiempo_actual_cazador - tiempo_cazador > 500:
        cazador.escanear(presa)
        tiempo_cazador = tiempo_actual_cazador

    tiempo_actual_presa = pygame.time.get_ticks()
    if tiempo_actual_presa - tiempo_presa > 5000:
        presa.mover_a_nueva_posicion()
        tiempo_presa = tiempo_actual_presa

    if cazador.detectado:
        cazador.mover_hacia(presa)

    keys = pygame.key.get_pressed()
    cazador.rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * CELL_SIZE
    cazador.rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * CELL_SIZE

    screen.blit(fondo, (0, 0))

    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT), 1)
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y), 1)

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(10)