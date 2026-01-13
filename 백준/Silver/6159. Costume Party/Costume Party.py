import sys
input = sys.stdin.readline

N, S = map(int, input().split())
L = [int(input()) for _ in range(N)]

L.sort()

left = 0
right = N - 1
answer = 0

while left < right:
    if L[left] + L[right] <= S:
        answer += (right - left)
        left += 1
    else:
        right -= 1

print(answer)