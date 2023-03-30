N = int(input())
K, d = 0, 1
while d < N:
    K += 1
    d *= 2

choices = [[] for _ in range(K)]

for i in range(1, N + 1):
    k = i
    for j in range(K):
        if k & 1:
            choices[j].append(i)
        k >>= 1
print(K)
for i in range(K):
    print(len(choices[i]), end=' ')
    for j in choices[i]:
        print(j, end=' ')
    print()
