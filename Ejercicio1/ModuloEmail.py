import string


class Email:
    __idDeCuenta: string
    __dominio:string
    __tipoDeDominio:string
    __contraseña:string

    def __init__(self,id ="vacio",dominio = "vacio",tipoDedominio = "vacio",contra = "vacio"):
        self.__idDeCuenta = id
        self.__dominio=dominio
        self.__tipoDeDominio=tipoDedominio
        self.__contraseña=contra

    def retornaEmail(self):
        return self.__idDeCuenta+"@"+self.__dominio+"."+self.__tipoDeDominio

    def getDominio(self):
        return self.__dominio

    def getContraseña(self):
        return self.__contraseña

    def setContraseña(self,contraseña):
        self.__contraseña = contraseña

    def crearCuenta(self, correo):
        Split1=correo.split('@')
        self.__idDeCuenta=Split1[0]
        Split2=Split1[1].split('.')
        self.__dominio=Split2[0]
        self.__tipoDeDominio=Split2[1]
        print("Ingresar contraseña")
        self.__contraseña = input()

    def getId(self):
        return self.__idDeCuenta
