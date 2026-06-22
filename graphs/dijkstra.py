"""
Dijkstra's Algorithm
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

    def dijkstra(self, start):
        distances = {v: float('inf') for v in self.adj_list}
        distances[start] = 0
        pq = [(0, start)]
        previous = {v: None for v in self.adj_list}

        while pq:
            current_dist, current = heapq.heappop(pq)

            if current_dist > distances[current]:
                continue

            for neighbor, weight in self.adj_list[current].items():
                new_distance = current_dist + weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current
                    heapq.heappush(pq, (new_distance, neighbor))

        return distances, previous

    def get_path(self, previous, start, end):
        path = []
        current = end

        while current is not None:
            path.append(current)
            current = previous[current]

        path.reverse()

        if path and path[0] == start:
            return path
        return []


def main():
    g = WeightedGraph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 1)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 3)

    dist, prev = g.dijkstra('A')
    print("Distances:", dist)
    print("Path A to D:", g.get_path(prev, 'A', 'D'))


if __name__ == "__main__":
    main()