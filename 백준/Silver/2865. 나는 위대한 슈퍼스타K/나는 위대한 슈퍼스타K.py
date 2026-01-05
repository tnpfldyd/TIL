import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

best = [0.0] * N

for _ in range(M):
    data = input().split()
    for i in range(0, len(data), 2):
        idx = int(data[i]) - 1
        score = float(data[i + 1])
        best[idx] = max(best[idx], score)

best.sort(reverse=True)

answer = sum(best[:K])
print(f"{answer:.1f}")