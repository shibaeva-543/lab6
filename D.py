ch = list(map(int, input().split()))
M = list(map(int, input().split()))
k = ch[0]
n = ch[1]

for i in range (0, k - 1):
	A = list(map(int, input().split()))
	for j in range (0, n):
		if A[j] < M[j]:
			M[j] = A[j]
			j += 1
	i +=1
			
print(M)
