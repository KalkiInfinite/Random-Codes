from queue import PriorityQueue

class State:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def successors(self, x_capacity, y_capacity):
        successors = []
        successors.append(State(x_capacity, self.y, self))
        successors.append(State(self.x, y_capacity, self))
        successors.append(State(0, self.y, self))
        successors.append(State(self.x, 0, self))
        pour_amount = min(self.x, y_capacity - self.y)
        successors.append(State(self.x - pour_amount, self.y + pour_amount, self))
        pour_amount = min(self.y, x_capacity - self.x)
        successors.append(State(self.x + pour_amount, self.y - pour_amount, self))
        return successors

def manhattan_distance(state, target):
    return abs(state.x - target) + abs(state.y - target)

def astar_search(x_capacity, y_capacity, target):
    start_state = State(0, 0)
    visited = set()
    frontier = PriorityQueue()
    frontier.put((0, start_state))  # (priority, state)
    while not frontier.empty():
        current_cost, current_state = frontier.get()
        if current_state in visited:
            continue
        visited.add(current_state)
        if current_state.x == target or current_state.y == target:
            return current_state
        for successor in current_state.successors(x_capacity, y_capacity):
            if successor not in visited:
                cost = current_cost + 1
                priority = cost + manhattan_distance(successor, target)
                frontier.put((priority, successor))
    return None

def main():
    x_capacity = 4
    y_capacity = 3
    target = 2
    solution = astar_search(x_capacity, y_capacity, target)
    if solution:
        print("Solution found:")
        path = []
        while solution:
            path.append(solution)
            solution = solution.parent
        path.reverse()
        for state in path:
            print(state)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
