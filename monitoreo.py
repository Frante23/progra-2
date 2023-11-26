class Monitoreo:
    def __init__(self):
        self.log = []   

    def recopilar_datos(self, tipo_evento, filas_afectadas, columnas_afectadas):
        evento = {
            'tipo_evento': tipo_evento ,  
            'filas_afectadas': filas_afectadas,
            'columnas_afectadas': columnas_afectadas,
        }
        self.log.append(evento)

    def analisis(self):
        for evento in self.log:
            print(f"Evento: {evento['tipo_evento']}")
            print(f"Filas Afectadas: {evento['filas_afectadas']}")
            print(f"Columnas Afectadas: {evento['columnas_afectadas']}")
            print("\n")
