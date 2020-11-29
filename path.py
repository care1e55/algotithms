from collections import defaultdict, deque

inp = []
n = input()
for i in range(int(n)):
    inp.append(input())
start_stop = input()
start, stop = start_stop.split()
start = int(start)
stop = int(stop)


mat = [[int(j) for j in i.split()] for i in inp]
graph = defaultdict(list)

for i, v in enumerate(mat, 1):
    for j, u in enumerate(v, 1):
        if u == 1:
            graph[i].append(j)

def bfs(graph, start, stop):
    if start == stop:
        print(0)
        exit()
    visited = []
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        vertex = path[-1]
        if vertex not in visited:
            for neighbor in graph[vertex]:
                shortest_path = list(path)
                shortest_path.append(neighbor)
                queue.append(shortest_path)
                if neighbor == stop:
                    return shortest_path
            visited.append(vertex)
    return -1

result = bfs(graph, start, stop)
if result == -1:
    print(-1)
else:
    print(len(result)-1)
    print(*result)