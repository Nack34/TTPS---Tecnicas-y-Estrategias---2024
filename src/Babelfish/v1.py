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

values = {}


def add_element_to_dictionary():
    entrada = leer_entrada()
    values[entrada[1]] = entrada[0]


def res():
    print(values.get(leer_entrada()[0], 'eh'))

try:
    while True:
        add_element_to_dictionary()
except EOFError: # Para simular un EOF en sistemas Windows: Presiona Ctrl + Z seguido de Enter.
    pass


try:
    while True:
        res()
except EOFError: # Para simular un EOF en sistemas Windows: Presiona Ctrl + Z seguido de Enter.
    pass