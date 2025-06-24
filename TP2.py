import os

def moneda_incorrecta(linea):
    ars_flag = False
    usd_flag = False
    eur_flag = False
    gbp_flag = False
    jpy_flag = False
    if "ARS" in linea:
        ars_flag = True
    if "USD" in linea:
        usd_flag = True
    if "EUR" in linea:
        eur_flag = True
    if "GBP" in linea:
        gbp_flag = True
    if "JPY" in linea:
        jpy_flag = True
    # Condición de no repetición de código en la orden
    if ars_flag and (usd_flag or eur_flag or gbp_flag or jpy_flag):
        return False
    elif usd_flag and (eur_flag or gbp_flag or jpy_flag):
        return False
    elif eur_flag and (gbp_flag or jpy_flag):
        return False
    elif gbp_flag and jpy_flag:
        return False
    #Condicion de existencia del código en la orden
    if ars_flag or usd_flag or eur_flag or gbp_flag or jpy_flag:
        return True
    else:
        return False

def identificacion_destinatario(intervalo, indice=0):
    limite = len(intervalo)

    if indice >= limite:
        return True  # Caso base: todos los caracteres fueron válidos

    letra = intervalo[indice]
    if letra in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789-_":
        return identificacion_destinatario(intervalo, indice + 1)
    else:
        return False

def ident_destinatario_combinacion(intervalo):
    if (((intervalo.isupper() or intervalo.isdigit()) and ("-" in intervalo or "_" in intervalo)) or
            intervalo.isupper() or intervalo.isdigit()):
        return True
    else:
        return False

def principal():
    nombre_archivo = "ordenes.txt"
    if not os.path.exists(nombre_archivo):
        return None
    m = open(nombre_archivo,"rt")
    linea = m.readline()
    timestamp = linea[0:41]

    #Punto 1
    r1 = 0
    r2 = 0
    
    for linea in m:
        destinatario = linea[0:19].strip()
        identificacion = linea[20:29].strip()
        orden_de_pago = linea[30:39].strip()
        monto_nominal = int(linea[40:49].strip())
        identificacion_comision = int(linea[50:51].strip())
        identificacion_impositivo = int(linea[52:53].strip())
        print(destinatario)
        #Punto 1
        #r1 --> contador de Monedas no autorizadas
        #r2 --> contador de destinatarios mal identificados
        #variables: orden_de_pago, identificacion.

        if (not moneda_incorrecta(orden_de_pago) and not identificacion_destinatario(identificacion) and
                not ident_destinatario_combinacion(identificacion)):
            r1 += 1
        if not identificacion_destinatario(identificacion) and not ident_destinatario_combinacion(identificacion):
            r2 += 1
        #Punto 2 La cantidad de operaciones válidas (r3), y la suma (redondeada  a dos decimales)  de  todos los 
        #montos finales de estas operaciones válidas (r4). 
        #r3 y r4 se inicializan en 0
        
        #r3--> contador de operaciones válidas
        #r4--> suma de todos los montos finales de estas operaciones válidas(redondeado a dos decimales)

if __name__ == "__main__":
    principal()