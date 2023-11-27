import pygame
import sys
import random
from eventos import Eventos
from monitoreo import Monitoreo
from organismos import planta1, planta2, planta3, planta4, planta5
from organismos import animal1, animal2, animal3, animal4, animal5
from organismos import presa1, presa2, presa3, presa4, presa5

pygame.init()

filas = 20
columnas = 30
ancho_celda = 30
tamano_oasis = 5

ancho = columnas * ancho_celda
alto = (filas + 2) * ancho_celda


animal1.imagen = pygame.transform.scale(animal1.imagen, (ancho_celda, ancho_celda))
animal2.imagen = pygame.transform.scale(animal2.imagen, (ancho_celda, ancho_celda))
animal3.imagen = pygame.transform.scale(animal3.imagen, (ancho_celda, ancho_celda))
animal4.imagen = pygame.transform.scale(animal4.imagen, (ancho_celda, ancho_celda))
animal5.imagen = pygame.transform.scale(animal5.imagen, (ancho_celda, ancho_celda))

presa1.imagen = pygame.transform.scale(presa1.imagen, (ancho_celda, ancho_celda))
presa2.imagen = pygame.transform.scale(presa2.imagen, (ancho_celda, ancho_celda))
presa3.imagen = pygame.transform.scale(presa3.imagen, (ancho_celda, ancho_celda))
presa4.imagen = pygame.transform.scale(presa4.imagen, (ancho_celda, ancho_celda))
presa5.imagen = pygame.transform.scale(presa5.imagen, (ancho_celda, ancho_celda))

planta1.imagen = pygame.transform.scale(planta1.imagen, (ancho_celda, ancho_celda))
planta2.imagen = pygame.transform.scale(planta2.imagen, (ancho_celda, ancho_celda))
planta3.imagen = pygame.transform.scale(planta3.imagen, (ancho_celda, ancho_celda))
planta4.imagen = pygame.transform.scale(planta4.imagen, (ancho_celda, ancho_celda))
planta5.imagen = pygame.transform.scale(planta5.imagen, (ancho_celda, ancho_celda))

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('desierto epico')

def generar_desierto():
    matriz = [[0] * columnas for _ in range(filas)]

    oasis_fila = random.randint(0, filas - tamano_oasis)
    oasis_columna = random.randint(0, columnas - tamano_oasis)

    for i in range(tamano_oasis):
        for j in range(tamano_oasis):
            matriz[oasis_fila + i][oasis_columna + j] = 1

    for _ in range(5):  
        fila_planta = random.randint(0, filas - 1)
        columna_planta = random.randint(0, columnas - 1)

        while oasis_fila <= fila_planta < oasis_fila + tamano_oasis and oasis_columna <= columna_planta < oasis_columna + tamano_oasis:
            fila_planta = random.randint(0, filas - 1)
            columna_planta = random.randint(0, columnas - 1)

        matriz[fila_planta][columna_planta] = 2  

    return matriz



def dibujar_desierto(matriz, eventos_registrados, nombre_evento, planta1, planta2, planta3, planta4, planta5, animal1, animal2, animal3, animal4, animal5, presa1, presa2, presa3, presa4, presa5):
    for fila in range(filas):
        for columna in range(columnas):
            x = columna * ancho_celda
            y = fila * ancho_celda
            if matriz[fila][columna] == 0:
                pygame.draw.rect(ventana, (194, 178, 128), (x, y, ancho_celda, ancho_celda))
            elif matriz[fila][columna] == 1:
                pygame.draw.rect(ventana, (0, 0, 255), (x, y, ancho_celda, ancho_celda))
            elif matriz[fila][columna] == 2: 
                planta_actual = None
                for planta in [planta1, planta2, planta3, planta4, planta5]:
                    if planta.posicion == (columna, fila):
                        planta_actual = planta
                        break

                if planta_actual:
                    ventana.blit(planta_actual.imagen, (x, y))
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

    ventana.blit(animal1.imagen, (animal1.posicion[0] * ancho_celda, animal1.posicion[1] * ancho_celda))
    ventana.blit(animal2.imagen, (animal2.posicion[0] * ancho_celda, animal2.posicion[1] * ancho_celda))
    ventana.blit(animal3.imagen, (animal3.posicion[0] * ancho_celda, animal3.posicion[1] * ancho_celda))
    ventana.blit(animal4.imagen, (animal4.posicion[0] * ancho_celda, animal4.posicion[1] * ancho_celda))
    ventana.blit(animal5.imagen, (animal5.posicion[0] * ancho_celda, animal5.posicion[1] * ancho_celda))

    ventana.blit(presa1.imagen, (presa1.posicion[0] * ancho_celda, presa1.posicion[1] * ancho_celda))
    ventana.blit(presa2.imagen, (presa2.posicion[0] * ancho_celda, presa2.posicion[1] * ancho_celda))
    ventana.blit(presa3.imagen, (presa3.posicion[0] * ancho_celda, presa3.posicion[1] * ancho_celda))
    ventana.blit(presa4.imagen, (presa4.posicion[0] * ancho_celda, presa4.posicion[1] * ancho_celda))
    ventana.blit(presa5.imagen, (presa5.posicion[0] * ancho_celda, presa5.posicion[1] * ancho_celda))

    ventana.blit(planta1.imagen, (planta1.posicion[0] * ancho_celda, planta1.posicion[1] * ancho_celda))
    ventana.blit(planta2.imagen, (planta2.posicion[0] * ancho_celda, planta2.posicion[1] * ancho_celda))
    ventana.blit(planta3.imagen, (planta3.posicion[0] * ancho_celda, planta3.posicion[1] * ancho_celda))
    ventana.blit(planta4.imagen, (planta4.posicion[0] * ancho_celda, planta4.posicion[1] * ancho_celda))
    ventana.blit(planta5.imagen, (planta5.posicion[0] * ancho_celda, planta5.posicion[1] * ancho_celda))


    for i, evento in enumerate(eventos_registrados):
        mensaje = f"Evento {i + 1}: {nombre_evento}, Filas Afectadas: {evento['filas_afectadas']}, Columnas Afectadas: {evento['columnas_afectadas']}"
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

    for animal in [animal1, animal2, animal3, animal4, animal5]:
        animal.mover(columnas, filas)

    for presa in [presa1, presa2, presa3, presa4, presa5]:
        presa.mover(columnas, filas)

    eventos.evento_aleatorio(matriz)

    filas_afectadas = eventos.filas_afectadas
    columnas_afectadas = eventos.columnas_afectadas

    monitoreo.recopilar_datos(eventos.tipo_evento, filas_afectadas, columnas_afectadas)

    ventana.fill((255, 255, 255))
    
    nombre_evento = eventos.obtener_nombre()

    dibujar_desierto(matriz, monitoreo.log, nombre_evento, planta1, planta2, planta3, planta4, planta5, animal1, animal2, animal3, animal4, animal5, presa1, presa2, presa3, presa4, presa5)
    eventos.color(matriz)

    if len(monitoreo.log) > 2:
        monitoreo.analisis()

    pygame.display.flip()
    pygame.time.Clock().tick(10) 