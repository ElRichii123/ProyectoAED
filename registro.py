import random
import time


class Compra():
    def __init__(self, codigo, cant, precio, envio, monto, fecha):
        self.codigo = codigo
        self.cant = cant
        self.precio = precio
        self.envio = envio
        self.monto = monto
        self.fecha = fecha


class Publicacion():
    def __init__(self, codigo, precio, ubicacion, estado, cant_dispo, puntuacion):
        self.codigo = codigo
        self.precio = precio
        self.ubicacion = ubicacion
        self.estado = estado
        self.cant_dispo = cant_dispo
        self.puntuacion = puntuacion


def convertir_compra(articulo, cant, monto, envio):
    codigo = articulo.codigo
    precio = articulo.precio
    fecha = time.strftime("%Y/%m/%d")
    compra = Compra(codigo, cant, precio, envio, monto, fecha)
    return compra


def puntuar(p):
    puntuar = (" ", "Mala", "Regular", "Buena", "Muy Buena", "Excelente")
    return puntuar[p]


def ubicar(u, c=None):
    ubicar = (
        "", "Buenos Aires", "Catamarca", "Chaco", "Chubut", "Cordoba", "Corrientes", "Entre Rios", "Formosa", "Jujuy",
        "La Pampa", "La Rioja", "Mendoza", "Misiones", "Neuquen", "Rio Negro", "Salta", "San Juan", "San Luis",
        "Santa Cruz", "Santa Fe", "Santiago del Estero", "Tierra del Fuego", "Tucuman")
    if u == 0:
        for i in range(len(ubicar)):
            if ubicar[i] == c:
                return i
    else:
        return ubicar[u]


def not_empty(v):
    if len(v) != 0:
        return True
    else:
        print("El arreglo esta vacio :(")
        return False


def to_string(art):
    r = ''
    r += '{:<25}'.format('Codigo: ' + str(art.codigo))
    r += '{:<20}'.format('Precio: $' + str(art.precio))
    r += '{:<20}'.format('Estado: ' + art.estado)
    r += '{:<30}'.format('Cantidad disponible: ' + str(art.cant_dispo))
    r += '{:<30}'.format('Puntuacion: ' + str(puntuar(art.puntuacion)))
    r += '{:<30}'.format('Ubicacion: ' + str(ubicar(art.ubicacion)))
    return r


def mostrar_lista(v):
    for i in v:
        print(to_string(i))


def add_in_order(articulo, v):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        mitad = (izq + der) // 2
        if articulo.codigo == v[mitad].codigo:
            pos = mitad
            break

        if articulo.codigo < v[mitad].codigo:
            der = mitad - 1
        else:
            izq = mitad + 1

    if izq > der:
        pos = izq
    v[pos:pos] = [articulo]


def cargar_datos():
    n = int(input("Ingrese cantidad de articulos: "))
    v = []
    for i in range(n):
        codigo = random.randint(100, 2000)
        precio = random.randint(1000, 5000)
        ubicacion = random.randint(1, 23)
        estado = random.choice(("nuevo", "usado"))
        cant_dispo = random.randint(1, 100)
        puntacion = random.randint(1, 5)
        articulo = Publicacion(codigo, precio, ubicacion, estado, cant_dispo, puntacion)
        add_in_order(articulo, v)
    return v


def to_str(cpra):
    r = "*" * 20
    r += '{:<25}'.format("\nCodigo: #" + str(cpra.codigo) + "-" + str(cpra.fecha))
    r += '{:<25}'.format("\nResumen de compra")
    r += '{:<25}'.format("\nProducto: $" + str(cpra.monto) + "(" + str(cpra.precio) + "*" + str(cpra.cant) + ")")
    if cpra.envio == "1":
        porc = (cpra.precio * cpra.cant) * 10 // 100
        total = cpra.monto + porc
        r += '{:<25}'.format("\nCargo del envio: $" + str(porc))
        r += '{:<25}'.format("\nTu pago: $" + str(total))
    else:
        r += '{:<25}'.format("\nCargo del envio: " + "$0 (eligio retirar en sucursal)")
        r += '{:<25}'.format("\nTu pago: $" + str(cpra.precio * cpra.cant))
    return r
