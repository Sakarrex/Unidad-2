from numpy import true_divide


class Conjunto:
    __ListaNumeros = []
    
    def __init__(self):
        self.__ListaNumeros = []

    def getConjunto(self):
        return self.__ListaNumeros
     
    def agregarValor(self,valor):
       
        if valor > 0:
            self.__ListaNumeros.append(valor)
        else:
            print("Error")
        
    def __add__(self,otro):
        if type(otro) == Conjunto:
            conjunto1 = self.__ListaNumeros
            conjunto2 = otro.getConjunto()
            for i in range(len(conjunto2)):
                if conjunto2[i] not in conjunto1:
                    conjunto1.append(conjunto2[i])

            return conjunto1
    
    def __sub__(self,otro):
        if type(otro) == Conjunto:
            ConjuntoDiferencia = []
            for i in range(len(self.__ListaNumeros)):
                if self.__ListaNumeros[i] not in otro.getConjunto():
                    ConjuntoDiferencia.append(self.__ListaNumeros[i])
            return ConjuntoDiferencia
    
    def __eq__(self,otro):
        if type(otro) == Conjunto:
            bandera = True
          
            conjunto1 = self.__ListaNumeros
            conjunto2 = otro.getConjunto()
            
            if(len(conjunto1) == len(conjunto2)):
                
                i = 0
                while i < len(conjunto1) and bandera == True:
                    if conjunto1[i] not in conjunto2:
                        bandera = False
                    i+=1
                
            else:
                bandera = False
            
            return bandera