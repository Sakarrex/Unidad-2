
import csv

from ModuloViajeroFrecuente7 import ViajeroFrecuente

if __name__ == "__main__":

    ListaViajeros = []
    archivo = open("c:\\Users\\Usuario\\Desktop\\POO\\Unidad-2\\Ejercicio2\\Viajeros.csv")
    reader = csv.reader(archivo, delimiter = ",")
    for lines in reader:
        ListaViajeros.append(ViajeroFrecuente(int(lines[0]),lines[1],lines[2],lines[3],int(lines[4])))
    archivo.close

    print(645 == ListaViajeros[0])
    print(ListaViajeros[0] == 100)

    print("Millas viajero {}: {}".format(ListaViajeros[0].getNumeroViajero(),ListaViajeros[0].cantidadTotaldeMillas()))

    100 + ListaViajeros[0]

    print("Millas viajero {}: {}".format(ListaViajeros[0].getNumeroViajero(),ListaViajeros[0].cantidadTotaldeMillas()))

    100 - ListaViajeros[0]
    
    print("Millas viajero {}: {}".format(ListaViajeros[0].getNumeroViajero(),ListaViajeros[0].cantidadTotaldeMillas()))

