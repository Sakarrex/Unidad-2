class Registro:
    __temperatura = int
    __humedad = int
    __presiónAtmosferica = int
    def __init__(self, temp = -1000, humedad = -1000, presion= -1000):
        self.__temperatura = int(temp)
        self.__humedad = int(humedad)
        self.__presiónAtmosferica = int(presion)
    
    def getTemperatura(self):
        return int(self.__temperatura)

    def getHumedad(self):
        return int(self.__humedad)
    
    def getPresion(self):
        return int(self.__presiónAtmosferica)
    
    def getVariable(self, variable):
        __x = int
        if variable == 1:
           __x = self.getTemperatura()
        elif variable == 2:
            __x = self.getHumedad()
        elif variable == 3:
            __x = self.getPresion()
        else:
            __x = -9999999
        return int(__x)
        

