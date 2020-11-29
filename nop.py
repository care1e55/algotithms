def NOP(n,m, N, M):
    F = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if N[i - 1] == M[j - 1]:
                F[i][j] = F[i - 1][j - 1] + 1
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    print(F[n][m])


n = int(input())
N = input().split()
m = int(input())
M = input().split()
NOP(n,m, N, M)