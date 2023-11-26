import pygame
import sys
import random  
from eventos import Eventos
from monitoreo import Monitoreo

pygame.init()

filas = 20
columnas = 30
ancho_celda = 30
tamano_oasis = 5

ancho = columnas * ancho_celda
alto = (filas + 2) * ancho_celda 

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

def dibujar_desierto(matriz, eventos_registrados):
    for fila in range(filas):
        for columna in range(columnas):
            x = columna * ancho_celda
            y = fila * ancho_celda
            if matriz[fila][columna] == 0:
                pygame.draw.rect(ventana, (194, 178, 128), (x, y, ancho_celda, ancho_celda))
            elif matriz[fila][columna] == 1:
                pygame.draw.rect(ventana, (0, 0, 255), (x, y, ancho_celda, ancho_celda))
            elif matriz[fila][columna] == (255, 0, 0):  # color meteorito
                pygame.draw.rect(ventana, (255, 0, 0), (x, y, ancho_celda, ancho_celda))
            elif matriz[fila][columna] == (139, 69, 19):  # color terremoto
                pygame.draw.rect(ventana, (139, 69, 19), (x, y, ancho_celda, ancho_celda))
            elif matriz[fila][columna] == (255, 165, 0):  # color tornado
                pygame.draw.rect(ventana, (255, 165, 0), (x, y, ancho_celda, ancho_celda))

                
    for fila in range(filas + 1):
        pygame.draw.line(ventana, (0, 0, 0), (0, fila * ancho_celda), (ancho, fila * ancho_celda), 2)

    for columna in range(columnas + 1):
        pygame.draw.line(ventana, (0, 0, 0), (columna * ancho_celda, 0), (columna * ancho_celda, alto), 2)
        
    for i in range(filas, filas + 2):
        pygame.draw.rect(ventana, (0, 0, 0), (0, i * ancho_celda, ancho, ancho_celda))
        
    for i, evento in enumerate(eventos_registrados):
        mensaje = f"Evento {i + 1}: {evento['tipo_evento']}, Filas Afectadas: {evento['filas_afectadas']}, Columnas Afectadas: {evento['columnas_afectadas']}"
        fuente = pygame.font.SysFont(None, 24)
        texto = fuente.render(mensaje, True, (255, 255, 255))
        ventana.blit(texto, (10, (filas + i) * ancho_celda))

matriz = generar_desierto()
eventos = Eventos(filas, columnas)
monitoreo = Monitoreo()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    eventos.evento_aleatorio(matriz)

    filas_afectadas = eventos.filas_afectadas
    columnas_afectadas = eventos.columnas_afectadas

    monitoreo.recopilar_datos(eventos.tipo_evento, filas_afectadas, columnas_afectadas)

    ventana.fill((255, 255, 255))
    
    dibujar_desierto(matriz, monitoreo.log)
    eventos.color(matriz)

    if len(monitoreo.log) > 2:  
        monitoreo.analisis()

    pygame.display.flip()