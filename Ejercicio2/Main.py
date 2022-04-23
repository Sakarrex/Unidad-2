from ModuloViajeroFrecuente import ViajeroFrecuente

def test():
    objetoPrueba = ViajeroFrecuente(23,"736423","Sebastian","Garcia",8352.4)
    print('Prueba:{}'.format(objetoPrueba.muestra()))

if __name__ == "__main__":
    test()