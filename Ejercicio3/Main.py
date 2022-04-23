
from csv import reader
import csv
from ModuloRegistro import Registro

if __name__ == "__main__":
    RegistroDia = []
    archivo = open("c:\\Users\\Usuario\\Desktop\\POO\\Unidad-2\\Ejercicio3\\Registro.csv")
    reader = csv.reader(archivo, delimiter = ",")
    for files in reader:
        RegistroDia.append( int(files[0]) , RegistroHora = [int(files[1]) , Registro(int(files[2]) , int(files[3]) , int(files[4]) )])
    archivo.close

    for i in RegistroDia:
        print("Dia: {} Hora: {} Temperatura: {} Humedad: {} Presion: {}".format(RegistroDia[0],RegistroDia[1][0],RegistroDia[1][1].getTemperatura,RegistroDia[1][1].getHumedad,RegistroDia[1][1].getPresion))