import csv
from ClaseMedicamento import Medicamento


__ListaMedicamentos = []


__archivo = open("c:\\Users\\Usuario\\Desktop\\POO\\Unidad-2\\Ejercicio Integrador\\medicamentos.csv")
__reader = csv.reader(__archivo, delimiter = ";")

__bandera = False
for file in __reader:
    if __bandera == False:
        __bandera = not __bandera
    else:
        Unmedicamento = Medicamento(file[0],file[1],file[2],file[3],file[4],file[5],file[6])
        __ListaMedicamentos.append(Unmedicamento)



__archivo.close

def getListaDeMedicamentos():
    return __ListaMedicamentos


            
