from datetime import date


class Cama:
    __idCama = int
    __habitacion = int
    __estado = bool
    __apellidoNombre = str
    __diagnostico = str
    __fechaDeInternacion = str
    __fechaDeAlta= str

    def __init__(self,idCama = 0, habitacion = 0, estado = False, nombre = "Vacio", diagnostico = "Vacio", fechaDeInternacion = "Vacio", fechaDeAlta = "Vacio"):
        self.__idCama = int(idCama)
        self.__habitacion = int(habitacion)
        self.__estado = bool(estado)
        self.__apellidoNombre = str(nombre)
        self.__diagnostico = str(diagnostico)
        self.__fechaDeInternacion = str(fechaDeInternacion)
        self.__fechaDeAlta = str(fechaDeAlta)
    
    def getNombre(self):
        return self.__apellidoNombre
    
    def getIdCama(self):
        return self.__idCama
    
    def getHabitacion(self):
        return self.__habitacion

    def getDiagnostico(self):
        return self.__diagnostico
    
    def getFechaDeInternacion(self):
        return self.__fechaDeInternacion
