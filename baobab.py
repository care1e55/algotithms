inp = []
n = int(input())
for i in range(n):
    inp.append(input())

edge_num = 0
mat = [[int(j) for j in i.split()] for i in inp]
edge_num = sum([sum(i) for i in mat])//2

def dfs(v):
    visited[v] = True
    for i in range(n):
        if mat[v][i] == 1 and not visited[i]:
            dfs(i)

if (n - 1) != edge_num:
    print("NO")
else:
    visited = [False]*n
    dfs(0)
    if False not in visited:
        print('YES')
    else:
        print("NO")
