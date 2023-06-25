from heapq import heappush, heappop

def dijkstras(graph, source, dest):
    distances = {}
    for vertex in graph:
        distances[vertex] = 999999
    distances[source] = 0
    heap = []
    heappush(heap, (0, source))
    previous = {}
    while heap:
        cur_dis, cur_vert = heappop(heap)
        if cur_dis > distances[cur_vert]:
            continue
        if cur_vert == dest:
            break
        for weight, node in graph[cur_vert]:
            cost = cur_dis + weight
            if cost < distances[node]:
                distances[node] = cost
                previous[node] = cur_vert
                heappush(heap, (cost, node))
    if dest not in previous:
        return None
    path = []
    node = dest
    while node != source:
        path.insert(0, node)
        node = previous[node]
    return distances, path


graph = {
    'A': {(5, 'B'), (2, 'C')},
    'B': {(5, 'A'), (1, 'C'), (3, 'D')},
    'C': {(2, 'A'), (1, 'B'), (2, 'D')},
    'D': {(3, 'B'), (2, 'C'), (4, 'E')},
    'E': {(4, 'D')}
}
source = "A"
destination = "E"
ans = dijkstras(graph, source, destination)
print(ans)