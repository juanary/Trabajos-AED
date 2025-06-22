# función para determinar si un caracter es un digito.
def es_digito(car):
    return "0" <= car <= "9"


# función para determinar si un caracter es una vocal.
def es_vocal(car):
    return car in "aeiouáéíóúAEIOUÁÉÍÓÚ"


# función para determinar si un caracter es una consonante...
def es_consonante(car):
    return car.lower() in "bcdfghjklmnñpqrstvwxyz"


# función para calcular el promedio entero entre sus parámetros...
def calcular_promedio(a, c):
    promedio = 0
    if c > 0:
        promedio = a // c
    return promedio


# función principal del programa.
def principal():
    # inicialización de variables de resultados..
    r1 = r3 = r4 = 0
    r2 = None

    # contador de letras en una palabra...
    cl = 0

    # item 1: variable para el caracter anterior y contador de mayusculas...
    ant, cm = " ", 0

    # item 2: flag de inclusión de digito impar...
    sdi = False

    # item 3: acumuladores, contadores y flags para r3...
    acr3, cpr3, sev, cc = 0, 0, False, 0

    # item 4: flags para b, ba y t...
    sb, sba, st = False, False, False

    # apertura del archivo de entrada, lectura del texto a procesar y cierre del archivo...
    m = open("entrada.txt")
    texto = m.read()
    m.close()

    # texto = "La fila f34 parece completa pero la columna C3 y el sector x4g5 no."
    # texto = "Parece que C3PO es mejor que R2D2 y Olivaw1."
    # texto = "Odiosas y enemistadas se atacaron afuera del campo."
    texto = "El ancho de bastos es banca y pasaba el Beagle y Santa Barbara."

    # ciclo general de procesamiento...
    for car in texto:
        # chequeo de final de palabra...
        if car in " .":
            # corte de palabra...
            # procesar solo si la palabra tenía al menos un caracter...
            if cl > 0:
                # item 1...
                if es_digito(ant) and cm == 0:
                    r1 += 1

                # item 2...
                if sdi:
                    if r2 is None or cl > r2:
                        r2 = cl

                # item 3...
                if cc >= 3 and sev:
                    cpr3 += 1
                    acr3 += cl

                # item 4...
                if sba and not st:
                    r4 += 1

            # resetear variables para la siguiente palabra...
            # contador de letras...
            cl = 0

            # item 1...
            ant, cm = " ", 0

            # item 2...
            sdi = False

            # item 3...
            sev, cc = False, 0

            # item 4...
            sb, sba, st = False, False, False

        else:
            # caracter dentro de la palabra... contarlo...
            cl += 1

            # item 1...
            if car.isupper():
                cm += 1
            ant = car

            # item 2...
            if es_digito(car) and int(car) % 2 == 1:
                sdi = True

            # item 3...
            if es_vocal(car) and cl == 1:
                sev = True
            elif es_consonante(car):
                cc += 1

            # item 4...
            if car in "bB":
                sb = True
            else:
                if sb and car in "aáAÁ":
                    sba = True
                sb = False

            if car in "tT":
                st = True

    # cálculo del porcentaje para r3...
    r3 = calcular_promedio(acr3, cpr3)

    # visualizacion de los resultados pedidos...
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


# script principal.
if __name__ == "__main__":
    principal()
