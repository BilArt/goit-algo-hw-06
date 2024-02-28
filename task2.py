import networkx as nx
import matplotlib.pyplot as plt

# DFS
def dfs(graph, start, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    visited.add(start)
    path.append(start)
    for next_node in graph[start]:
        if next_node not in visited:
            dfs(graph, next_node, visited, path)
    return path

# BFS
def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    path = []
    while queue:
        node = queue.pop(0)
        path.append(node)
        for next_node in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)
    return path

# Створення графа
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Здійснення порівняння
start_node = 1  # Початкова вершина для обох алгоритмів

dfs_path = dfs(G, start_node)
bfs_path = bfs(G, start_node)

print("Шлях, знайдений за допомогою DFS:", dfs_path)
print("Шлях, знайдений за допомогою BFS:", bfs_path)

# Порівняння результатів
if dfs_path == bfs_path:
    print("Шляхи, знайдені DFS та BFS, однакові.")
else:
    print("Шляхи, знайдені DFS та BFS, різні.")

# Пояснення різниці в отриманих шляхах можна надати у README файлі.
