import pygame
import sys
import random
from eventos import Eventos

pygame.init()

filas = 20
columnas = 30
ancho_celda = 30
tamano_oasis = 5

ancho = columnas * ancho_celda
alto = filas * ancho_celda

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('desierto epico')

def generar_desierto():
    matriz = [[0] * columnas for _ in range(filas)]

    oasis_fila = random.randint(0, filas - tamano_oasis)
    oasis_columna = random.randint(0, columnas - tamano_oasis)

    for i in range(tamano_oasis):
        for j in range(tamano_oasis):
            matriz[oasis_fila + i][oasis_columna + j] = 1

    return matriz

def dibujar_desierto(matriz):
    for fila in range(filas):
        for columna in range(columnas):
            x = columna * ancho_celda
            y = fila * ancho_celda
            if matriz[fila][columna] == 0:
                pygame.draw.rect(ventana, (194, 178, 128), (x, y, ancho_celda, ancho_celda))
            elif matriz[fila][columna] == 1:
                pygame.draw.rect(ventana, (0, 0, 255), (x, y, ancho_celda, ancho_celda))
            elif matriz[fila][columna] == (139, 69, 19):  # color meteorito
                pygame.draw.rect(ventana, (139, 69, 19), (x, y, ancho_celda, ancho_celda))
                
    for fila in range(filas + 1):
        pygame.draw.line(ventana, (0, 0, 0), (0, fila * ancho_celda), (ancho, fila * ancho_celda), 2)

    for columna in range(columnas + 1):
        pygame.draw.line(ventana, (0, 0, 0), (columna * ancho_celda, 0), (columna * ancho_celda, alto), 2)

matriz = generar_desierto()
eventos = Eventos(filas, columnas)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    eventos.evento_aleatorio(matriz)
    
    ventana.fill((255, 255, 255))
    dibujar_desierto(matriz)
    eventos.color(matriz) 

    pygame.display.flip()