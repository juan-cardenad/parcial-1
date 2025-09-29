class Vehiculotransportepublico:
    def __init__(self, placa="", trayecto=None,tipo=""):
        self.placa = placa
        self.trayecto = list(trayecto) if trayecto else []
        self.tipo = tipo

class BusetaInterveredal(Vehiculotransportepublico):
    def __init__(self, placa="", trayecto=None):
        super().__init__(placa, trayecto)
        self.tipo = "BusetaInterveredal"


class BusetaIntermunicipal(Vehiculotransportepublico):
    def __init__(self, placa="", trayecto=None):
        super().__init__(placa, trayecto)
        self.tipo = "BusetaIntermunicipal"


class MotoTaxi(Vehiculotransportepublico):
    def __init__(self, placa="", trayecto=None):
        super().__init__(placa, trayecto)
        self.tipo = "MotoTaxi"


#