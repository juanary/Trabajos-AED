def validar_identificador(identificador):
    identificador = identificador.strip()
    if identificador == "":
        return False

    solo_guiones = True
    for c in identificador:
        if not (('A' <= c <= 'Z') or ('0' <= c <= '9') or c == '-'):
            return False
        if c != '-':
            solo_guiones = False

    return not solo_guiones

def calcular_monto_base(moneda, monto_nominal, algoritmo):
    if algoritmo == 1 and moneda == "ARS":
        comision = monto_nominal * 0.09
        return monto_nominal - comision
    elif algoritmo == 2 and moneda == "USD":
        if monto_nominal < 50000:
            comision = 0
        elif monto_nominal < 80000:
            comision = monto_nominal * 0.05
        else:
            comision = monto_nominal * 0.078
        return monto_nominal - comision
    elif algoritmo == 3 and (moneda == "EUR" or moneda == "GBP"):
        comision = 100
        if monto_nominal > 25000:
            comision += monto_nominal * 0.06
        return monto_nominal - comision
    elif algoritmo == 4 and moneda == "JPN":
        comision = 500 if monto_nominal <= 100000 else 1000
        return monto_nominal - comision
    elif algoritmo == 5 and moneda == "ARS":
        if monto_nominal < 500000:
            comision = 0
        else:
            comision = monto_nominal * 0.07
            if comision > 50000:
                comision = 50000
        return monto_nominal - comision
    return monto_nominal

def calcular_monto_final(monto_base, algoritmo):
    if algoritmo == 1:
        if monto_base <= 300000:
            impuesto = 0
        else:
            excedente = monto_base - 300000
            impuesto = excedente * 0.25
        return monto_base - impuesto
    elif algoritmo == 2:
        impuesto = 50 if monto_base < 50000 else 100
        return monto_base - impuesto
    elif algoritmo == 3:
        return monto_base - (monto_base * 0.03)
    return monto_base

def principal():
    with open("ordenes25.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    datos = lineas[1:]

    cant_minvalida = 0
    cant_binvalido = 0
    cant_oper_validas = 0
    suma_mf_validas = 0

    cant_ARS = cant_USD = cant_EUR = cant_GBP = cant_JPY = 0

    mayor_diferencia = -1
    cod_my = ""
    mont_nom_my = 0
    mont_fin_my = 0

    nom_primer_benef = datos[0][0:20].strip()
    cant_nom_primer_benef = 0

    total_ordenes = 0
    total_invalidas = 0
    suma_mf_ARS = 0
    cant_validas_ARS = 0

    for linea in datos:
        total_ordenes += 1

        nombre = linea[0:20].strip()
        identificador = linea[20:30].strip()
        codigo = linea[30:40].strip()
        monto_nominal = int(linea[40:50].strip())
        alg_com = int(linea[50:52].strip())
        alg_imp = int(linea[52:54].strip())

        moneda = "INVALIDA"
        if "ARS" in codigo:
            moneda = "ARS"
            cant_ARS += 1
        if "USD" in codigo:
            if moneda != "INVALIDA":
                moneda = "MULTIPLE"
            else:
                moneda = "USD"
                cant_USD += 1
        if "EUR" in codigo:
            if moneda != "INVALIDA":
                moneda = "MULTIPLE"
            else:
                moneda = "EUR"
                cant_EUR += 1
        if "GBP" in codigo:
            if moneda != "INVALIDA":
                moneda = "MULTIPLE"
            else:
                moneda = "GBP"
                cant_GBP += 1
        if "JPN" in codigo:
            if moneda != "INVALIDA":
                moneda = "MULTIPLE"
            else:
                moneda = "JPN"
                cant_JPY += 1

        if nombre == nom_primer_benef:
            cant_nom_primer_benef += 1

        if moneda == "INVALIDA" or moneda == "MULTIPLE":
            cant_minvalida += 1
            total_invalidas += 1
            continue

        if not validar_identificador(identificador):
            cant_binvalido += 1
            total_invalidas += 1

        if validar_identificador(identificador):
            monto_base = calcular_monto_base(moneda, monto_nominal, alg_com)
            monto_final = calcular_monto_final(monto_base, alg_imp)
            cant_oper_validas += 1
            suma_mf_validas += round(monto_final, 2)

            if moneda == "ARS":
                suma_mf_ARS += round(monto_final, 2)
                cant_validas_ARS += 1
        else:
            monto_base = calcular_monto_base(moneda, monto_nominal, alg_com)
            monto_final = calcular_monto_final(monto_base, alg_imp)

        diferencia = monto_nominal - monto_final
        if diferencia > mayor_diferencia:
            mayor_diferencia = diferencia
            cod_my = codigo
            mont_nom_my = monto_nominal
            mont_fin_my = round(monto_final, 2)

    porcentaje = (total_invalidas * 100) // total_ordenes
    promedio = (suma_mf_ARS // cant_validas_ARS) if cant_validas_ARS else 0

    print(' (r1) - Cantidad de ordenes invalidas - moneda no autorizada:', cant_minvalida)
    print(' (r2) - Cantidad de ordenes invalidas - beneficiario mal identificado:', cant_binvalido)
    print(' (r3) - Cantidad de operaciones validas:', cant_oper_validas)
    print(' (r4) - Suma de montos finales de operaciones validas:', round(suma_mf_validas, 2))
    print(' (r5) - Cantidad de ordenes para moneda ARS:', cant_ARS)
    print(' (r6) - Cantidad de ordenes para moneda USD:', cant_USD)
    print(' (r7) - Cantidad de ordenes para moneda EUR:', cant_EUR)
    print(' (r8) - Cantidad de ordenes para moneda GBP:', cant_GBP)
    print(' (r9) - Cantidad de ordenes para moneda JPN:', cant_JPY)
    print('(r10) - Codigo de la orden de pago con mayor diferencia  nominal - final:', cod_my)
    print('(r11) - Monto nominal de esa misma orden:', mont_nom_my)
    print('(r12) - Monto final de esa misma orden:', mont_fin_my)
    print('(r13) - Nombre del primer beneficiario del archivo:', nom_primer_benef)
    print('(r14) - Cantidad de veces que apareció ese mismo nombre:', cant_nom_primer_benef)
    print('(r15) - Porcentaje de operaciones inválidas sobre el total:', porcentaje)
    print('(r16) - Monto final promedio de las ordenes validas en moneda ARS:', promedio)

if __name__ == "__main__":
    principal()
