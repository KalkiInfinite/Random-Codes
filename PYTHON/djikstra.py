import random

def generate_random_cost(n):
   
    cost = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                cost[i][j] = random.randint(1, 10)  
    return cost

def shortest_paths(v, cost, dist, n):
    S = [False] * (n + 1)
    for i in range(1, n + 1):
        dist[i] = cost[v][i]

    S[v] = True
    dist[v] = 0.0
   
    for num in range(2, n):
        min_dist = float('inf')
        u = -1
        for i in range(1, n + 1):
            if not S[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
       
        if u == -1:
            break
       
        S[u] = True  
       
        for w in range(1, n + 1):
            if not S[w] and dist[w] > dist[u] + cost[u][w]:
                dist[w] = dist[u] + cost[u][w]


n = int(input("Enter the number of vertices: "))


cost = generate_random_cost(n)


dist = [0] * (n + 1)

shortest_paths(1, cost, dist, n)

print("Shortest distances from vertex 1:")
for i in range(1, n + 1):
    print("Vertex", i, ":", dist[i])
