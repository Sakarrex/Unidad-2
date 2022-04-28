import csv



from ModuloViajeroFrecuente6 import ViajeroFrecuente

if __name__ == "__main__":
    ListaMayorMillasAcumuladas = []
    ListaViajeros = []
    archivo = open("c:\\Users\\Usuario\\Desktop\\POO\\Unidad-2\\Ejercicio2\\Viajeros.csv")
    reader = csv.reader(archivo, delimiter = ",")
    for lines in reader:
        ListaViajeros.append(ViajeroFrecuente(int(lines[0]),lines[1],lines[2],lines[3],int(lines[4])))
    archivo.close

    max =  ListaViajeros[0].cantidadTotaldeMillas()

    for i in range(len(ListaViajeros)):
        if(ListaViajeros[i].cantidadTotaldeMillas() > max):
            max = ListaViajeros[i].cantidadTotaldeMillas()
    
    print('max = {}'.format(max))

    for i in range(len(ListaViajeros)):
        if(ListaViajeros[i].cantidadTotaldeMillas() == max):
            ListaMayorMillasAcumuladas.append(ListaViajeros[i])
           
    print("Millas viajero {}: {}".format(ListaViajeros[0].getNumeroViajero(),ListaViajeros[0].cantidadTotaldeMillas()))

    ListaViajeros[0] + 100
    
    print("Millas viajero {}: {}".format(ListaViajeros[0].getNumeroViajero(),ListaViajeros[0].cantidadTotaldeMillas()))

    ListaViajeros[0] - 100

    print("Millas viajero {}: {}".format(ListaViajeros[0].getNumeroViajero(),ListaViajeros[0].cantidadTotaldeMillas()))