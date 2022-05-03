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
    
    def __str__(self):
        return "IdCama: {}\nHabitacion: {}\nNombre y apellido: {}\nDiagnostico: {}\nFecha de Internacion: {}".format(self.__idCama,self.__habitacion,self.__apellidoNombre,self.__diagnostico,self.__fechaDeInternacion)


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
    
    def ActualizarAlta(self,alta):
        self.__fechaDeAlta = alta

    def getAlta(self):
        return self.__fechaDeAlta
    
    def getEstado(self):
        return self.__estado