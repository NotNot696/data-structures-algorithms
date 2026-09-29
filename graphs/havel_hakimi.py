"""
Havel-Hakimi Algorithm
-----------------------
Constructs a simple undirected graph from a degree sequence.

Time Complexity: O(n² log n)
Space Complexity: O(n²) for edges
"""


def havel_hakimi_graph(degrees: list):

    vertices = []
    for i, degree in enumerate(degrees):
        name = chr(ord("A") + i)
        vertices.append([degree, name])

    if sum(degrees) % 2 != 0:
        return None

    edges = []

    while vertices:
        vertices.sort(reverse=True)

        degree, vertex = vertices.pop(0)

        if degree == 0:
            return edges

    
        if degree > len(vertices):
            return None

        
        for i in range(degree):
            if vertices[i][0] <= 0:
                return None

            edges.append([vertex, vertices[i][1]])
            vertices[i][0] -= 1

    return edges


def main():
    """Test the Havel-Hakimi algorithm."""
    test_cases = [
        ([3, 3, 2, 2, 2], "Graphical"),
        ([3, 3, 2, 2, 1], "Not graphical (odd sum)"),
        ([5, 2, 2, 2, 1], "Not graphical (degree too large)"),
        ([0, 0, 0, 0], "Empty graph"),
        ([3, 3, 3, 3], "Complete graph K4"),
    ]

    for degrees, desc in test_cases:
        result = havel_hakimi_graph(degrees)
        print(f"{desc}: degrees={degrees}")
        print(f"  Result: {result}\n")


if __name__ == "__main__":
    main()