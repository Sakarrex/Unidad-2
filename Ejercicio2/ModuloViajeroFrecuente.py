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

    def cantidadTotalMillas(self):
        return self.__millas_acum
    
    def acumularMillas(self, cantidadMillas):
        self.__millas_acum = self.__millas_acum + cantidadMillas
        return self.__millas_acum
    
    def canjearMillas(self, cantidadMillas):
        if(cantidadMillas <= self.__millas_acum):
            print("Millas acumuladas")
            self.__millas_acum -= cantidadMillas
        else:
            print("Cantidad Insuficiente de millas acumuladas")   
        return self.__millas_acum

    def muestra(self):
        return str(self.__num_viajero) +" "+ self.__dni + self.__nombre + self.__apellido + str(self.__millas_acum)