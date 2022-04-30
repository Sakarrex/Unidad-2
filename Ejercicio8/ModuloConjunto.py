class Conjunto:
    __ListaNumeros = []
    __tamano = int

    def __init__(self, tamano):
        self.__tamano = int(tamano)
        
    
    def getConjunto(self):
        return self.__ListaNumeros

    def getTamano(self):
        return self.__tamano
    
    def getlen(self):
        return len(self.__ListaNumeros)
    
    def agregarValor(self, valor):
        #print("Lista: {}".format(len(self.__ListaNumeros)))
        if len(self.__ListaNumeros) < self.__tamano and valor > 0:
            self.__ListaNumeros.append(valor)
        else:
            print("Error")

    def __add__(self,otro):
        if type(otro) == Conjunto:
            conjunto1 = sorted(self.__ListaNumeros)
            conjunto2 = sorted(otro.getConjunto())
            conjuntoUnion = conjunto1+conjunto2
            for i in range(len(conjuntoUnion)):
                valorActual = conjuntoUnion[i]
                for j in range(i+1,len(conjuntoUnion)):
                    if valorActual == conjuntoUnion[j]:
                        conjuntoUnion.pop(j)
            return conjuntoUnion
            