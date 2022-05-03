import csv
from operator import delitem
import numpy as np
from ClaseCama import Cama
import ManejadorMedicamentos

__ArregloCamas = np.empty(3,dtype=Cama)

__archivo = open("c:\\Users\\Usuario\\Desktop\\POO\\Unidad-2\\Ejercicio Integrador\\camas.csv")
__reader = csv.reader(__archivo, delimiter = ";")



banderaLectura = False
for files in __reader:
    if banderaLectura == False:
        banderaLectura = not banderaLectura
    else:
        UnaCama = Cama(files[0],files[1],files[2],files[3],files[4],files[5],files[6])
        __ArregloCamas[files[0]-1] = UnaCama
        

__archivo.close

def getCamaNombre(Nombre):
    camaADevolver = None
    i=0
    banderaNombre = False
    while i < len(__ArregloCamas) and banderaNombre == False:
        if(__ArregloCamas[i].getNombre() == Nombre):
            banderaNombre = True
        i+=1
    if(banderaNombre == True):
        camaADevolver = __ArregloCamas[i-1]
    return camaADevolver

def DarDeAlta(Nombre):
    CamaDeALta = getCamaNombre(Nombre)
    IdDecama = CamaDeALta.getIdCama()
    ListaMedicamentos = ManejadorMedicamentos.getListaDeMedicamentos()
    if(CamaDeALta != None):
        print("Paciente: {}          Cama:{}    Habitacion:{}\nDiagnostico: {}       Fecha De Internaion: {}".format(CamaDeALta.getNombre(),CamaDeALta.getIdCama(),CamaDeALta.getHabitacion(),CamaDeALta.getDiagnostico(),CamaDeALta.getFechaDeInternacion()))
        for i in range(len(ListaMedicamentos[IdDecama-1])):
            print(ListaMedicamentos[IdDecama-1][i].getNombreComercial())