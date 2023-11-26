import pygame
import sys
import random
from eventos import Eventos
from monitoreo import Monitoreo
from cazador import Animal
from presa import Presa

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

CELL_SIZE = 40
WIDTH, HEIGHT = 800, 600

ventana = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("La caza en el desierto")

all_sprites = pygame.sprite.Group()


cazador = Animal("cazador.png", CELL_SIZE, CELL_SIZE)
presa = Presa("presa.png", 2 * CELL_SIZE, 2 * CELL_SIZE)

all_sprites.add(cazador, presa)


filas = 20
columnas = 30
ancho_celda = 30
tamano_oasis = 5

matriz = [[0] * columnas for _ in range(filas)]
eventos = Eventos(filas, columnas)
monitoreo = Monitoreo()

def dibujar_desierto(matriz, eventos_registrados):
    for fila in range(filas):
        for columna in range(columnas):
            x = columna * ancho_celda
            y = fila * ancho_celda
            if matriz[fila][columna] == 0:
                pygame.draw.rect(ventana, (194, 178, 128), (x, y, ancho_celda, ancho_celda))
            elif matriz[fila][columna] == 1:
                pygame.draw.rect(ventana, (0, 0, 255), (x, y, ancho_celda, ancho_celda))
            elif matriz[fila][columna] == (255, 0, 0):
                pygame.draw.rect(ventana, (255, 0, 0), (x, y, ancho_celda, ancho_celda))
            elif matriz[fila][columna] == (139, 69, 19):
                pygame.draw.rect(ventana, (139, 69, 19), (x, y, ancho_celda, ancho_celda))
            elif matriz[fila][columna] == (255, 165, 0):
                pygame.draw.rect(ventana, (255, 165, 0), (x, y, ancho_celda, ancho_celda))

    for fila in range(filas + 1):
        pygame.draw.line(ventana, (0, 0, 0), (0, fila * ancho_celda), (WIDTH, fila * ancho_celda), 2)

    for columna in range(columnas + 1):
        pygame.draw.line(ventana, (0, 0, 0), (columna * ancho_celda, 0), (columna * ancho_celda, HEIGHT), 2)

    for i in range(filas, filas + 2):
        pygame.draw.rect(ventana, (0, 0, 0), (0, i * ancho_celda, WIDTH, ancho_celda))

    for i, evento in enumerate(eventos_registrados):
        tipo_evento = evento['tipo_evento'] if evento['tipo_evento'] else 'Evento Desconocido'
        mensaje = f"Evento {i + 1}: {tipo_evento}, Filas Afectadas: {evento['filas_afectadas']}, Columnas Afectadas: {evento['columnas_afectadas']}"
        fuente = pygame.font.SysFont(None, 24)
        texto = fuente.render(mensaje, True, (255, 255, 255))
        ventana.blit(texto, (10, (filas + i) * ancho_celda))

clock = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tiempo_actual_cazador = pygame.time.get_ticks()
    if tiempo_actual_cazador - tiempo_cazador > 500:
        cazador.escanear(presa, ventana)
        tiempo_cazador = tiempo_actual_cazador

        if cazador.detectado:
            cazador.mover_hacia(presa)
        else:
            direccion_aleatoria = random.choice([(CELL_SIZE, 0), (-CELL_SIZE, 0), (0, CELL_SIZE), (0, -CELL_SIZE)])
            cazador.rect.x += direccion_aleatoria[0]
            cazador.rect.y += direccion_aleatoria[1]

    tiempo_actual_presa = pygame.time.get_ticks()
    if tiempo_actual_presa - tiempo_presa > 500:
        presa.arrancar()
        tiempo_presa = tiempo_actual_presa

    cazador.rect.x = max(CELL_SIZE, min(cazador.rect.x, WIDTH - 2 * CELL_SIZE))
    cazador.rect.y = max(CELL_SIZE, min(cazador.rect.y, HEIGHT - 2 * CELL_SIZE))

    presa.rect.x = max(CELL_SIZE, min(presa.rect.x, WIDTH - CELL_SIZE))
    presa.rect.y = max(CELL_SIZE, min(presa.rect.y, HEIGHT - CELL_SIZE))

    ventana.fill(WHITE)
    
    dibujar_desierto(matriz, monitoreo.log)
    
    all_sprites.update()
    all_sprites.draw(ventana)

    pygame.display.flip()

    clock.tick(10)
