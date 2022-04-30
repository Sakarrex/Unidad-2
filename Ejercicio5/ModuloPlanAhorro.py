import re


class PlandeAhorro:
    __codigo = int
    __modeloVehiculo = str
    __versionVehiculo = str
    __valorVehiculo = int
    __cantidadCuotasPlan = 60
    __cantidadDeCoutasLicitas = 10
    
    def __init__(self, codigo = 0, modelo = "Vacio", version = "Vacio", valor = 0):
        self.__codigo = int(codigo)
        self.__modeloVehiculo = str(modelo)
        self.__versionVehiculo = str(version)
        self.__valorVehiculo = int(valor)
    
    def __str__(self):
        return "Codigo: {}, Modelo: {}, Version: {}, Valor:{}, Cantidad de cuotas: {}, Cantidad de cuotas licitas: {}".format(self.__codigo,self.__modeloVehiculo,self.__versionVehiculo,self.__valorVehiculo,PlandeAhorro.__cantidadCuotasPlan,PlandeAhorro.__cantidadDeCoutasLicitas)
    
    def getCodigo(self):
        return self.__codigo
    
    def getModelo(self):
        return self.__modeloVehiculo
    
    def getVersion(self):
        return self.__versionVehiculo
    
    def actualizarValor(self,valor):
        self.__valorVehiculo = valor
    
    def valorDeCuota(self):
        return ((self.__valorVehiculo/PlandeAhorro.__cantidadCuotasPlan) + self.__valorVehiculo *0.10)
    
    @classmethod
    def getCantidadCuotasLicitas(cls):
        return PlandeAhorro.__cantidadDeCoutasLicitas
    
    @classmethod
    def setCantidadCuotasLicitas(cls,valor):
        PlandeAhorro.__cantidadDeCoutasLicitas = valor