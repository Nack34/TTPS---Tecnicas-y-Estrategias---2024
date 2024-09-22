#from src.auxiliar.decoradores import procesar_entradas_hasta_EOF
#from src.auxiliar.ayudaMemoria import leer_entrada

#Time Limit Exceed

from collections import deque
import heapq

def leer_entrada():
    entrada = input().strip()  # lee una línea de entrada
    
    if not entrada:
        raise EOFError # Si se introduce una línea vacía, lanzamos EOFError
    if entrada == "EOF":
        raise EOFError  # Si se introduce "EOF", lanzamos EOFError
    
    # Convertir la entrada en una lista de enteros
    secuencia = list(map(int, entrada.split()))

    return secuencia

def procesar_entradas_hasta_EOF(func):
    def wrapper():
        try:
            while True:
                func()
        except EOFError: # Para simular un EOF en sistemas Windows: Presiona Ctrl + Z seguido de Enter.
            pass

    return wrapper


def print_res(can_be_pila, can_be_cola, can_be_cola_prioridad):
    cant_posibilidades = can_be_pila*1 + can_be_cola*1 + can_be_cola_prioridad*1

    if (cant_posibilidades == 0): print("impossible") 
    elif (cant_posibilidades > 1): print("not sure")
    else: 
        if (can_be_pila): print("stack") 
        elif (can_be_cola): print("queue") 
        elif (can_be_cola_prioridad): print("priority queue") 

@procesar_entradas_hasta_EOF
def res():
    pila = []
    can_be_pila = True
    cola = deque()
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
                heapq.heappush(cola_prioridad, -elem)
        else:
            if (can_be_pila): 
                tendria_que_ser = pila.pop()
                can_be_pila = (elem == tendria_que_ser)  
            if (can_be_cola): 
                tendria_que_ser = cola.popleft()
                can_be_cola = (elem == tendria_que_ser)  
            if (can_be_cola_prioridad): 
                tendria_que_ser = -heapq.heappop(cola_prioridad)
                can_be_cola_prioridad = (elem == tendria_que_ser)  

    print_res(can_be_pila, can_be_cola, can_be_cola_prioridad)



res()
