def kruskals_algorithm(graph):
    sorted_edges = []
    for vertex in graph:
        for edge in graph[vertex]:
            sorted_edges.append((edge[0], vertex, edge[1]))
    sorted_edges.sort()
    print(*sorted_edges, sep="\n")

    parent = {}
    minimum_spanning_tree = []

    def find_parent(vertex):
        if parent[vertex] != vertex:
            parent[vertex] = find_parent(parent[vertex])
        return parent[vertex]

    for vertex in graph:
        parent[vertex] = vertex

    for edge in sorted_edges:
        weight, source, destination = edge
        if find_parent(source) != find_parent(destination):
            minimum_spanning_tree.append(edge)
            parent[find_parent(source)] = find_parent(destination)

    return minimum_spanning_tree

# graph = {
#     "A": [(1, "B"), (3, "E")],
#     "B": [(1, "A"), (2, "E"), (1, "D"), (4, "C")],
#     "C": [(4, "B"), (1, "D")],
#     "D": [(1, "B"), (2, "E"), (1, "C")],
#     "E": [(3, "A"), (2, "B"), (2, "D")]
# }
graph = {
    "A": [(7,"B"), (9, "C"), (14,"F")],
    "B": [(7,"A"), (15, "D"), (10, "C")],
    "C": [(9,"A"), (10, "B"), (11, "D"), (2,"F")],
    "D": [(15, "B"), (6, "E"), (11, "C")],
    "E": [(9, "F"), (6, "D")],
    "F": [(14, "A"),(2, "C"),(9, "E")]
}
minimum_spanning_tree = kruskals_algorithm(graph)
print(minimum_spanning_tree)

# graph = {
#     "A": [(28, "B"), (10, "F")],
#     "B": [(28, "A"), (14, "G"), (16, "C")],
#     "C": [(16, "B"), (12, "D")],
#     "D": [(22, "E"), (18, "G"), (12, "C")],
#     "E": [(25, "F"), (24, "G"), (22, "D")],
#     "F": [(10, "A"), (25, "E")],
#     "G": [(14, "B"), (18, "D"), (24, "E")]
# }
