from collections import deque, defaultdict

n, m = input().split()
edges_list = [list(map(int, input().split())) for i in range(int(m))]

graph = defaultdict(list)
for i in range(1, int(n)+1):
    graph[i] = list(map(lambda j: list(filter(lambda v: v != i, j))[0], filter(lambda j: i in j, edges_list)))

def find_components(graph):
    visited = set()
    components = set()
    for i in range(1,int(n)+1):
        if i not in visited:
            visited.add(i)
            component = set()
            queue = deque([i])
            while queue:
                vertex = queue.popleft()
                component.add(vertex)
                for neighbor in graph[vertex]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            components.add(frozenset(component))
    return components

components = find_components(graph)

print(len(components))
for c in components:
    print(len(c))
    print(*c)