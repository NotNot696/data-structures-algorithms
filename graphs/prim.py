"""
Prim's Algorithm (Minimum Spanning Tree)
"""

import heapq


class WeightedGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = {}

    def add_edge(self, v1, v2, weight):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.adj_list[v1][v2] = weight
        self.adj_list[v2][v1] = weight

    def prim(self, start):
        distances = {v: float('inf') for v in self.adj_list}
        distances[start] = 0
        pq = [(0, start)]
        previous = {v: None for v in self.adj_list}
        total_weight = 0

        while pq:
            current_dist, current = heapq.heappop(pq)

            if current_dist > distances[current]:
                continue

            total_weight += current_dist

            for neighbor, weight in self.adj_list[current].items():
                if weight < distances[neighbor]:
                    distances[neighbor] = weight
                    previous[neighbor] = current
                    heapq.heappush(pq, (weight, neighbor))

        return previous, total_weight


def main():
    g = WeightedGraph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 1)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 3)

    prev, total = g.prim('A')
    print("Total weight:", total)
    print("MST edges:")
    for v, p in prev.items():
        if p is not None:
            print(f"{p} → {v}")


if __name__ == "__main__":
    main()