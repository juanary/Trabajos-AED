# función para determinar si un caracter es un digito.
def es_digito(car):
    return "0" <= car <= "9"


# función para determinar si un caracter es una vocal.
def es_vocal(car):
    return car in "aeiouáéíóúAEIOUÁÉÍÓÚ"


# función para determinar si un caracter es una consonante...
def es_consonante(car):
    return car.lower() in "bcdfghjklmnñpqrstvwxyz"


# función para calcular el porcentaje entero entre sus parámetros...
def calcular_porcentaje(cantidad, total):
    porcentaje = 0
    if total > 0:
        porcentaje = cantidad * 100 // total
    return porcentaje


# función principal del programa.
def principal():
    # inicialización de variables de resultados..
    r1 = r3 = r4 = 0
    r2 = None

    # contador de letras en una palabra...
    cl = 0

    # item 1: flag de consonante y flag de digito...
    sc34, sd = False, False

    # item 2: flag de inicio con "s"...
    ss = False

    # item 3: contadores para r3...
    cp, cpr3, cv = 0, 0, 0

    # item 4: flag para n y contador de silabas ni...
    sn, cni = False, 0

    # apertura del archivo de entrada, lectura del texto a procesar y cierre del archivo...
    m = open("entrada.txt")
    texto = m.read()
    m.close()

    # texto = "SALU4 o PAE3 son codigos malos en el mercado como salTA37."
    # texto = "Salen siempre temprano las aves del sol."
    # texto = "Andamos a los tumbos."
    # texto = "Ningun navio y ninguna ninfa es lindo ni feo en Ninive."

    # ciclo general de procesamiento...
    for car in texto:
        # chequeo de final de palabra...
        if car in " .":
            # corte de palabra...
            # procesar solo si la palabra tenía al menos un caracter...
            if cl > 0:
                # item 1...
                if sc34 and sd:
                    r1 += 1

                # item 2...
                if ss:
                    if r2 is None or cl < r2:
                        r2 = cl

                # item 3...
                # total de palabras del texto...
                cp += 1

                # cantidad de palabras con 2 o más vocales...
                if cv >= 2:
                    cpr3 += 1

                # item 4...
                if cni == 1:
                    r4 += 1

            # resetear variables para la siguiente palabra...
            # contador de letras...
            cl = 0

            # item 1...
            sc34, sd = False, False

            # item 2...
            ss = False

            # item 3...
            cv = 0

            # item 4...
            sn, cni = False, 0

        else:
            # caracter dentro de la palabra... contarlo...
            cl += 1

            # item 1...
            if es_consonante(car) and cl in (3, 4):
                sc34 = True
            elif es_digito(car):
                sd = True

            # item 2...
            if car in "sS" and cl == 1:
                ss = True

            # item 3...
            if es_vocal(car):
                cv += 1

            # item 4...
            if car in "nN":
                sn = True
            else:
                if sn and car in "iíIÍ":
                    cni += 1
                sn = False

    # cálculo del porcentaje para r3...
    r3 = calcular_porcentaje(cpr3, cp)

    # visualizacion de los resultados pedidos...
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


# script principal.
if __name__ == "__main__":
    principal()
