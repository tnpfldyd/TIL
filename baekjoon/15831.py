import sys
input = sys.stdin.readline

N, B, W = map(int, input().split())
load = input().rstrip()
left = wc = bc = answer = 0
for right in range(N):
    if load[right] == 'W':
        wc += 1
    else:
        bc += 1
    while bc > B:
        if load[left] == 'W':
            wc -= 1
        else:
            bc -= 1
        left += 1
    if wc >= W and bc <= B:
        answer = max(answer, right - left + 1)
print(answer)