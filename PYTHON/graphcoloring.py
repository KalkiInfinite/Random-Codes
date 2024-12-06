import random

def generate_random_matrix(n):
    return [[random.choice([True, False]) for _ in range(n)] for _ in range(n)]

MAX_VERTICES = 100
color = [0] * MAX_VERTICES

def isSafe(v, n, col, G):
    for i in range(n):
        if G[v][i] and col == color[i]:
            return False
    return True

def graphColoringUtil(n, m, v, G):
    if v == n:
        return True

    for col in range(1, m + 1):
        if isSafe(v, n, col, G):
            color[v] = col
            if graphColoringUtil(n, m, v + 1, G):
                return True
            color[v] = 0

    return False

def printSolution(n):
    print("Solution Exists: Following are the assigned colors")
    for i in range(n):
        print(f"Node {i}: Color {color[i]}")

def graphColoring(n, m, G):
    for i in range(MAX_VERTICES):
        color[i] = 0

    if not graphColoringUtil(n, m, 0, G):
        print("Solution does not exist")
        return False

    printSolution(n)
    return True

if __name__ == "__main__":
    n = int(input("Enter the number of vertices: "))
    m = int(input("Enter the number of colors: "))

    G = generate_random_matrix(n)

    if not graphColoring(n, m, G):
        print("No solution exists")
import random

def generate_random_matrix(n):
    return [[random.choice([True, False]) for _ in range(n)] for _ in range(n)]

MAX_VERTICES = 100
color = [0] * MAX_VERTICES

def isSafe(v, n, col, G):
    for i in range(n):
        if G[v][i] and col == color[i]:
            return False
    return True

def graphColoringUtil(n, m, v, G):
    if v == n:
        return True

    for col in range(1, m + 1):
        if isSafe(v, n, col, G):
            color[v] = col
            if graphColoringUtil(n, m, v + 1, G):
                return True
            color[v] = 0

    return False

def printSolution(n):
    print("Solution Exists: Following are the assigned colors")
    for i in range(n):
        print(f"Node {i}: Color {color[i]}")

def graphColoring(n, m, G):
    for i in range(MAX_VERTICES):
        color[i] = 0

    if not graphColoringUtil(n, m, 0, G):
        print("Solution does not exist")
        return False

    printSolution(n)
    return True

if __name__ == "__main__":
    n = int(input("Enter the number of vertices: "))
    m = int(input("Enter the number of colors: "))

    G = generate_random_matrix(n)

    if not graphColoring(n, m, G):
        print("No solution exists")
