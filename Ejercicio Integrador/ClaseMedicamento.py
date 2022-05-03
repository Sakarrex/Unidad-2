class Medicamento:
    __idCama = int
    __idMedicamento = int
    __nombreComercial = str
    __Monodroga = str
    __Presentacion = str
    __cantidadAplicada = int
    __PrecioTotal = int

    def __init__(self,idcama,idmedicamento,nombrecomercial,monodroga,presentacion,cantidadaplicada,preciototal):
        self.__idCama = int(idcama)
        self.__idMedicamento = int(idmedicamento)
        self.__nombreComercial = str(nombrecomercial)
        self.__Monodroga = str(monodroga)
        self.__Presentacion = str(presentacion)
        self.__cantidadAplicada = int(cantidadaplicada)
        self.__PrecioTotal = int(preciototal)
    
    def getNombreComercial(self):
        return self.__nombreComercial

    def getMonodroga(self):
        return self.__Monodroga
    
    def getPresentacion(self):
        return self.__Presentacion
    
    def getCantidad(self):
        return self.__cantidadAplicada
    
    def getPrecio(self):
        return self.__PrecioTotal
    
    def getIdcama(self):
        return self.__idCama