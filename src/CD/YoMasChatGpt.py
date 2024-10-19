import sys

def leer_entrada(split_by=" "):
    entrada = sys.stdin.readline().strip()
    
    # Convertir la entrada en una lista de enteros
    secuencia = list(map(int, entrada.split(split_by)))
    
    return secuencia

def res():
    cant_coincidencias = 0

    # Leer las cantidades de CDs de Jack y Jill
    cant_cds = leer_entrada()

    # Si la entrada es "0 0", se termina el procesamiento
    if cant_cds == [0, 0]:
        return False

    cds_jack = {}

    # Leer los CDs de Jack
    for i in range(cant_cds[0]):
        elem = leer_entrada()[0]
        cds_jack[elem] = True

    # Comparar con los CDs de Jill
    for i in range(cant_cds[1]):
        elem = leer_entrada()[0]
        if elem in cds_jack:
            cant_coincidencias += 1

    # Escribir el resultado
    sys.stdout.write(str(cant_coincidencias) + "\n")
    return True

# Ciclo principal
while res():
    pass
