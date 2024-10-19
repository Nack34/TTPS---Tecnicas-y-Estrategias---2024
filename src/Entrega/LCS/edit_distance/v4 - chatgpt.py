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
                memo[i][j] = min(memo[i - 1][j - 1] + cost_replace,  
                                 memo[i - 1][j] + cost_delete,       
                                 memo[i][j - 1] + cost_insert)      
    return memo[-1][-1]

input_data = stdin.read().splitlines()

T = int(input_data[0])
results = []

for i in range(1, 2 * T, 2):
    A = input_data[i]
    B = input_data[i + 1]
    results.append(str(edit_distance(A, B)))

stdout.write("\n".join(results) + "\n")
