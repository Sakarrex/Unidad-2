from csv import reader
import csv
from ModuloViajeroFrecuente import ViajeroFrecuente

def test():
    objetoPrueba = ViajeroFrecuente(23,"736423","Sebastian","Garcia",8352.4)
    print('Prueba:{}'.format(objetoPrueba.muestra()))

if __name__ == "__main__":
    test()
    ListaViajeros = []
    archivo = open("c:\\Users\\Usuario\\Desktop\\POO\\Unidad-2\\Ejercicio2\\Viajeros.csv")
    reader = csv.reader(archivo, delimiter = ",")
    for lines in reader:
        ListaViajeros.append(ViajeroFrecuente(int(lines[0]),lines[1],lines[2],lines[3],int(lines[4])))
    archivo.close

    numeroDeViajero = int(input("Ingresar viajero a buscar: "))
    i = 0
    bandera = False
    while i < len(ListaViajeros) and bandera == False:
        if(numeroDeViajero == ListaViajeros[i].getNumeroViajero()):
            bandera = True
        i+=1
    
    if bandera == False:
        print("Viajero no encontrado")
    else:
  
        ViajeroActual = ListaViajeros[i-1]
        print("Viajero: {}".format(ViajeroActual.muestra()))
        print("Ingresar opción: \n a: Consultar cantidad de millas \n b: Acumular millas \n c: Canjear Millas \n d: Finalizar")
        switch = input()
        while switch != 'd':
            if switch == 'a':
                print("Cantidad de millas: {}".format(ViajeroActual.cantidadTotaldeMillas()))
            elif switch == 'b':
                ViajeroActual.acumularMillas(int(input("Ingrese canitdad de millas a acumular: ")))
                print("sale")
            elif switch == 'c':
                ViajeroActual.canjearMillas(int(input("Ingrese canitdad de millas a canjear")))
            else:
                print("Codigo incorrecto")
            print("Ingresar opción: \n a: Consultar cantidad de millas \n b: Acumular millas \n c: Canjear Millas \n d: Finalizar")
            switch = input()

    print("Drirección de memoria ListaViajeros: {}".format(hex(id(ListaViajeros))))
    j = 0
    for j in range(len(ListaViajeros)):
        print("Dirección de memoria ListaViajeros {}: {}".format(j,hex(id(ListaViajeros[j]))))
