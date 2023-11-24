import random
import pygame.time

class Eventos:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.tiempo_impacto = None
        self.matriz_original = None
        self.siguiente_meteorito = pygame.time.get_ticks()
        self.siguiente_terremoto = pygame.time.get_ticks()
        self.siguiente_tornado = pygame.time.get_ticks()
        self.filas_afectadas = set()
        self.columnas_afectadas = set()
        self.tipo_evento = None

    def reiniciar_datos(self):
        self.tiempo_impacto = None
        self.matriz_original = None
        self.filas_afectadas = set()
        self.columnas_afectadas = set()
        self.tipo_evento = None
        
    def evento_aleatorio(self, matriz):
        # Verifica si ha pasado 1 minuto desde el último meteorito
        if pygame.time.get_ticks() - self.siguiente_meteorito >= 15000:
            self.reiniciar_datos()
            self.tipo_evento = 'Meteorito'  # Añade esta línea
            self.matriz_original = [fila[:] for fila in matriz]
            self.meteorito(matriz)
            self.tiempo_impacto = pygame.time.get_ticks()
            self.siguiente_meteorito = pygame.time.get_ticks()

        # Verifica si han pasado 2 minutos desde el último terremoto
        if pygame.time.get_ticks() - self.siguiente_terremoto >= 120000:
            self.reiniciar_datos()
            self.tipo_evento = 'Terremoto'
            self.matriz_original = [fila[:] for fila in matriz]
            self.terremoto(matriz)
            self.tiempo_impacto = pygame.time.get_ticks()
            self.siguiente_terremoto = pygame.time.get_ticks()

        # Verifica si ha pasado 1.30 minuto desde el último tornado
        if pygame.time.get_ticks() - self.siguiente_tornado >= 90000:
            self.reiniciar_datos()
            self.tipo_evento = 'Tornado'
            self.matriz_original = [fila[:] for fila in matriz]
            self.tornado(matriz)
            self.tiempo_impacto = pygame.time.get_ticks()
            self.siguiente_tornado = pygame.time.get_ticks()

        # Verifica si han pasado 10 segundos desde el impacto
        if self.tiempo_impacto is not None and pygame.time.get_ticks() - self.tiempo_impacto >= 10000:
            self.revertir_impacto(matriz)

    def meteorito(self, matriz):
        fila_meteorito = random.randint(0, self.filas - 1)
        columna_meteorito = random.randint(0, self.columnas - 1)

        radio_meteorito = 2  

        for i in range(-radio_meteorito, radio_meteorito + 1):
            for j in range(-radio_meteorito, radio_meteorito + 1):
                nueva_fila = fila_meteorito + i
                nueva_columna = columna_meteorito + j

                if 0 <= nueva_fila < self.filas and 0 <= nueva_columna < self.columnas:
                    matriz[nueva_fila][nueva_columna] = 'impacto_meteorito'  
                    
                    # Agrega las filas y columnas afectadas al registro
                    self.filas_afectadas.add(nueva_fila)
                    self.columnas_afectadas.add(nueva_columna)
                    self.tipo_evento = 'Meteorito'
                    print("Tipo de evento:", self.tipo_evento)

    def terremoto(self, matriz):
        fila_terremoto = random.randint(0, self.filas - 1)
        columna_terremoto = random.randint(0, self.columnas - 1)

        radio_terremoto = 5  

        for i in range(-radio_terremoto, radio_terremoto + 1):
            for j in range(-radio_terremoto, radio_terremoto + 1):
                nueva_fila = fila_terremoto + i
                nueva_columna = columna_terremoto + j

                if 0 <= nueva_fila < self.filas and 0 <= nueva_columna < self.columnas:
                    matriz[nueva_fila][nueva_columna] = 'impacto_terremoto'  
                    
                    self.filas_afectadas.add(nueva_fila)
                    self.columnas_afectadas.add(nueva_columna)
                    
                    self.tipo_evento = 'Terremoto'
                    print("Tipo de evento:", self.tipo_evento)
                    
    def tornado(self, matriz):
        fila_tornado = random.randint(0, self.filas - 1)
        columna_tornado = random.randint(0, self.columnas - 1)

        radio_tornado = 3

        for i in range(-radio_tornado, radio_tornado + 1):
            for j in range(-radio_tornado, radio_tornado + 1):
                nueva_fila = fila_tornado + i
                nueva_columna = columna_tornado + j

                if 0 <= nueva_fila < self.filas and 0 <= nueva_columna < self.columnas:
                    matriz[nueva_fila][nueva_columna] = 'impacto_tornado'
                    
                    self.filas_afectadas.add(nueva_fila)
                    self.columnas_afectadas.add(nueva_columna)
                    self.tipo_evento = 'Tornado'
                    print("Tipo de evento:", self.tipo_evento)


    def color(self, matriz):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if matriz[fila][columna] == 'impacto_meteorito':
                    matriz[fila][columna] = (255, 0, 0)  
                elif matriz[fila][columna] == 'impacto_terremoto':
                    matriz[fila][columna] = (139, 69, 19)  
                elif matriz[fila][columna] == 'impacto_tornado':
                    matriz[fila][columna] = (255, 165, 0)

    def revertir_impacto(self, matriz):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                matriz[fila][columna] = self.matriz_original[fila][columna]  

        self.tiempo_impacto = None  
