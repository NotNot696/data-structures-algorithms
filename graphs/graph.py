"""
Graph Implementation (Unweighted)
"""

from collections import deque


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list[v1]:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)

    def remove_vertex(self, v):
        if v not in self.adj_list:
            return
        for neighbor in self.adj_list[v]:
            self.adj_list[neighbor].remove(v)
        del self.adj_list[v]

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []

        while queue:
            vertex = queue.popleft()
            result.append(vertex)

            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    def dfs_recursive(self, start):
        visited = set()
        result = []

        def _dfs(vertex):
            visited.add(vertex)
            result.append(vertex)
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(start)
        return result

    def has_cycle(self):
        visited = set()

        def _has_cycle(vertex, parent):
            visited.add(vertex)

            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    if _has_cycle(neighbor, vertex):
                        return True
                elif neighbor != parent:
                    return True

            return False

        for vertex in self.adj_list:
            if vertex not in visited:
                if _has_cycle(vertex, None):
                    return True

        return False

    def __str__(self):
        result = ""
        for v, neighbors in self.adj_list.items():
            result += f"{v}: {neighbors}\n"
        return result


def main():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(4, 5)

    print(g)
    print("BFS from 1:", g.bfs(1))
    print("DFS from 1:", g.dfs_recursive(1))
    print("Has cycle:", g.has_cycle())


if __name__ == "__main__":
    main()