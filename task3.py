import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Функція для знаходження найкоротшого шляху за алгоритмом Дейкстри
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, edge_data in graph[current_node].items():
            weight = edge_data['weight']
            distance = current_distance + weight['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

# Створення графа з вагами ребер
G_weighted = nx.Graph()
G_weighted.add_nodes_from([1, 2, 3, 4])
G_weighted.add_weighted_edges_from([(1, 2, {'weight': 1}), (2, 3, {'weight': 2}), (3, 4, {'weight': 3}), (4, 1, {'weight': 4})])

# Застосування алгоритму Дейкстри
start_node = 1  # Початкова вершина
shortest_paths = dijkstra(G_weighted, start_node)

# Виведення результатів
print("Найкоротші шляхи від вершини", start_node)
for node, distance in shortest_paths.items():
    print("Вершина:", node, "Найкоротший шлях:", distance)

# Візуалізація графа без ваг ребер
nx.draw(G_weighted, with_labels=True, node_size=700, node_color="skyblue", font_size=12, font_weight="bold", font_color="black", pos=nx.circular_layout(G_weighted))
plt.title("Graph Visualization")
plt.show()
