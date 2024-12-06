def lcs_length(X, Y, m, n):
    c = [[0] * (n + 1) for _ in range(m + 1)]
    b = [[""] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "≈"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "↑"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "←"
    return c, b

def print_lcs(b, X, i, j):
    if i == 0 or j == 0:
        return ""
    if b[i][j] == "≈":
        return print_lcs(b, X, i - 1, j - 1) + X[i - 1]
    elif b[i][j] == "↑":
        return print_lcs(b, X, i - 1, j)
    else:
        return print_lcs(b, X, i, j - 1)

def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)
    c, b = lcs_length(X, Y, m, n)
    return print_lcs(b, X, m, n)

X = input("\nEnter the first string: ")
Y = input("Enter the second string: ")
result = longest_common_subsequence(X, Y)
print("Longest Common Subsequence:", result)
