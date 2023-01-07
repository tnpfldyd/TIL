import sys, bisect
input = sys.stdin.readline
N, M = map(int, input().split())
T = int(input())
cats = []
for _ in range(T):
    a, b = map(int, input().split())
    if a <= N and b <= M:
        cats.append((a, b))
cats.sort()
result = []
for a, b in cats:
    if result:
        if result[-1] <= b:
            result.append(b)
        else:
            idx = bisect.bisect_right(result, b)
            result[idx] = b
    else:
        result.append((b))
print(len(result))