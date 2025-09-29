#
class Trayecto:
    def __init__(self, origen="", destino="", valor_pasaje=0):
        self.origen = origen
        self.destino = destino
        self.valor_pasaje = valor_pasaje
        self.pasajeros = []


    def registrar_pasajero(self, pasajero):
        self.pasajeros.append(pasajero)

