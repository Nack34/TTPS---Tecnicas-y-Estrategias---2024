#

def solve_cd_problem():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        
        jack_cds = set()
        for _ in range(n):
            jack_cds.add(int(input()))
        
        common_cds = 0
        for _ in range(m):
            if int(input()) in jack_cds:
                common_cds += 1
        
        print(common_cds)

# Ejecutar la solución
solve_cd_problem()