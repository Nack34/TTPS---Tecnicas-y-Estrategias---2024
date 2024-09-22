#Accepted (el error es que no habia chequeado que las listas esten con elementos antes de sacar algo, creo)

def leer_entrada():
    entrada = input().strip()  # lee una línea de entrada
    
    if not entrada:
        raise EOFError # Si se introduce una línea vacía, lanzamos EOFError
    if entrada == "EOF":
        raise EOFError  # Si se introduce "EOF", lanzamos EOFError
    
    # Convertir la entrada en una lista de enteros
    secuencia = list(map(int, entrada.split()))

    return secuencia

def print_res(can_be_pila, can_be_cola, can_be_cola_prioridad):
    cant_posibilidades = can_be_pila*1 + can_be_cola*1 + can_be_cola_prioridad*1

    if (cant_posibilidades == 0): return "impossible" 
    elif (cant_posibilidades > 1): return "not sure"
    else: 
        if (can_be_pila): return "stack" 
        elif (can_be_cola): return "queue" 
        elif (can_be_cola_prioridad): 
            return "priority queue"

def res():
    pila = []
    can_be_pila = True
    cola = []
    can_be_cola = True
    cola_prioridad = []
    can_be_cola_prioridad = True

    cant_inputs = leer_entrada()

    for i in range(cant_inputs[0]):
        input = leer_entrada()
        accion = input[0]
        elem = input[1]
        if (accion == 1):
            if (can_be_pila): 
                pila.append(elem)
            if (can_be_cola): 
                cola.append(elem)
            if (can_be_cola_prioridad): 
                cola_prioridad.append(elem)
        else:
            if (can_be_pila):
                if len(pila) > 0: 
                    tendria_que_ser = pila.pop()
                    can_be_pila = (elem == tendria_que_ser)  
                else:
                    can_be_pila = False
            if (can_be_cola): 
                if len(cola) > 0: 
                    tendria_que_ser = cola.pop(0)
                    can_be_cola = (elem == tendria_que_ser)  
                else:
                    can_be_cola = False
            if (can_be_cola_prioridad): 
                if len(cola_prioridad) > 0: 
                    cola_prioridad.sort(reverse=True)
                    tendria_que_ser = cola_prioridad.pop(0)
                    can_be_cola_prioridad = (elem == tendria_que_ser)  
                else:
                    can_be_cola_prioridad = False

    to_print = print_res(can_be_pila, can_be_cola, can_be_cola_prioridad)
    print(to_print)

try:
    while True:
        res()
except EOFError: # Para simular un EOF en sistemas Windows: Presiona Ctrl + Z seguido de Enter.
    pass

