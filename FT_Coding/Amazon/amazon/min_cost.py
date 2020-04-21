def minCostIncurred(numTotalEdgeNodes, numTotalAvailableNetworkRoutes, networkRoutesAvailable, numNewNetworkRoutesConstruct, costNewNetworkRoutesConstruct):
    num_nodes = numTotalEdgeNodes
    edges = networkRoutesAvailable # 1,2
    new_edges_with_cost = costNewNetworkRoutesConstruct # 1,2, 5
    graph = make_graph(edges, num_nodes)
    # new_edges_with_cost_sorted = new_edges_with_cost.sort(key=lambda x: x[2])
    # print new_edges_with_cost_sorted
    total_min = 0
    for value_list in graph.values():
        current_conn = []
        groups_connected = []
        current_min = 9999
        for cost_list in new_edges_with_cost:
            fgl = set([y for x in groups_connected for y in x])
            intersect = set(cost_list[0:2]).intersection(set(value_list))
            if intersect is not None and fgl.intersection(intersect) is None:
                if cost_list[2] < current_min:
                    current_min = cost_list[2]
                    current_conn = cost_list[0:2]
            groups_connected.append(current_conn)
        total_min += current_min
    return total_min


def make_graph(edges, num_nodes):
    graph = {}
    for edge in edges:
        for item in graph.items():
            if edge[0] in item[1]:
                item[1].append(edge[1])

        values =  [y for x in graph.values() for y in x]
        if edge[0] not in graph.keys() and edge[0] not in values:
            if edge[0] == 4:
                print(graph.values())
            graph[edge[0]] = [edge[0], edge[1]]

    for node in range(1, num_nodes+1):
        if not node in graph.keys() and not node in [y for x in graph.values() for y in x]:
            graph[node] = [node]
    return graph


print minCostIncurred(6, 3, [[1,4], [4,5], [2,3]], 4, [[1,2,5],[1,3,10],[1,6,2], [5,6,5]])
