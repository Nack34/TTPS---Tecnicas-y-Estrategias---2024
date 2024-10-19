#Accepted
def lis(seq):
    n = len(seq)
    DP = [1] * n 
    prev = [-1] * n 

    ans = 0  
    for i in range(n):
        for j in range(i):
            if seq[j] < seq[i] and DP[i] < DP[j] + 1:
                DP[i] = DP[j] + 1
                prev[i] = j
        if DP[ans] < DP[i]:
            ans = i

    return max(DP)

N = int(input()) 
A = list(map(int, input().split())) 

print(lis(A))
