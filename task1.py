import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин та ребер до графа
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Візуалізація графа
nx.draw(G, with_labels=True)
plt.show()

# Аналіз основних характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
average_degree = sum(degree_sequence) / num_nodes

print("Кількість вершин:", num_nodes)
print("Кількість ребер:", num_edges)
print("Середня ступінь вершин:", average_degree)
