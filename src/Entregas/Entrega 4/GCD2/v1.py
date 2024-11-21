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
    
    n = int(data[0])
    results = []
    
    for i in range(1, n + 1):
        a, b = data[i].split()
        a = int(a)
        b = int(b)
        res = gcd(a, b)
        results.append(str(gcd(a, res)))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
