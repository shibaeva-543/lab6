import math

N = int(input())
A = list(map(int, input().split()))

for i in range (0, N - 1):
	for j in range (i + 1, N):
		if A[i] > 0:
			i += 1
		else:
			if A[i] < A [j] and abs(A[i]) == abs(A[j]):
	
