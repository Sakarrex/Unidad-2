class Registro:
    __temperatura = int
    __humedad = int
    __presiónAtmosferica = int
    def __init__(self, temp = -1000, humedad = -1000, presion= -1000):
        self.__temperatura = int(temp)
        self.__humedad = int(humedad)
        self.__presiónAtmosferica = int(presion)
    
    def getTemperatura(self):
        return str(self.__temperatura)

    def getHumedad(self):
        return str(self.__humedad)
    
    def getPresion(self):
        return str(self.__presiónAtmosferica)