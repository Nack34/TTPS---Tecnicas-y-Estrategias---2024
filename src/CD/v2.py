# Time Limit Exceeded ??????

def leer_entrada(split_by = " ", eof_string= "EOF"):
    entrada = input().strip()  # lee una línea de entrada
    
    if not entrada:
        raise EOFError # Si se introduce una línea vacía, lanzamos EOFError
    if entrada == eof_string:
        raise EOFError  # Si se introduce eof_string, lanzamos EOFError

    return entrada

def res():
    cant_coincidencias = 0

    entrada = leer_entrada(eof_string= "0 0")
    
    # Convertir la entrada en una lista de enteros
    cant_cds = list(map(int, entrada.split(" ")))

    cds_jack = {}

    for i in range(cant_cds[0]):
        elem = int(leer_entrada())
        cds_jack[elem]=True

    for i in range(cant_cds[1]):
        elem = int(leer_entrada())
        try:
            cant_coincidencias += cds_jack[elem]
        except KeyError:
            pass


    print(cant_coincidencias)
    resol.append(cant_coincidencias)

resol = []

try:
    while True:
        res()
except EOFError: 
    pass

print(resol)