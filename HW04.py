import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    # Node представляє вузол дерева з унікальним ідентифікатором, ключем (значенням) та кольором.
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    # Додає вузли та ребра до графа, рекурсивно обходячи дерево.
    # Використовує унікальні ідентифікатори для додавання вузлів до графа та їх позиціонування.
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла
        # Додаємо вуршину ліворуч
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        # Додаємо вуршину праворуч
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    # Створює граф
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    # додає вузли та ребра
    tree = add_edges(tree, tree_root, pos)

    # визначає кольори та мітки
    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }  # Використовуйте значення вузла для міток

    # візуалізує дерево
    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()

def build_heap(arr):
    n = len(arr)
    nodes = [Node(key=arr[i]) for i in range(n)]
    
    for i in range(n):
        if 2 * i + 1 < n:
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < n:
            nodes[i].right = nodes[2 * i + 2]

    return nodes[0] if nodes else None

# # Створення дерева
# root = Node(0)
# root.left = Node(4)
# root.left.left = Node(5)
# root.left.right = Node(10)
# root.right = Node(1)
# root.right.left = Node(3)

# Тестовий масив для побудови купи
arr = [3, 1, 6, 5, 2, 8, 7, 4]
root = build_heap(arr)

# Відображення дерева
draw_tree(root)
