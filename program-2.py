from heapq import heappush,heappop
def dijkstras(graph,source):
    distances = {}
    for vertex in graph:
        distances[vertex] = 99999
    distances[source] = 0
    heap = []
    heappush(heap,(0,source))
    while heap:
        weight,node = heappop(heap)#(2,b)
        if weight > distances[vertex]:

            continue
        for cost,next_node in graph[node]:
            total_cost = weight + cost
            if total_cost < distances[next_node]:
                distances[next_node] = total_cost
                heappush(heap,(total_cost,next_node))
        return distances
graph = {
    "A": [(7,"B"), (9, "C"), (14,"F")],
    "B": [(7,"A"), (15, "D"), (10, "C")],
    "C": [(9,"A"), (10, "B"), (11, "D"), (2,"F")],
    "D": [(15, "B"), (6, "E"), (11, "C")],
    "E": [(9, "F"), (6, "D")],
    "F": [(14, "A"),(2, "C"),(9, "E")]
}
ans = dijkstras(graph,"A")
print(ans)