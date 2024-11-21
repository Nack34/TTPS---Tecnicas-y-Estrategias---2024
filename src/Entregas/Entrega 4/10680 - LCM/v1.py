#EL ALGORITMO NO TIENE SENTIDO

from math import gcd

def last_nonzero_digit_of_lcm(n):
    def last_nonzero_digit_modulo(x):
        while x % 10 == 0:
            x //= 10
        return x % 10

    last_digit = 1
    for i in range(1, n + 1):
        # Calculamos el LCM iterativo considerando solo el último dígito distinto de cero
        last_digit = (last_digit * i // gcd(last_digit, i)) % 10
        last_digit = last_nonzero_digit_modulo(last_digit)
    return last_digit

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
print("\n".join(map(str, results)))
