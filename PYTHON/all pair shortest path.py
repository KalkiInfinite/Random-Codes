import numpy as np

def all_pairs_shortest_path(graph):
    n = len(graph)
    dist = np.copy(graph)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

def generate_random_graph(num_vertices):

    graph = np.random.randint(1, 101, size=(num_vertices, num_vertices))
    np.fill_diagonal(graph, 0)
    return graph

def main():
    num_vertices = int(input("Enter the number of vertices in the graph: "))

    graph = generate_random_graph(num_vertices)

    print("\nRandom matrix with diagonal elements as zero:")
    print(graph)

    result = all_pairs_shortest_path(graph)

    print("\nShortest paths between all pairs:")
    print(result)

if __name__ == "__main__":
    main()