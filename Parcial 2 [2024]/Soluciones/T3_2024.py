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

    # item 1: flag de mayuscula y flag de digito en cuarta...
    scm, sd4 = False, False

    # item 2: flag de inclusión de "p" o de "n"...
    spn = False

    # item 3: acumuladores, contadores y flags para r3...
    acr3, cpr3, cdr3, svr3 = 0, 0, 0, False

    # item 4: flags para f, fa y comienzo en vocal...
    sf, sfa, scv = False, False, False

    # apertura del archivo de entrada, lectura del texto a procesar y cierre del archivo...
    m = open("entrada.txt")
    texto = m.read()
    m.close()

    # texto = "El civ6 es mejor que el Civ5 y el FIFA24 es mejor que el PES24."
    # texto = "Le pasan la pelota al genio."
    # texto = "Las rutas A2 y R1513 son las mas transitadas despues de las rutas Ead513 y TAfg814."
    # texto = "Las familias afamadas no conocen Antofagasta ni leen a Mafalda pero se afianzan."

    # ciclo general de procesamiento...
    for car in texto:
        # chequeo de final de palabra...
        if car in " .":
            # corte de palabra...
            # procesar solo si la palabra tenía al menos un caracter...
            if cl > 0:
                # item 1...
                if scm and sd4:
                    r1 += 1

                # item 2...
                if spn:
                    if r2 is None or cl > r2:
                        r2 = cl

                # item 3...
                if cdr3 >= 2 and svr3:
                    cpr3 += 1
                    acr3 += cl

                # item 4...
                if sfa and scv:
                    r4 += 1

            # resetear variables para la siguiente palabra...
            # contador de letras...
            cl = 0

            # item 1...
            scm, sd4 = False, False

            # item 2...
            spn = False

            # item 3...
            cdr3, svr3 = 0, False

            # item 4...
            sf, sfa, scv = False, False, False

        else:
            # caracter dentro de la palabra... contarlo...
            cl += 1

            # item 1...
            if car.isupper() and cl == 1:
                scm = True
            elif es_digito(car) and cl == 4:
                sd4 = True

            # item 2...
            if car in "pPnN":
                spn = True

            # item 3...
            if es_digito(car):
                cdr3 += 1
            elif es_vocal(car):
                svr3 = True

            # item 4...
            if car in "fF":
                sf = True
            else:
                if sf and car in "aáAÁ":
                    sfa = True
                sf = False

            if es_vocal(car) and cl == 1:
                scv = True

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
