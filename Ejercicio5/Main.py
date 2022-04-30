from csv import reader
import csv
from ModuloPlanAhorro import PlandeAhorro

def test():
    PlanDePrueba = PlandeAhorro(100,"Ford","Focus",100000)
    print(PlanDePrueba)

if __name__ == "__main__":

    test() 
    
    ListaPlanes = []
    valor = int
    archivo = open("c:\\Users\\Usuario\\Desktop\\POO\\Unidad-2\\Ejercicio5\\planes.csv")
    reader = csv.reader(archivo, delimiter = ";")
    for lines in reader:
        ListaPlanes.append(PlandeAhorro(lines[0],lines[1],lines[2],lines[3]))
    archivo.close

    print("Seleccione opción: \n a)Actualizar valor de vehiculo \n b)Vehiculos segun valor de cuotas \n c)Monto para licitar \n d) modificar cantidad de cuotas para licitar \n e) finalizar")
    switch=input()
    while switch != 'e':
        if switch == 'a':
            for i in range(len(ListaPlanes)):
                print("Codigo: {}, Modelo: {}, Versión: {}".format(ListaPlanes[i].getCodigo(),ListaPlanes[i].getModelo(),ListaPlanes[i].getVersion()))
                ListaPlanes[i].actualizarValor(int(input("Ingresar nuevo valor de vehiculo: ")))
        
        if switch == 'b':
            valor = int(input("ingresar valor"))
            for i in range(len(ListaPlanes)):
                if(ListaPlanes[i].valorDeCuota() < valor):
                    print("Codigo: {}, Modelo: {}, Versión: {}".format(ListaPlanes[i].getCodigo(),ListaPlanes[i].getModelo(),ListaPlanes[i].getVersion()))
        
        if switch == 'c':
            codigoVehiculo = int(input("Ingresar codigo de vehiculo: "))
            i = 0
            bandera = False
            while i < len(ListaPlanes) and bandera == False:
                if ListaPlanes[i].getCodigo() == codigoVehiculo:
                    bandera = True
                else:
                    i += 1
                
            if(bandera == True):
                print("Monto que se debe haber pagado para licitar el vehículo: {}".format(ListaPlanes[i].getCantidadCuotasLicitas()*ListaPlanes[i].valorDeCuota()))
            else: 
                print("Codigo no encontrado")
        if switch == 'd':
            codigoPlan = int(input("Ingresar codigo de plan: "))
            i = 0
            bandera = False
            while i < len(ListaPlanes) and bandera == False:
                if ListaPlanes[i].getCodigo() == codigoPlan:
                    bandera = True
                else:
                    i += 1
                
            if bandera == True:
                ListaPlanes[i].setCantidadCuotasLicitas(int(input("Ingresas nueva cantidad de cuotas licitas: ")))
                print("Nueva cantidad de cuotas licitas: {}".format(ListaPlanes[i].getCantidadCuotasLicitas()))
            else:
                print("Codigo no encontrado")
        
        print("Seleccione opción: \n a)Actualizar valor de vehiculo \n b)Vehiculos segun valor de cuotas \n c)Monto para licitar \n d) modificar cantidad de cuotas para licitar \n e) finalizar")
        switch=input()
