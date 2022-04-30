
from asyncio.windows_events import NULL
from csv import reader
import csv
from ModuloRegistro import Registro

def test():
    Registroprueba = Registro(10,20,5)
    print(Registroprueba)

if __name__ == "__main__":
    
    test()

    __RegistroMes = []
    cantidadDias=2
    for i in range(cantidadDias):
       
        __RegistroMes.append([])
    archivo = open("c:\\Users\\Usuario\\Desktop\\POO\\Unidad-2\\Ejercicio3\\Registro.csv")
    reader = csv.reader(archivo, delimiter = ",")
    for files in reader:
        x= (int(files[0]))-1
        __RegistroHora=(Registro(int(files[2]),int(files[3]),int(files[4])))
        __RegistroMes[x].append(__RegistroHora)
    archivo.close


    print("Seleccionar opcion: \n 1: Para cada variable el día y hora de menor y mayor valor. \n 2: temperatura promedio mensual por cada hora. \n 3: Listado de valores para un día dado")
    switch = int(input())
    while switch != 4:
        if switch == 1:
            for variable in range(1,4):
                print("variable:{}".format(variable))
                mayorDia=1
                menorDia=1   
                mayorHora=0
                menorHora=0
                mayor = int(__RegistroMes[0][0].getVariable(variable))
                menor = int(__RegistroMes[0][0].getVariable(variable))
                for i in range(len(__RegistroMes)):
                    for j in range(len(__RegistroMes[i])):
                        if __RegistroMes[i][j].getVariable(variable) > mayor:
                            mayor = __RegistroMes[i][j].getVariable(variable)
                            mayorDia = i+1
                            mayorHora = j
                        if __RegistroMes[i][j].getVariable(variable) < menor:
                            menor = __RegistroMes[i][j].getVariable(variable)
                            menorDia = i+1
                            menorHora = j
                print("Menor Variable {}: {}, dia: {}, hora: {}".format(variable,menor,menorDia,menorHora))
                print("Mayor Variable {}: {}, dia: {}, hora: {}".format(variable,mayor,mayorDia,mayorHora))
        elif switch == 2:
            
            for i in range(len(__RegistroMes[0])):
                promedio = 0.0
                for j in range(len(__RegistroMes)):
                    promedio += __RegistroMes[j][i].getTemperatura()
                print("Promedio de temperatura mensual hora {}: {}".format(i,promedio/len(__RegistroMes)))        
        elif switch == 3:
            dia = int(input("indicar numero de dia: "))
            print ("    Hora       Temperatura       Humedad       Presion")
            for i in range(len(__RegistroMes[dia-1])):
                print("    {}           {}                  {}            {}".format(i,__RegistroMes[dia-1][i].getTemperatura(),__RegistroMes[dia-1][i].getHumedad(),__RegistroMes[dia-1][i].getPresion()))
        else:
            print("Opcion invalida")
        switch = int(input("Seleccionar opcion: \n 1:Para cada variable el día y hora de menor y mayor valor. \n 2: temperatura promedio mensual por cada hora. \n 3: Listado de valores para un día dado"))
    