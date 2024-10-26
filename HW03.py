import heapq


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = {}

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node][to_node] = weight
        self.edges[to_node][from_node] = weight  # Для неорієнтованого графа


def dijkstra(graph, start):
    heap = []
    heapq.heappush(heap, (0, start))
    distances = {node: float("infinity") for node in graph.nodes}
    distances[start] = 0
    shortest_path = {}

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.edges[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
                shortest_path[neighbor] = current_node

    return distances, shortest_path

# Створення графа
graph = Graph()
nodes = ["A", "B", "C", "D", "E"]
for node in nodes:
    graph.add_node(node)

graph.add_edge("A", "B", 1)
graph.add_edge("A", "C", 4)
graph.add_edge("B", "C", 2)
graph.add_edge("B", "D", 5)
graph.add_edge("C", "D", 1)
graph.add_edge("C", "E", 3)
graph.add_edge("D", "E", 3)

# Виконання алгоритму Дейкстри
start_node = "A"
distances, paths = dijkstra(graph, start_node)

# Виведення результатів
print("Distances from {}: {}".format(start_node, distances))
print("Shortest paths: {}".format(paths))
