def NQueens(k, n, x):
    for i in range(1, n+1):
        if Place(k, i, x):
            x[k] = i
            if k == n:
                print(x[1:])
            else:
                NQueens(k+1, n, x)

def Place(k, i, x):
    for j in range(1, k):
        if x[j] == i or abs(x[j] - i) == abs(j - k):
            return False
    return True

n = int(input("Enter the value of n for an n x n chessboard: "))
x = [0] * (n+1)  
NQueens(1, n, x)