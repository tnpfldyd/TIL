import sys
input = sys.stdin.readline

N, K = map(int, input().split())
makgeolli = [int(input()) for _ in range(N)]

start, end = 1, max(makgeolli)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    for m in makgeolli:
        count += m // mid
    if count >= K:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)