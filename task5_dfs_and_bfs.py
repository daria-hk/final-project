import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import numpy as np

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, value_map, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)   # Використання id та збереження значення вузла
        value_map[node.id] = node # Збереження значення в карті значень
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, value_map, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, value_map, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    value_map = {}
    tree = add_edges(tree, tree_root, pos, value_map)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()
    return value_map, tree, pos

def update_color_and_draw_tree(tree, pos, value_map, visited):
    colors = [value_map[node].color for node in tree.nodes()]
    labels = {node: value_map[node].val for node in tree.nodes()}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def dfs_recursive(graph, vertex, value_map, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    color = list(np.random.choice(range(1, 20), size=3))
    norm_color = [x / 100.0 for x in color]
    value_map[vertex].color = norm_color # колір вузла
    update_color_and_draw_tree(graph, pos, value_map, visited) # Відвідуємо вершину міняючи колір
    print(value_map[vertex].val, end=' ')  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, value_map, visited)

def bfs_recursive(graph, queue, value_map, visited=None):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        visited = set()
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    # Перевіряємо, чи відвідували раніше дану вершину
    if vertex not in visited:
        # Якщо не відвідували, друкуємо вершину
        color = list(np.random.choice(range(1, 256), size=3))
        norm_color = [x / 255.0 for x in color]
        value_map[vertex].color = norm_color # колір вузла # колір вузла
        update_color_and_draw_tree(graph, pos, value_map, visited) # Відвідуємо вершину міняючи колір 
        print(value_map[vertex].val, end=" ") 
        # Додаємо вершину до множини відвіданих вершин.
        visited.add(vertex)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги.
        queue.extend(set(graph[vertex]) - visited)
    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    bfs_recursive(graph, queue, value_map, visited)

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

value_map, tree, pos = draw_tree(root)

# dfs на графіку
dfs_recursive(tree, root.id, value_map)

print("\n")

# bfs на графіку
bfs_recursive(tree, deque([root.id]), value_map)
