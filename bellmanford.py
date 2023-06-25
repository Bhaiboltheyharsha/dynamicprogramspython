def bellman(graph, source, n):
    distance = {}
    for vertex in graph:
        distance[vertex] = 999999
    distance[source] = 0
    for _ in range(n-1):
        for vertex in graph:
            for weight, neighbour in graph[vertex]:
                current_cost = distance[vertex] + weight
                if current_cost < distance[neighbour]:
                    distance[neighbour] = current_cost
    for vertex in graph:
        for weight, neighbour in graph[vertex]:
            current_cost = distance[vertex] + weight
            if current_cost < distance[neighbour]:
                print("graph has negative weight cycle")
                raise ValueError("negative weight cycle found")

    return distance

graph = {
    'A': {(6, 'B'), (5, 'C'), (5, "D")},
    'B': {(-1, 'F')},
    'C': {(-2, 'B'), (1, 'F')},
    'D': {(-1, 'E'), (-2, "C")},
    'E': {(3, 'G')},
    'F': {(3, "G")},
    'G': []
}
source = "A"
n = len(graph.keys())-1
ans = bellman(graph, source, n)
print(ans)