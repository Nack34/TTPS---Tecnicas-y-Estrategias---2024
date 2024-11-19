#time limit exceeded
from sys import stdin, stdout
def edit_distance(s, t, cost_delete=1, cost_insert=1, cost_replace=1):
    n = len(s) + 1 
    m = len(t) + 1 
    memo = [[0] * m for _ in range(n)]  

    for i in range(n):
        memo[i][0] = i * cost_delete 
    for j in range(m):
        memo[0][j] = j * cost_insert 

    for i in range(1, n):
        for j in range(1, m):
            if s[i - 1] == t[j - 1]:
                memo[i][j] = memo[i - 1][j - 1]  
            else:
                memo[i][j] = memo[i - 1][j - 1] + cost_replace  
                memo[i][j] = min(memo[i][j], memo[i - 1][j] + cost_delete)  
                memo[i][j] = min(memo[i][j], memo[i][j - 1] + cost_insert)  

    return memo[-1][-1]  

T = int(stdin.readline())  

for _ in range(T):
    A = stdin.readline().strip()  
    B = stdin.readline().strip() 
    
    stdout.write(str(edit_distance(A, B))+"\n")
