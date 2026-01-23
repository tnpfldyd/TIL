import sys
input = sys.stdin.readline

T = input().strip()
N = int(input())

need = [0] * 26
for c in T:
    need[ord(c) - ord('A')] += 1

cost = []
book_cnt = []

for _ in range(N):
    c, w = input().split()
    c = int(c)
    cnt = [0] * 26
    for ch in w:
        cnt[ord(ch) - ord('A')] += 1
    cost.append(c)
    book_cnt.append(cnt)

INF = 10**18
answer = INF

for mask in range(1, 1 << N):
    total_cost = 0
    have = [0] * 26

    for i in range(N):
        if mask & (1 << i):
            total_cost += cost[i]
            for k in range(26):
                have[k] += book_cnt[i][k]

    possible = True
    for k in range(26):
        if have[k] < need[k]:
            possible = False
            break

    if possible:
        answer = min(answer, total_cost)

print(answer if answer != INF else -1)