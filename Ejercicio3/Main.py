
from csv import reader
import csv
from ModuloRegistro import Registro

if __name__ == "__main__":
    
    __RegistroDia = []
    archivo = open("c:\\Users\\Usuario\\Desktop\\POO\\Unidad-2\\Ejercicio3\\Registro.csv")
    reader = csv.reader(archivo, delimiter = ",")
    for files in reader:
        __RegistroHora = [int(files[1]),Registro(int(files[2]) , int(files[3]) , int(files[4]) )]
        __RegistroDia.append(int(files[0]))
        __RegistroDia.append(__RegistroHora)
    archivo.close

    i= 0

    for i in range(len(__RegistroDia)):
        print("Dia{}".format(__RegistroDia[i]))
        ##print("Dia: {} Hora: {} Temperatura: {} Humedad: {} Presion: {}".format(__RegistroDia[0],__RegistroDia[1][0],__RegistroDia[1][1].getTemperatura,__RegistroDia[1][1].getHumedad,__RegistroDia[1][1].getPresion))
        ##