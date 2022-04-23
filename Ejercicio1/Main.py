from csv import reader
import csv
from ModuloEmail import Email

def test():
    correoPrueba = Email("alumnopoo","gmail","com","abc")
    print("CorreoPrueba: {},{}".format(correoPrueba.retornaEmail(),correoPrueba.getContraseña()))

if __name__ == "__main__":

    test()
    switch = int(input("Ingresar switch "))
    while switch != 0 :
        
        if(switch == 1): 
        
            nombre = input("Ingresar nombre ")

            
            identificador = input("Ingresar identificador de la cuenta ")
        
            
            dominio = input("Ingresar dominio ")

        
            tipoDeDominio = input("Ingresar tipo de dominio ")

            
            contraseña=input("Ingresar Contraseña")

            unCorreo = Email(identificador,dominio,tipoDeDominio,contraseña)
            
            print("Estimado/a", nombre,"te enviaremos tus mensajes a la dirección ", unCorreo.retornaEmail())

        if(switch == 2):
            
        
            if(input("Ingresar contraseña previa")== unCorreo.getContraseña()):
                unCorreo.setContraseña(input("Contraseña correcta, ingresar nueva contraseña"))
                print ("Contraseña actual:" + unCorreo.getContraseña())
            else:
                print("Contraseña incorrecta")

        if(switch == 3):
            print("Ingresar correo a crear")
            nuevoCorreo = Email()
            nuevoCorreo.crearCuenta(input())

            print("Correo:",nuevoCorreo.retornaEmail(), "contraseña:", nuevoCorreo.getContraseña())

        if(switch == 4):
            i=0
            listaEmails = []
            archivo = open("c:\\Users\\Usuario\\Desktop\\POO\\Unidad-2\\Ejercicio1\\Correos.csv")
            reader = csv.reader(archivo, delimiter=',')
            for fila in reader:
                listaEmails.append(Email(fila[0],fila[1],fila[2],fila[3]))
            archivo.close    
            
            bandera = False
            correoBuscar = input("Ingresar correo a buscar ")
            while i < len(listaEmails) and bandera == False:
                
                if(listaEmails[i].getId() == correoBuscar):
                    bandera = True
                i+=1
            if(bandera == True):
                print("Correo encontrado")
            else:
                print("Correo no encontrado")
        switch = int(input("Ingresar switch "))
  
                
