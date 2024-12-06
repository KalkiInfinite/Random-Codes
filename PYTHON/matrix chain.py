import sys
import random
n= int(input("Enter size of an array : "))
ranarr= [random.randint(1,50) for _ in range(n)]
ranarr.sort()
print ("Randomly generated array",ranarr)

def MatrixChain(p, i, j):
	if i == j:
		return 0
	min = sys.maxsize

	for k in range(i, j):
		count = (MatrixChain(p, i, k) + MatrixChain(p, k + 1, j) + p[i-1] * p[k] * p[j])
		if count < min:
			min = count
	return min

if __name__ == '__main__':

	N = len(ranarr)
	
	print("Minimum number of multiplications is ",MatrixChain(ranarr, 1, N-1))