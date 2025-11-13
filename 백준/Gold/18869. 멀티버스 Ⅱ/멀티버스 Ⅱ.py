import sys
input = sys.stdin.readline

M, N = map(int, input().split())
pattern_counts = {}

for _ in range(M):
    arr = list(map(int, input().split()))
    uniq = sorted(set(arr))
    rank = {v: i for i, v in enumerate(uniq)}  # 0-based rank
    seq = tuple(rank[v] for v in arr)
    pattern_counts[seq] = pattern_counts.get(seq, 0) + 1

ans = 0
for cnt in pattern_counts.values():
    ans += cnt * (cnt - 1) // 2

print(ans)