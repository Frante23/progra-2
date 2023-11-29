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
        self.tipo_evento = set()
        self.tiempo_limpiar = None 
        self.nombre_evento = None
        
    def obtener_nombre(self):
        return self.nombre_evento
        
    def reiniciar_datos(self):
        self.nombre_evento = None
        self.tiempo_impacto = None
        self.matriz_original = None
        self.filas_afectadas.clear()
        self.columnas_afectadas.clear()
        self.tipo_evento = None
        self.tiempo_limpiar = None

    def evento_aleatorio(self, matriz, organismos):  # Agregamos 'organismos' como parámetro
        if self.tiempo_limpiar is not None and pygame.time.get_ticks() - self.tiempo_limpiar >= 5000:
            self.reiniciar_datos()

        # Verifica si ha pasado 1 minuto desde el último meteorito
        if pygame.time.get_ticks() - self.siguiente_meteorito >= 15000:
            self.tipo_evento = 'Meteorito'
            self.matriz_original = [fila[:] for fila in matriz]
            self.meteorito(matriz, organismos)  # Pasamos 'organismos'
            self.tiempo_impacto = pygame.time.get_ticks()
            self.siguiente_meteorito = pygame.time.get_ticks()
            

        # Verifica si han pasado 2 minutos desde el último terremoto
        if pygame.time.get_ticks() - self.siguiente_terremoto >= 120000:
            self.tipo_evento = 'Terremoto'
            self.matriz_original = [fila[:] for fila in matriz]
            self.terremoto(matriz, organismos)
            self.tiempo_impacto = pygame.time.get_ticks()
            self.siguiente_terremoto = pygame.time.get_ticks()

        # Verifica si ha pasado 1.30 minuto desde el último tornado
        if pygame.time.get_ticks() - self.siguiente_tornado >= 90000:
            self.tipo_evento = 'Tornado'
            self.matriz_original = [fila[:] for fila in matriz]
            self.tornado(matriz, organismos)
            self.tiempo_impacto = pygame.time.get_ticks()
            self.siguiente_tornado = pygame.time.get_ticks()

        # Verifica si han pasado 10 segundos desde el impacto
        if self.tiempo_impacto is not None and pygame.time.get_ticks() - self.tiempo_impacto >= 10000:
            self.revertir_impacto(matriz)
            
        if self.tiempo_impacto is not None and pygame.time.get_ticks() - self.tiempo_impacto >= 5000:
            self.filas_afectadas.clear()
            self.columnas_afectadas.clear()
            self.tiempo_limpiar = pygame.time.get_ticks()
            
    def afecta_posicion(self, fila, columna):
        return fila in self.filas_afectadas and columna in self.columnas_afectadas

    def impacto_organismos(self, organismos):
        for organismo in organismos:
            if self.afecta_posicion(organismo.posicion[1], organismo.posicion[0]):
                organismos.remove(organismo)

    def meteorito(self, matriz, organismos):
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
                self.nombre_evento = 'Meteorito'
                print("Tipo de evento:", self.tipo_evento)
                self.impacto_organismos(organismos)

    def terremoto(self, matriz, organismos):
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
                    self.nombre_evento = 'Terremoto'
                    print("Tipo de evento:", self.tipo_evento)
                    self.impacto_organismos(organismos)
                    
    def tornado(self, matriz, organismos):
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
                    self.nombre_evento = 'Tornado'
                    print("Tipo de evento:", self.tipo_evento)
                    self.impacto_organismos(organismos)


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
