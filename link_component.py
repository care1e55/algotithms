from collections import deque

n, m = input().split()
graph = [[] for i in range(int(n))]
for _ in range(int(m)):
    a, b = input().split()
    graph[int(a)-1].append(int(b)-1)
    graph[int(b)-1].append(int(a)-1)

def find_components(graph):
    visited = [False]*(int(n)+1)
    components = []
    for i in range(1,int(n)+1):
        if not visited[i]:
            visited[i] = True
            component = []
            queue = deque([i])
            while queue:
                vertex = queue.popleft()
                component.append(vertex)
                for neighbor in graph[vertex-1]:
                    if not visited[neighbor+1]:
                        visited[neighbor+1] = True
                        queue.append(neighbor+1)
            components.append(component)
    return components

components = find_components(graph)

print(len(components))
for c in components:
    print(len(c))
    print(*c)