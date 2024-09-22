
def leer_entrada():
    entrada = input().strip()  # lee una línea de entrada
    
    if not entrada:
        raise EOFError # Si se introduce una línea vacía, lanzamos EOFError
    if entrada == "EOF":
        raise EOFError  # Si se introduce "EOF", lanzamos EOFError
    
    # Convertir la entrada en una lista de enteros
    secuencia = list(map(int, entrada.split()))

    return secuencia

##############################################

def for_normal():
    numeros = [1, 2, 3, 4, 5]

    # Bucle for normal
    for numero in numeros:
        print(numero)


##############################################


def pila_normal():

    # Declaración de la pila
    pila = []

    # Agregar elementos (push)
    pila.append(10)
    pila.append(20)
    pila.append(30)

    # Remover y devolver el último elemento (pop)
    elemento = pila.pop()  # Devuelve 30
    print(elemento)  # Salida: 30


##############################################

def deque_normal():

    from collections import deque

    # Declaración de la cola
    cola = deque()

    # Agregar elementos (enqueue)
    cola.append(10)
    cola.append(20)
    cola.append(30)

    # Remover y devolver el primer elemento (dequeue)
    elemento = cola.popleft()  # Devuelve 10
    print(elemento)  # Salida: 10



##############################################

def cola_prioridad_descendente():

    import heapq

    # Declaración de la cola de prioridad (max-heap)
    cola_prioridad = []

    # Agregar elementos
    heapq.heappush(cola_prioridad, -10)  # Se almacena como -10
    heapq.heappush(cola_prioridad, -20)  # Se almacena como -20
    heapq.heappush(cola_prioridad, -30)  # Se almacena como -30

    # Remover y devolver el mayor elemento (convertimos el valor negativo a positivo)
    elemento = -heapq.heappop(cola_prioridad)  # Devuelve 30
    print(elemento)  # Salida: 30



##############################################

def no_se_muestra_input():
    import getpass

    def obtener_entrada_oculta():
        return getpass.getpass("")

    def mostrar_salida(mensaje):
        print(mensaje)

    # Ejemplo de uso
    entrada = obtener_entrada_oculta()  # Llama a la función para obtener la entrada sin mostrarla
    mostrar_salida("La entrada ha sido registrada.")  # Mensaje de salida
    mostrar_salida(entrada)  # Mensaje de salida


##############################################


def tomar_tiempo(function):
    
    import time
    input() #meter un enter para empezar a tomar el tiempo

    # Medir el tiempo de ejecución
    start_time = time.time()  # Guardar el tiempo de inicio

    function()

    end_time = time.time()    # Guardar el tiempo de finalización

    # Calcular el tiempo en milisegundos
    execution_time = (end_time - start_time) * 1000  # Convertir a ms
    print(f"La función x() tardó {execution_time:.2f} ms en ejecutarse.")