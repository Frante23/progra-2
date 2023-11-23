import pygame
import sys
import random

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

def dibujar_mapa_desierto(matriz):
    for fila in range(filas):
        for columna in range(columnas):
            if matriz[fila][columna] == 0:
                color = (194, 178, 128)  
            else:
                color = (0, 0, 255)  
            pygame.draw.rect(ventana, color, (columna * ancho_celda, fila * ancho_celda, ancho_celda, ancho_celda))

matriz = generar_desierto()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dibujar_mapa_desierto(matriz)

    pygame.display.flip()
