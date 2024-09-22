# Accepted

def leer_entrada(split_by = " ", eof_string= "EOF"):
    entrada = input().strip()  # lee una línea de entrada
    
    if not entrada:
        raise EOFError # Si se introduce una línea vacía, lanzamos EOFError
    if entrada == eof_string:
        raise EOFError  # Si se introduce eof_string, lanzamos EOFError
    
    # Convertir la entrada en una lista de enteros
    secuencia = list(map(str, entrada.split(split_by)))

    return secuencia

values = {
    'W': 1,
    'H': 1/2,
    'Q': 1/4,
    'E': 1/8,
    'S': 1/16,
    'T': 1/32,
    'X': 1/64
}

def is_measure_correct(measure):
    sum = 0
    for note in list(measure):
        sum += values[note]
    return sum == 1

def res():
    cant_correctos = 0

    measures = leer_entrada(split_by = "/", eof_string= "*")
    measures.pop()
    measures.pop(0)

    for measure in measures:
        cant_correctos+=is_measure_correct(measure)

    print(cant_correctos)

try:
    while True:
        res()
except EOFError: # Para simular un EOF en sistemas Windows: Presiona Ctrl + Z seguido de Enter.
    pass

