import random
n= int(input("Enter size of an array : "))
ranarr= [random.randint(1,50) for _ in range(n)]
ranarr.sort()
print ("Randomly generated array",ranarr)

def matrix_chain_order(ranarr):
    n = len(ranarr) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n)]

    for i in range(1, n + 1):
        m[i][i] = 0

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + ranarr[i - 1] * ranarr[k] * ranarr[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print("A" + str(i), end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")

def print_solution(m, s, ranarr):
    n = len(ranarr) - 1
    print("Minimum number of multiplications:", m[1][n])
    print("Optimal Parenthesization:", end=" ")
    print_optimal_parens(s, 1, n)
    print("\nIntermediate results:")
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            print(f"m[{i}][{j}] =", m[i][j])
    print("")

m, s = matrix_chain_order(ranarr)
print_solution(m, s, ranarr)