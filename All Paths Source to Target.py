graph = [[1, 2],
         [3],
         [3],
         []]
# graph = [[1], [3], [4], [4], [5], []]
#Output: [[0,1,3],[0,2,3]]
def traverse(graph, ptr, routes):
    if graph[ptr] == []:
        return [[ptr]]#[r+[ptr] for r in routes]
    else:
        RouteToCurrentNode = [r+[ptr] for r in routes]
        # print(RouteToCurrentNode)
        sub_routes = []
        for n in graph[ptr]:
            sub_route = traverse(graph, n, routes)
            sub_routes += sub_route
        print(sub_routes)
        route = [p+q for p in RouteToCurrentNode for q in sub_routes]
        return route
ans = traverse(graph, 0, [[]])

print(ans)