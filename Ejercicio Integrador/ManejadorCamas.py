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
        __ArregloCamas[int(files[0])-1] = UnaCama
        

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

def DarDeAlta(Nombre, Alta):
    CamaDeALta = getCamaNombre(Nombre)
    
    ListaMedicamentos = ManejadorMedicamentos.getListaDeMedicamentos()
    TotalAdeudado = 0
    if(CamaDeALta != None):
        IdDecama = CamaDeALta.getIdCama()
        CamaDeALta.ActualizarAlta(Alta)
        
        print("Paciente: {}          Cama:{}    Habitacion:{}".format(CamaDeALta.getNombre(),CamaDeALta.getIdCama(),CamaDeALta.getHabitacion()))
        print("Diagnostico: {}       Fecha De Internaion: {}".format(CamaDeALta.getDiagnostico(),CamaDeALta.getFechaDeInternacion()))
        print("Fecha de alta: " + CamaDeALta.getAlta())
        print("Medicamento/monodroga       Presentacion         Cantidad       Precio")
        for i in range(len(ListaMedicamentos)):
            if ListaMedicamentos[i].getIdcama() == IdDecama:
                print("{}/{}        {}             {}         {}".format(ListaMedicamentos[i].getNombreComercial(),ListaMedicamentos[i].getMonodroga(),ListaMedicamentos[i].getPresentacion(),ListaMedicamentos[i].getCantidad(),ListaMedicamentos[i].getPrecio()))
                TotalAdeudado += ListaMedicamentos[i].getPrecio() * ListaMedicamentos[i].getCantidad()
        print("Total adeudado:                                 {}".format(TotalAdeudado))
    else:
        print("cama no encontrada")

def ListarDiagnostico(Diagnostico):
    for i in range(len(__ArregloCamas)):
        
        if (__ArregloCamas[i].getEstado() == True) and (__ArregloCamas[i].getDiagnostico() == Diagnostico):
            print(__ArregloCamas[i])