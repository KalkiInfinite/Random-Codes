import random

def dijkstra_shortest_paths(v, cost, dist, n):
    visited = [False] * n
    dist[v] = 0.0
    path = [[] for _ in range(n)]
    path[v] = [v] 
    
    for _ in range(n):
        u = -1
        min_dist = float('inf')
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        
        if u == -1:
            break
        
        visited[u] = True
        
        for w in range(n):
            if not visited[w] and cost[u][w] > 0 and dist[w] > dist[u] + cost[u][w]:
                dist[w] = dist[u] + cost[u][w]
                path[w] = path[u] + [w]  

    return path


n = 6
v = 0  


cost = [[0 if i == j else random.randint(1, 10) for j in range(n)] for i in range(n)]


print("Randomly generated cost matrix:")
for row in cost:
    print(row)

dist = [float('inf')] * n  
shortest_paths = dijkstra_shortest_paths(v, cost, dist, n)
min_cost_path = shortest_paths[5]  

min_cost_path_display = [node + 1 for node in min_cost_path]
dist_display = dist[5]  

print("\nShortest path from node 1 to node 6:", min_cost_path_display)
print("Minimum cost:", dist_display)
