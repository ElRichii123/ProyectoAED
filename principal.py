import registro
import archivos
import validacion


def buscar(v,x):
    n = len(v)
    izq, der = 0, n-1
    pos = -1
    while izq <= der:
        mitad = (izq + der) // 2
        if x == v[mitad].codigo:
            pos = mitad
            return pos
        elif x < v[mitad].codigo:
            der = mitad - 1
        else:
            izq = mitad + 1
    return pos


def comprar(v):
    codigo, pos = validacion.codigo(v)
    cant = validacion.cantdad(v, pos)
    if cant == None:
        return
    v[pos].cant_dispo -= cant

    envio = validacion.envio()
    monto = cant * v[pos].precio
    compra = registro.convertir_compra(v[pos], cant, monto, envio)
    archivos.agregar(compra)


def intervalos():
    print("------Intervalo de Fechas----------")
    finical = validacion.fechas("INICIAL")
    ffinal = validacion.fechas("FINAL")
    archivos.intervalo(finical, ffinal)


def rango(v):
    min, max = v[0], v[0]
    for i in v:
        if i.precio < min.precio:
            min = i
        if i.precio > max.precio:
            max = i
    print("EL menor precio de las publicacions es: $", min.precio,"EL mayor precio es: $",max.precio)
    rmin, rmax = validacion.rangos()
    print("-->Publicaciones con esos precios<--")
    for i in v:
        if rmin <= i.precio <= rmax:
            print(registro.to_string(i))


def agregar_fav(v, favs):
    print("-->Agregar un favorito<--")
    codigo, pos = validacion.codigo(v)
    if not validacion.no_repetido(favs,codigo):
        registro.add_in_order(v[pos],favs)
        return favs
    else:
        print("Ese articulo ya esta en tu lista de favoritos :)")
        return favs



def actualizar(favs):
    for fav in favs:
        if archivos.repetidos(fav):
            archivos.agregar_fav(fav)
    archivos.mostrar_archivo("favoritos.dat")


def main():
    print("-"*10,"BIENVENIDO","-"*10)
    op = -1
    v, favs = [], []
    while op != 0:
        print("-" * 50)
        print("Opcion 1: Cargar datos ")
        print("Opcion 2: Comprar ")
        print("Opcion 3: Mis Compras")
        print("Opcion 4: Rango de precios")
        print("Opcion 5: Agregar favorito")
        print("Opcion 6: Actualizar favoritos")
        print("Opcion 0 : SALIR ")
        op = int(input("Ingrese la opcion: "))
        print("-" * 50)
        if op == 1:
            v = registro.cargar_datos()
            registro.mostrar_lista(v)

        elif op == 2:
            if registro.not_empty(v):
                comprar(v)

        elif op == 3:
            if registro.not_empty(v):
                intervalos()

        elif op == 4:
            if registro.not_empty(v):
                rango(v)

        elif op == 5:
            if registro.not_empty(v):
                favs = agregar_fav(v, favs)
                registro.mostrar_lista(favs)

        elif op == 6:
            if registro.not_empty(favs):
                actualizar(favs)

        elif op == 0:
            print("Muchas gracias""\tVuelva Pronto")
            break

if __name__ == '__main__':
    main()
