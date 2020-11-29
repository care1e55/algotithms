
graph = []
n_verteces, start, stop = input().split()
n_verteces = int(n_verteces)
start = int(start)-1
stop = int(stop)-1
for i in range(n_verteces):
    graph.append([int(j) for j in input().split()])

dist = [1e6] * n_verteces
dist[start] = 0
visited = [False] * n_verteces
prev = [-1] * n_verteces

def findmin(dist, visited): 
    cur_min = 1e6
    for v in range(n_verteces): 
        if dist[v] < cur_min and visited[v] == False: 
            cur_min = dist[v]
            min_index = v 
    return min_index 
   
def findpath(prev, j):
    if prev[j] == -1:
        result_path.append(j+1)
        return
    findpath(prev, prev[j])
    result_path.append(j+1)

if start == stop:
    print(start+1)
    exit()

try:
    for _ in range(n_verteces): 
        u = findmin(dist, visited)
        if u == stop:
            break
        visited[u] = True
        for v in range(n_verteces): 
            if graph[u][v] > 0 and visited[v] == False and dist[v] > dist[u] + graph[u][v]: 
                dist[v] = dist[u] + graph[u][v]
                prev[v] = u 

    result_path = []
    findpath(prev, stop)
    print(*result_path)
except:
    print(-1)