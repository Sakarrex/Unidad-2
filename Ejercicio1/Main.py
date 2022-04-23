from csv import reader
import csv
from ModuloEmail import Email

if __name__ == "__main__":

    
    print("Ingresar switch")
    switch = input()
    if(switch == '1'): 
        print("Ingresar nombre")
        nombre = input()

        print("Ingresar identificador de la cuenta")
        identificador = input()
    
        print("Ingresar dominio")
        dominio = input()

        print("Ingresar tipo de dominio")
        tipoDeDominio = input()

        print("Ingresar Contraseña")
        contraseña=input()

        unCorreo = Email(identificador,dominio,tipoDeDominio,contraseña)
        
        print("Estimado/a", nombre,"te enviaremos tus mensajes a la dirección ", unCorreo.retornaEmail())

    if(switch == '2'):
        print("Ingresar contraseña previa")
    
        if(input()== unCorreo.getContraseña()):
            print("Contraseña correcta, ingresar nueva contraseña")
            unCorreo.setContraseña(input())
            print ("Contraseña actual:" + unCorreo.getContraseña())
        else:
            print("Contraseña incorrecta")

    if(switch == '3'):
        print("Ingresar correo a crear")
        nuevoCorreo = Email()
        nuevoCorreo.crearCuenta(input())

        print("Correo:",nuevoCorreo.retornaEmail(), "contraseña:", nuevoCorreo.getContraseña())

    if(switch == '4'):
        listaEmails = []
        archivo = open("c:\\Users\\Usuario\\Desktop\\POO\\Unidad 2\\Ejercicio1\\Correos.csv")
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            listaEmails.append(Email(fila[0],fila[1],fila[2],fila[3]))
        archivo.close    
        print("Ingresar correo a buscar")
        bandera = False
        correoBuscar = input()
        for correoActual in listaEmails:
            
            if(correoActual.getId() == correoBuscar):
                bandera = True
        if(bandera == True):
            print("Correo encontrado")
        else:
            print("Correo no encontrado")        
