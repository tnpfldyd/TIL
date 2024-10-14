N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)
score = 0

for i in range(N):
    for j in range(N):
        if A[i] > B[j] != 0:
            score += 2
            A[i] = 0
            B[j] = 0
            break

for i in range(N):
    if A[i] == 0:
        continue
    for j in range(N):
        if A[i] == B[j] != 0:
            score += 1
            B[j] = 0
            break

print(score)