import csv
from ClaseMedicamento import Medicamento


__ListaCama = []
__cantidadDecamas = 3
for i in range(__cantidadDecamas):
    __ListaCama.append([])

__archivo = open("c:\\Users\\Usuario\\Desktop\\POO\\Unidad-2\\Ejercicio Integrador\\medicamentos.csv")
__reader = csv.reader(__archivo, delimiter = ";")

__bandera = False
for file in __reader:
    if __bandera == False:
        __bandera = not __bandera
    else:
        x = (int(file[0]))-1
        y = (int(file[1]))-1
        Unmedicamento = Medicamento(file[0],file[1],file[2],file[3],file[4],file[5],file[6])
        __ListaCama[x].append()

__archivo.close

def getListaDeMedicamentos(self):
    return __ListaCama
            
