import random
import pygame.time

class Eventos:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.tiempo_impacto = None  
        self.matriz_original = None  
        self.siguiente_meteorito = pygame.time.get_ticks()  

    def evento_aleatorio(self, matriz):
        if pygame.time.get_ticks() - self.siguiente_meteorito >= 60000:
            self.matriz_original = [fila[:] for fila in matriz]  
            self.meteorito(matriz)
            self.tiempo_impacto = pygame.time.get_ticks() 
            self.siguiente_meteorito = pygame.time.get_ticks() 

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
                    

    def color(self, matriz):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if matriz[fila][columna] == 'impacto_meteorito':
                    matriz[fila][columna] = (139, 69, 19) 
                    
                    
    def revertir_impacto(self, matriz):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                matriz[fila][columna] = self.matriz_original[fila][columna]  

        self.tiempo_impacto = None  
