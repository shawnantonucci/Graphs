# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None

# def earliest_ancestor(self, n1, n2):
#     if self is None:
#         return None

#     if self.key == n1 or self.key == n2:
#         return self

#     left_ancestor = earliest_ancestor(self.left, n1, n2)
#     right_ancestor = earliest_ancestor(self.right, n1, n2)

#     if left_ancestor and right_ancestor:
#         return self

#     return left_ancestor if left_ancestor is not None else right_ancestor


# self = Node(1)
# self.left = Node(2)
# self.right = Node(3)
# self.left.left = Node(4)
# self.left.right = Node(5)
# self.right.left = Node(6)
# self.right.right = Node(7)

# print(earliest_ancestor(self, 4, 5).key)
# print(earliest_ancestor(self, 4, 6).key)
# print(earliest_ancestor(self, 3, 4).key)
# print(earliest_ancestor(self, 2, 4).key)

# Afterhours Solution
from collections import deque


class Stack():
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()

    def size(self):
        return len(self.stack)


def earliest_ancestor(ancestors, starting_node):
    graph = dict()
    for tpl in ancestors:
        if tpl[1] not in graph:
            graph[tpl[1]] = set()
        graph[tpl[1]].add(tpl[0])

    def dfs(starting_vertex):
        nonlocal graph
        if starting_vertex not in graph:
            return -1

        distances = dict()

        visited = set()
        stack = Stack()
        stack.push([starting_vertex])
        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]  # last element in the array storing the path
            if vertex not in visited:
                if vertex in graph:
                    for neighbor in graph[vertex]:
                        path_new = path[:]  # path.copy()
                        path_new.append(neighbor)
                        stack.push(path_new)
                        if neighbor not in graph:
                            distances[neighbor] = len(path_new)
                            continue
                    visited.add(vertex)
        results = []
        max_length = -1
        for k, v in distances.items():  # we find the max length
            if v > max_length:
                max_length = v

        for k, v in distances.items():
            if v == max_length:
                results.append(k)

        return min(results)

    return dfs(starting_node)
