import sys
def gcd(u, v):
    while (v): 
        t = u; 
        u = v; 
        v = t % v; 

    return -u if u < 0 else u

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        N, M, K = data[i].split()
        N = int(N)
        M = int(M)
        K = int(K)
        results.append(gcd(N, M))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
