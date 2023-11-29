import matplotlib.pyplot as plt
import numpy as np

class Monitoreo:
    def __init__(self):
        self.log = []   
        self.contador = {'leon': 0, 'coyote': 0, 'serpiente': 0, 'caracal': 0, 'escorpion': 0, 'raton': 0, 'lagartija': 0, 'pajaro': 0, 'gacela': 0, 'tortuga': 0}

    def recopilar_datos(self, tipo_evento, filas_afectadas, columnas_afectadas):
        evento = {
            'tipo_evento': tipo_evento,  
            'filas_afectadas': filas_afectadas,
            'columnas_afectadas': columnas_afectadas,
        }
        self.log.append(evento)

    def contar_especies(self, organismos):
        # Reiniciamos el conteo
        for especie in self.contador:
            self.contador[especie] = 0

        # Contamos las especies en la lista de organismos
        for organismo in organismos:
            especie = organismo.nombre.lower()
            self.contador[especie] += 1

        # Devolvemos las especies y cantidades
        especies = list(self.contador.keys())
        cantidades = list(self.contador.values())
        return especies, cantidades


    def analisis(self, organismos):
        for evento in self.log:
            print(f"Evento: {evento['tipo_evento']}")
            print(f"Filas Afectadas: {evento['filas_afectadas']}")
            print(f"Columnas Afectadas: {evento['columnas_afectadas']}")
            print("\n")

        # Cada 30 segundos, realiza el análisis y muestra el gráfico
        if len(self.log) > 0 and len(self.log) % 3 == 0:  # Analiza cada 3 eventos
            self.contar_especies(organismos)
            self.mostrar_grafico()

    def mostrar_grafico(self):
        especies = list(self.contador.keys())
        cantidades = list(self.contador.values())
        # Crear un gráfico de barras
        plt.bar(especies, cantidades, color='blue')
        plt.xlabel('Especies')
        plt.ylabel('Cantidad')
        plt.title('Evolución de la cantidad de animales de cada especie')
        plt.show()