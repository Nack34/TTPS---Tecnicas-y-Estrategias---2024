from ayudaMemoria import leer_entrada

# Decorador que procesa entradas hasta EOF
def procesar_entradas_hasta_EOF(func):
    def wrapper():
        try:
            while True:
                func()
        except EOFError: # Para simular un EOF en sistemas Windows: Presiona Ctrl + Z seguido de Enter.
            pass

    return wrapper

# Función que será decorada
@procesar_entradas_hasta_EOF
def res():    
    print(leer_entrada())

# Llamada a la función decorada
#res() 
