def gcd(u, v):
    """Calcula el máximo común divisor (MCD) de u y v usando el algoritmo de Euclides iterativo."""
    while v:
        u, v = v, u % v  # Actualizamos u y v
    return abs(u)  # Devolvemos el valor absoluto del MCD

def last_nonzero_digit_of_lcm(n):
    def last_nonzero_digit_modulo(x):
        while x % 10 == 0:
            x //= 10
        return x 

    last_digit = 1
    for i in range(1, n + 1):
        # Calculamos el LCM iterativo considerando solo el último dígito distinto de cero
        last_digit = (last_digit * i // gcd(last_digit, i))
        last_digit = last_nonzero_digit_modulo(last_digit)
        #print(last_nonzero_digit_modulo(last_digit) % 10)
        print(last_digit)
    return last_nonzero_digit_modulo(last_digit) % 10 #last_digit % 10

# Lectura de entrada
import sys
input_lines = sys.stdin.read().strip().split("\n")
results = []

for line in input_lines:
    n = int(line)
    if n == 0:
        break
    results.append(last_nonzero_digit_of_lcm(n))

# Salida de resultados
#print("\n".join(map(str, results)))
