
from ModuloConjunto import Conjunto

if __name__ == "__main__":
    conjunto1 = Conjunto(4)
    conjunto2 = Conjunto(5)

    for i in range(conjunto1.getTamano()):
        print("tamaño: {}".format(conjunto1.getlen()))
        conjunto1.agregarValor(int(input("Ingresar valor conjunto 1: ")))
    
    for j in range(conjunto2.getTamano()):
        print("tamaño: {}".format(conjunto2.getlen()))
        conjunto2.agregarValor(int(input("Ingresar valor conjunto 2: ")))

    unionConjunto = conjunto1+conjunto2

    for i in range(len(unionConjunto)):
        print(unionConjunto[i])

# Conjunto 1 = {1,2,5,6}
# Conjunto 2 = {2,5,6,7,8}