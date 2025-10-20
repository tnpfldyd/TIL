import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dolls = list(map(int, input().split()))

left = 0
ryan_count = 0
min_length = N + 1

for right in range(N):
    if dolls[right] == 1:
        ryan_count += 1
    
    while ryan_count >= K:
        min_length = min(min_length, right - left + 1)
        if dolls[left] == 1:
            ryan_count -= 1
        left += 1

if min_length == N + 1:
    print(-1)
else:
    print(min_length)