# función para determinar si un caracter es un digito.
def es_digito(car):
    return "0" <= car <= "9"


# función para determinar si un caracter es una vocal.
def es_vocal(car):
    return car in "aeiouáéíóúAEIOUÁÉÍÓÚ"


# función para cacular el promedio entero entre sus parámetros.
def calcular_promedio(acumulador, contador):
    promedio = 0
    if contador > 0:
        promedio = acumulador // contador
    return promedio


# función principal del programa.
def principal():
    # inicialización de variables de resultados..
    r1 = r3 = r4 = 0
    r2 = None

    # contador de letras en una palabra...
    cl = 0

    # item 1: flag para x en segunda...
    sx2 = False

    # item 3: flag para dígito, acumulador de longitudes y contador de palabras...
    sd = False
    ac = cp = 0

    # item 4: flags para t y te...
    st = ste = False

    # apertura del archivo de entrada, lectura del texto a procesar y cierre del archivo...
    m = open("entrada.txt")
    texto = m.read()
    m.close()

    # texto = "En este tejado no se atienen a las normas."

    # ciclo general de procesamiento...
    for car in texto:
        # chequeo de final de palabra...
        if car in " .":
            # corte de palabra...
            # procesar solo si la palabra tenía al menos un caracter...
            if cl > 0:
                # item 1...
                if sx2:
                    r1 += 1

                # item 2...
                if r2 is None or cl > r2:
                    r2 = cl

                # item 3...
                if sd:
                    ac += cl
                    cp += 1

                # item 4...
                if ste:
                    r4 += 1

            # resetear variables para la siguiente palabra...
            # contador de letras...
            cl = 0

            # item 1...
            sx2 = False

            # item 3...
            sd = False

            # item 4...
            st = ste = False

        else:
            # caracter dentro de la palabra... contarlo...
            cl += 1

            # item 1...
            if car in "xX" and cl == 2:
                sx2 = True

            # item 3...
            if es_digito(car):
                sd = True

            # item 4...
            if car in "tT":
                st = True
            else:
                if st and car in "eéEÉ":
                    ste = True
                st = False

    # cálculo del promedio para r3...
    r3 = calcular_promedio(ac, cp)

    # visualizacion de los resultados pedidos...
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


# script principal.
if __name__ == "__main__":
    principal()
