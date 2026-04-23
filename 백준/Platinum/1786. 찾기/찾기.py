import sys
input = sys.stdin.readline

T = input().rstrip('\n')
P = input().rstrip('\n')

n = len(T)
m = len(P)

pi = [0] * m

j = 0
for i in range(1, m):
    while j > 0 and P[i] != P[j]:
        j = pi[j - 1]

    if P[i] == P[j]:
        j += 1
        pi[i] = j

result = []

j = 0
for i in range(n):
    while j > 0 and T[i] != P[j]:
        j = pi[j - 1]

    if T[i] == P[j]:
        if j == m - 1:
            result.append(i - m + 2)
            j = pi[j]
        else:
            j += 1

print(len(result))
print(*result)