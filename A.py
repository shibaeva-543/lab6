N = int(input())
A = list(map(int, input().split()))
for i in range (0, N - 1):
	for j in range (i + 1, N):
		if A[i] == A [j]:
			print (A[i])
			break
		else:
			i+=1
	
