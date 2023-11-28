import pygame
import sys
import random
import time
from eventos import Eventos
from monitoreo import Monitoreo
from organismos import Animal, Presa
from organismos import planta1, planta2, planta3, planta4, planta5
from organismos import animal1, animal2, animal3, animal4, animal5, animal6, animal7, animal8, animal9, animal10
from organismos import presa1, presa2, presa3, presa4, presa5, presa6, presa7, presa8, presa9, presa10

pygame.init()

filas = 20
columnas = 30
ancho_celda = 30
tamano_oasis = 5

ancho = columnas * ancho_celda
alto = (filas + 2) * ancho_celda


ancho_imagen = 30
alto_imagen = 30
ancho_imagen_planta = 30
alto_imagen_planta = 30

animales = [animal1, animal2, animal3, animal4, animal5, animal6, animal7, animal8, animal9, animal10]
presas = [presa1, presa2, presa3, presa4, presa5, presa6, presa7, presa8, presa9, presa10]
plantas = [planta1, planta2, planta3, planta4, planta5]

for animal in animales:
    animal.imagen = pygame.transform.scale(animal.imagen, (ancho_imagen, alto_imagen))

for presa in presas:
    presa.imagen = pygame.transform.scale(presa.imagen, (ancho_imagen, alto_imagen))

for planta in plantas:
    planta.imagen = pygame.transform.scale(planta.imagen, (ancho_imagen_planta, alto_imagen_planta))


for presa in presas:
    presa.posicion = (random.randint(0, columnas - 1), random.randint(0, filas - 1))

for planta in plantas:
    planta.posicion = (random.randint(0, columnas - 1), random.randint(0, filas - 1))
    
    
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

def dibujar_desierto(matriz, eventos_registrados, nombre_evento, planta1, planta2, planta3, planta4, planta5):
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
        pygame.draw.line(ventana, (0, 0, 0), (0, fila * ancho_celda), (ancho, fila * ancho_celda), 2)

    for columna in range(columnas + 1):
        pygame.draw.line(ventana, (0, 0, 0), (columna * ancho_celda, 0), (columna * ancho_celda, alto), 2)

    for i in range(filas, filas + 2):
        pygame.draw.rect(ventana, (0, 0, 0), (0, i * ancho_celda, ancho, ancho_celda))

    for animal in animales:
        ventana.blit(animal.imagen, (animal.posicion[0] * ancho_celda, animal.posicion[1] * ancho_celda))

    for presa in presas:
        ventana.blit(presa.imagen, (presa.posicion[0] * ancho_celda, presa.posicion[1] * ancho_celda))

    for planta in plantas:
        posicion = (planta.posicion[0] * ancho_celda, planta.posicion[1] * ancho_celda)
        ventana.blit(planta.imagen, posicion)


    if eventos_registrados:
        ultimo_evento = eventos_registrados[-1]
        mensaje_evento = f"Evento: {nombre_evento}, Filas Afectadas: {ultimo_evento['filas_afectadas']}, Columnas Afectadas: {ultimo_evento['columnas_afectadas']}"
        fuente_evento = pygame.font.SysFont(None, 24)
        texto_evento = fuente_evento.render(mensaje_evento, True, (255, 255, 255))

        ventana.blit(texto_evento, (10, filas * ancho_celda))
        
matriz = generar_desierto()
eventos = Eventos(filas, columnas)
monitoreo = Monitoreo()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for animal in animales:
        animal.mover(filas, columnas)

    # Verificar reproducción entre animales
    nuevos_animales = []
    for animal1 in animales:
        for animal2 in animales:
            if animal1 != animal2:
                info_nuevo_animal = animal1.reproducir(animal2)
                if info_nuevo_animal is not None:
                    # Usa 'imagen_path' del diccionario info_nuevo_animal
                    nuevo_animal = Animal(**info_nuevo_animal)

                    nuevos_animales.append(nuevo_animal)


    # Agregar los nuevos animales al arreglo de animales
    animales.extend(nuevos_animales)
    
    
    for presa in [presa1, presa2, presa3, presa4, presa5]:
        presa.mover(filas, columnas)

    eventos.evento_aleatorio(matriz)

    filas_afectadas = eventos.filas_afectadas
    columnas_afectadas = eventos.columnas_afectadas

    monitoreo.recopilar_datos(eventos.tipo_evento, filas_afectadas, columnas_afectadas)

    ventana.fill((255, 255, 255))

    nombre_evento = eventos.obtener_nombre()

    dibujar_desierto(matriz, monitoreo.log, nombre_evento, planta1, planta2, planta3, planta4, planta5)
    eventos.color(matriz)

    if len(monitoreo.log) > 2:
        monitoreo.analisis()

    pygame.display.flip()
    pygame.time.Clock().tick(1)