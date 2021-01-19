inp = []
n = int(input())
for i in range(n):
    inp.append(input())

mat = [[int(j) for j in i.split()] for i in inp]
visited = [0]*n
cycle_count = 0

def dfs(v):
    visited[v] = 1
    for i in range(n):
        if mat[v][i] == 1:
            if not visited[i]:
                if dfs(i):
                    return True
            elif visited[i] == 1:
                return True
    visited[v] = 2
    return False

for i in range(n):
    if (not visited[i]):
        if dfs(i):
            print(1)
            exit()
print(0)
        # cycle_count += 1
# print(cycle_count)
