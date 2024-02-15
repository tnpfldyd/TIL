import sys
input = sys.stdin.readline

N, K = map(int, input().split())

cal = 0
s = 1

numbers = list(map(int, input().split()))

for i in range(1, N + 1):
    t = numbers[i - 1]
    if (t | K) != K:
        cal = 0
        s = i + 1
    else:
        cal |= t
        if cal == K:
            print(s, i)
            break
else:
    print(-1)