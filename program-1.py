def fill_weight(graph):
    w = {}
    for vertex in graph:
        w[vertex] = 99999
    return w
def prims(graoh,start):
    weigth = fill_weight(graph)
    #print(weigth)
    weigth[start] = 0
    parent = {}
    bag = [start]
    visited = []
    while len(bag) != 0:
        ele = bag.pop(0)
        for w,n in graph[ele]:
            if n not in visited and w < weigth[n]:
                weigth[n] = w
                parent[n] = ele
                if n not in bag:
                    bag.append(n)
        visited.append(ele)
        mst = {}
        for key,value in parent.items():
            try:
                mst[value].append(key)
            except:
                mst[value] = [key]
        return [parent,weigth]
graph = {
    'A':[(1,"B"),(3,"E")],
    "B":[(1,"A"),(2,"E"),(1,"D"),(4,"C")],
    "C":[(4,"B"),(1,"D")],
    "D":[(1,"B"),(2,"E"),(1,"C")],
    "E":[(3,"A"),(2,"B"),(2,"D")],
}
mst = prims(graph, "A")
print(*mst,sep = '\n')
print(mst)