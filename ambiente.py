import pygame
import sys
import random
import time
import pygame_gui
from organismos import Animal, Presa
from eventos import Eventos
from monitoreo import Monitoreo
from organismos import planta1, planta2, planta3, planta4, planta5, leon1, leon2, coyote1, coyote2, serpiente1, serpiente2, caracal1, caracal2, escorpion1, escorpion2, raton1, raton2, lagartija1, lagartija2, pajaro1, pajaro2, gacela1, gacela2, tortuga1, tortuga2

pygame.init()
pygame.font.init()

filas = 20
columnas = 30
ancho_celda = 30
tamano_oasis = 5

ancho = columnas * ancho_celda
alto = (filas + 5) * ancho_celda

ancho_imagen = 30
alto_imagen = 30

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ventana = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('destruccion')

evento_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

button_rect = pygame.Rect(50, 550, 100, 50)
button_meteorito = pygame_gui.elements.UIButton(relative_rect=button_rect, text='Meteorito', manager=evento_manager)
button_rect.x += 120
button_terremoto = pygame_gui.elements.UIButton(relative_rect=button_rect, text='Terremoto', manager=evento_manager)
button_rect.x += 120
button_tornado = pygame_gui.elements.UIButton(relative_rect=button_rect, text='Tornado', manager=evento_manager)
button_rect.x += 120
button_grafico = pygame_gui.elements.UIButton(relative_rect=button_rect, text='Grafico', manager=evento_manager)


plantas = [planta1, planta2, planta3, planta4, planta5]
organismos = [leon1, leon2, coyote1, coyote2, serpiente1, serpiente2, caracal1, caracal2, escorpion1, escorpion2, raton1, raton2, lagartija1, lagartija2, pajaro1, pajaro2, gacela1, gacela2, tortuga1, tortuga2]


for planta in plantas:
    planta.imagen = pygame.transform.scale(planta.imagen, (ancho_imagen, alto_imagen))
    
for planta in plantas:
    planta.posicion = (random.randint(0, columnas - 1), random.randint(0, filas - 1))
    
for organismo in organismos:
    organismo.imagen = pygame.transform.scale(organismo.imagen, (ancho_imagen, alto_imagen))
    
for organismo in organismos:
    organismo.posicion = (random.randint(0, columnas - 1), random.randint(0, filas - 1))
    
    
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

def dibujar_desierto(matriz, eventos_registrados, nombre_evento, plantas, organismos):
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

    for fila in range(filas, filas + 5):
        pygame.draw.rect(ventana, (0, 0, 0), (0, fila * ancho_celda, ancho, ancho_celda))

    for organismo in organismos:
        if 0 <= organismo.posicion[0] < columnas and 0 <= organismo.posicion[1] < filas:
            ventana.blit(organismo.imagen, (organismo.posicion[0] * ancho_celda, organismo.posicion[1] * ancho_celda))

    for planta in plantas:
        if 0 <= planta.posicion[0] < columnas and 0 <= planta.posicion[1] < filas:
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
monitoreo = Monitoreo(organismos)
tasa_reproduccion = 0.2
pausar= False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        evento_manager.process_events(event)

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button_meteorito:
                    eventos.tipo_evento = 'Meteorito'
                    eventos.matriz_original = [fila[:] for fila in matriz]
                    eventos.meteorito(matriz, organismos, plantas)
                    eventos.tiempo_impacto = pygame.time.get_ticks()
                elif event.ui_element == button_terremoto:
                    eventos.tipo_evento = 'Terremoto'
                    eventos.matriz_original = [fila[:] for fila in matriz]
                    eventos.terremoto(matriz, organismos, plantas)
                    eventos.tiempo_impacto = pygame.time.get_ticks()
                elif event.ui_element == button_tornado:
                    eventos.tipo_evento = 'Tornado'
                    eventos.matriz_original = [fila[:] for fila in matriz]
                    eventos.tornado(matriz, organismos, plantas)
                    eventos.tiempo_impacto = pygame.time.get_ticks()
                elif event.ui_element == button_grafico:
                    pausar = True
                    monitoreo.mostrar_grafico()

    evento_manager.update(30)

    eventos.evento_aleatorio(matriz, organismos, plantas)

    for organismo in organismos:
        organismo.mover(filas, columnas)
        organismo.posicion = (
            max(0, min(organismo.posicion[0], columnas - 1)),
            max(0, min(organismo.posicion[1], filas - 1))
        )
         # Verifica si el organismo es un animal y hay presas en su posición
        if isinstance(organismo, Animal):
            presas_posicion = [presa for presa in organismos if isinstance(presa, Presa) and presa.posicion == organismo.posicion]

            # Realiza la caza
            for presa in presas_posicion:
                organismo.cazar(presa, organismos)

    for organismo in organismos:
        if random.random() < tasa_reproduccion:
            pareja = random.choice(organismos)
            nuevo_organismo = organismo.reproducir(pareja)

            if nuevo_organismo is not None:
                organismos.append(nuevo_organismo)

    for planta in plantas:
        nueva_planta = planta.semillas()
        if nueva_planta is not None:
            nueva_planta.posicion = (
                max(0, min(nueva_planta.posicion[0], columnas - 1)),
                max(0, min(nueva_planta.posicion[1], filas - 1))
            )
            plantas.append(nueva_planta)

    filas_afectadas = eventos.filas_afectadas
    columnas_afectadas = eventos.columnas_afectadas

    monitoreo.recopilar_datos(eventos.tipo_evento, filas_afectadas, columnas_afectadas)
    monitoreo.analisis(organismos)

    ventana.fill((255, 255, 255))

    nombre_evento = eventos.obtener_nombre()

    dibujar_desierto(matriz, monitoreo.log, nombre_evento, plantas, organismos)
    eventos.color(matriz)

    evento_manager.draw_ui(ventana)
    pygame.display.flip()
    pygame.time.Clock().tick(1)