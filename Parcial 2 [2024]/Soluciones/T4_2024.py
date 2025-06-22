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

    # item 1: contadores para r1...
    cd, cv, cc = 0, 0, 0

    # item 2: flag de inclusión de "s" o de "c"...
    ssc = False

    # item 3: contadores para r3...
    cp, cpr3, cdr3 = 0, 0, 0

    # item 4: flags para v, vi y n...
    sv, svi, sn = False, False, False

    # apertura del archivo de entrada, lectura del texto a procesar y cierre del archivo...
    m = open("entrada.txt")
    texto = m.read()
    m.close()

    # texto = "R23A es un robot similar a R2D2 y C256 pero muy distinto de U57E3."
    # texto = "Antes de anclar cae el ocaso."
    # texto = "Estamos en la zona X3 o en la T5."
    # texto = "Avieso el viernes envia su mensaje a AVEIT."

    # ciclo general de procesamiento...
    for car in texto:
        # chequeo de final de palabra...
        if car in " .":
            # corte de palabra...
            # procesar solo si la palabra tenía al menos un caracter...
            if cl > 0:
                # item 1...
                if cd > cv and cc == 1:
                    r1 += 1

                # item 2...
                if ssc:
                    if r2 is None or cl < r2:
                        r2 = cl

                # item 3...
                cp += 1
                if cdr3 == 0:
                    cpr3 += 1

                # item 4...
                if svi and sn:
                    r4 += 1

            # resetear variables para la siguiente palabra...
            # contador de letras...
            cl = 0

            # item 1...
            cd, cv, cc = 0, 0, 0

            # item 2...
            ssc = False

            # item 3...
            cdr3 = 0

            # item 4...
            sv, svi, sn = False, False, False

        else:
            # caracter dentro de la palabra... contarlo...
            cl += 1

            # item 1...
            if es_digito(car):
                cd += 1
            elif es_vocal(car):
                cv += 1
            elif es_consonante(car):
                cc += 1

            # item 2...
            if car in "sScC":
                ssc = True

            # item 3...
            if es_digito(car):
                cdr3 += 1

            # item 4...
            if car in "vV":
                sv = True
            else:
                if sv and car in "iíIÍ":
                    svi = True
                sv = False

            if car in "nN":
                sn = True

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
