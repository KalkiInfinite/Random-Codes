def ids(graph, start, goal):
    depth_limit = 0
    while True:
        result = dls(graph, start, goal, depth_limit)
        if result is not None:
            return result
        depth_limit += 1

def dls(graph, start, goal, depth_limit):
    return recursive_dls(graph, start, goal, depth_limit, [start])

def recursive_dls(graph, node, goal, depth_limit, path):
    if node == goal:
        return path
    if depth_limit == 0:
        return None
    if node not in graph:
        return None
    for neighbor in graph[node]:
        result = recursive_dls(graph, neighbor, goal, depth_limit - 1, path + [neighbor])
        if result is not None:
            return result
    return None

romania_map = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

start_city = input("Enter the start city: ")
goal_city = input("Enter the goal city: ")
path = ids(romania_map, start_city, goal_city)
if path:
    print("Path found:", '->'.join(path))
else:
    print("Path not found.")
