
def prims(graph, start):
    weights = {}
    for key in graph.keys():
        weights[key] = 9999999
    weights[start] = 0
    parents = {}
    bag = [start]
    visited = []
    while len(bag) != 0:
        ele = bag.pop(0)
        for w, node in graph[ele]:
            if node not in visited and w < weights[node]:
                weights[node] = w
                parents[node] = ele
                if node not in bag:
                    bag.append(node)

        visited.append(ele)
    return [parents,weights]

graph = {
    "A": [(1,"B"), (3, "E")],
    "B": [(1,"A"),(2, "E"), (1, "D"), (4, "C")],
    "C": [(4, "B"), (1, "D")],
    "D": [(1, "B"), (2, "E"), (1, "C")],
    "E": [(3, "A"), (2, "B"), (2, "D")]
}
mst = prims(graph, "A")
print(mst)