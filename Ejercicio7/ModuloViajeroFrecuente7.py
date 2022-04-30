import string


class ViajeroFrecuente:
    __num_viajero = int
    __dni = string
    __nombre = string
    __apellido = string
    __millas_acum = int

    def __init__(self, num_viajero = -1, dni = '-1', nombre = 'vacio', apellido = 'vacio', millas_acumuladas = -1):
        self.__num_viajero = int(num_viajero)
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = int(millas_acumuladas)

    def cantidadTotaldeMillas(self):
        return self.__millas_acum
    
    def acumularMillas(self, cantidadMillas):
        self.__millas_acum = self.__millas_acum + cantidadMillas
        return self.__millas_acum
    
    def canjearMillas(self, cantidadMillas):
        if(cantidadMillas <= self.__millas_acum):
            self.__millas_acum -= cantidadMillas
        else:
            print("Cantidad Insuficiente de millas acumuladas")   
        return self.__millas_acum

    def muestra(self):
        return str(self.__num_viajero) +" "+ self.__dni + " " + self.__nombre + " " + self.__apellido + " " +str(self.__millas_acum)
    
    def getNumeroViajero(self):
        return self.__num_viajero

    def __gt__(self,otro):
        if type(otro) == ViajeroFrecuente:
            return self.__millas_acum > otro.__millas_acum
    
    def __eq__(self, otro):
        return

    def __add__(self, otro):
        if type(otro) == int:
            self.__millas_acum += otro
    
    def _radd_(self,otro):
        if type(otro) == int:
            self
   
    def __sub__(self,otro):
        if type(otro) == int:
           return self.__millas_acum - otro

    def __rsub__(self,otro):
        if type(otro) == int:
            return otro - self.__millas_acum
    

  