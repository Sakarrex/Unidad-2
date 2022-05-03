
from ModuloConjunto import Conjunto

if __name__ == "__main__":
    conjunto1 = Conjunto()
    conjunto2 = Conjunto()

    for i in range(int(input("tamaño conjunto 1 : "))):
        x = int(input("Ingresar valor conjunto 1: "))
        conjunto1.agregarValor(x)
    
    print(conjunto1.getConjunto())

    for j in range(int(input("tamaño conjunto 2: "))):
        conjunto2.agregarValor(int(input("Ingresar valor conjunto 2: ")))

    print(conjunto2.getConjunto())
    
    unionConjunto = conjunto1 + conjunto2

    print("conjunto union: {}".format(unionConjunto))

    unionDiferencia = conjunto1 - conjunto2

    print("Conjunto diferencia {}".format(unionDiferencia))
    
    if(conjunto1 == conjunto2):
        print("Son iguales")
    else:
        print("Son distintos")
   
#
# Conjunto 1 = {1,3,2,5,6,7}
# Conjunto 2 = {2,5,6,7,8}