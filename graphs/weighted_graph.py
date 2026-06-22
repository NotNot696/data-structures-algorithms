"""
Weighted Graph Implementation
"""


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

    def __str__(self):
        result = ""
        for v, neighbors in self.adj_list.items():
            result += f"{v}: {neighbors}\n"
        return result


def main():
    g = WeightedGraph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 1)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 3)

    print(g)


if __name__ == "__main__":
    main()