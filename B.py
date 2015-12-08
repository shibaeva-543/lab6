N = int(input())
P = list(map(int, input().split()))
k = []*N

for i in range (0, N):
	if P[i] == 5:
		k[i] +=1
	else:
		k[i] -= (P[i] - 5)/5
	i += 1
