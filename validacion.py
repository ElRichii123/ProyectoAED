import time

import principal


def formato(fecha):
    for format in ["%Y/%m/%d"]:
        try:
            rdo = time.strptime(fecha, format)
            return True
        except:
            pass
    return False


def fechas(m):
    f = input("Ingrese fecha " + m + " (aaaa/mm/dd) : ")
    while format(f) == False:
        print("ERROR--> (formato distinto de aaaa/mm/dd)")
        f = input("Ingrese nuevamente la fecha: ")
    return f


def no_repetido(v, x):
    n = len(v)
    izq, der = 0, n - 1
    while izq <= der:
        mitad = (izq + der) // 2
        if v[mitad].codigo == x:
            return True
        elif x < v[mitad].codigo:
            der = mitad - 1
        else:
            izq = mitad + 1
    return False


def rangos():
    rmin = int(input("Ingrese el menor precio que desea gastar: "))
    rmax = int(input("Ingrese el mayor precio que desea gastar: "))
    while rmin < 0 or rmax < 0:
        print("ERROR--> Ingrese rangos mayores o iguales a 0")
        rmin = int(input("Ingrese el menor precio que desea gastar: "))
        rmax = int(input("Ingrese el mayor precio que desea gastar: "))
    return rmin, rmax


def codigo(v):
    codigo = int(input("Ingrese el Codigo: "))
    pos = principal.buscar(v, codigo)
    while pos == -1:
        codigo = int(input("ERROR---> Ese codigo no existe :(, ingrese otro: "))
        pos = principal.buscar(v, codigo)
    return codigo, pos


def cantdad(v, pos):
    if v[pos].cant_dispo == 0:
        print("No hay mas articulos disponible :(")
        return
    cant = int(input("Ingrese la cantidad que desea comprar: "))
    while cant > v[pos].cant_dispo:
        cant = int(input("ERROR---> No hay tanta cantidad de arituclos, ingrese otra mas pequeña: "))
    return cant


def envio():
    envio = input("Ingrese la forma de envio a DOMICILIO (1) o RETIRAR EN SUCURSAL (2): ")
    while envio != "1" and envio != "2":
        envio = input("ERROR---> Debe elegir entre ENVIO A DOMICILIO(1) o RETIRAR EN SUCURSAL(2): ")
    return envio
