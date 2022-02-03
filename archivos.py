import pickle
import os.path
import principal
import registro
import io

FD, nfavs = "miscompras.dat", "favoritos.dat"


def crear_txt(compra):
    file = open("miscompras.txt", "w+t")
    compra_str = registro.to_str(compra)
    file.write(compra_str)
    file.seek(0, io.SEEK_SET)
    for linea in file.readlines():
        print(linea)
    file.close()


def agregar(compra):
    file = open(FD, "ab")
    pickle.dump(compra, file)
    file.close()
    crear_txt(compra)


def intervalo(fmin, fmax):
    file = open(FD, "rb")
    size = os.path.getsize(FD)
    while file.tell() < size:
        compra = pickle.load(file)
        if fmin <= str(compra.fecha) <= fmax:
            print(registro.to_str(compra))
    file.close()


def mostrar_archivo(name):
    file = open(name, "rb")
    size = os.path.getsize(name)
    while file.tell() < size:
        i = pickle.load(file)
        print(registro.to_string(i))
    file.close()


def agregar_fav(fav):
    file = open(nfavs, "ab")
    pickle.dump(fav, file)
    file.close()


def repetidos(fav):
    if os.path.exists(nfavs):
        file = open(nfavs, "rb")
        size = os.path.getsize(nfavs)
        file.seek(0, io.SEEK_SET)
        while file.tell() < size:
            fav_archivo = pickle.load(file)
            if fav.codigo == fav_archivo.codigo:
                file.close()
                return False
        file.close()
    return True


