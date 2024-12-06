from math import gcd

def solve_case(N, M, K):
    factor = (2**K - 2)
    for x in range(1, N):
        a = x
        b = N - x
        if gcd(a, b) == 1:
            calculated_M = a**2 + b**2 - factor * a * b
            if calculated_M == M:
                return gcd(N, M)
    return 1  # Default return if no valid pair is found (edge cases)

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])  # Number of test cases
    results = []
    for i in range(1, T + 1):
        N, M, K = data[i].split()
        N = int(N)
        M = int(M)
        K = int(K)
        results.append(solve_case(N, M, K))
    
    # Print all results
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()
