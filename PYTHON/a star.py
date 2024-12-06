from queue import PriorityQueue

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {v: [] for v in range(vertices)}

    def add_edge(self, src, dest, weight):
        self.adjacency_list[src].append((dest, weight))
        self.adjacency_list[dest].append((src, weight))

    def astar_search(self, start, goal, heuristic):
        visited = [False] * self.vertices
        pq = PriorityQueue()
        pq.put((0, start))
        total_cost = 0
        while not pq.empty():
            cost, current_node = pq.get()
            total_cost += cost
            print(current_node, end=' ')
            if current_node == goal:
                print(f"\nGoal found! Total cost: {total_cost}")
                return True
            visited[current_node] = True
            for neighbor, weight in self.adjacency_list[current_node]:
                if not visited[neighbor]:
                    priority = weight + heuristic[neighbor]
                    pq.put((priority, neighbor))
        print("\nGoal not found!")
        return False

if __name__ == "__main__":
    graph = Graph(8)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 2)
    graph.add_edge(1, 3, 5)
    graph.add_edge(1, 4, 10)
    graph.add_edge(2, 5, 3)
    graph.add_edge(2, 6, 7)
    graph.add_edge(3, 7, 2)
    graph.add_edge(4, 7, 4)
    graph.add_edge(5, 7, 1)
    graph.add_edge(6, 7, 9)
    start_node = 1
    goal_node = 7
    heuristic = [14, 10, 7, 3, 3, 2, 1, 0]
    print("A* Search: ")
    graph.astar_search(start_node, goal_node, heuristic)
