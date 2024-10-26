import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from collections import deque


class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, node_colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node_colors[node[0]] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def generate_colors(n):
    cmap = plt.get_cmap("viridis")
    colors = [mcolors.rgb2hex(cmap(i / n)[:3]) for i in range(n)]
    return colors


def bfs(root):
    queue = deque([root])
    visited = []
    while queue:
        node = queue.popleft()
        if node:
            visited.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return visited


def dfs(root):
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        if node:
            visited.append(node)
            stack.append(node.right)
            stack.append(node.left)
    return visited


def visualize_traversal(root, traversal_func):
    nodes = traversal_func(root)
    colors = generate_colors(len(nodes))
    node_colors = {node.id: colors[i] for i, node in enumerate(nodes)}
    draw_tree(root, node_colors)


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

print("Візуалізація обходу в ширину:")
visualize_traversal(root, bfs)

print("Візуалізація обходу в глибину:")
visualize_traversal(root, dfs)
