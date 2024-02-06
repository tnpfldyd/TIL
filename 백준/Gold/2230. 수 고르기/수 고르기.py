import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
numbers = sorted([int(input()) for _ in range(N)])

left = right = 0
answer = INF
while left < N and right < N:
    temp = numbers[right] - numbers[left]
    if M < temp:
        answer = min(answer, temp)
        left += 1
    elif M == temp:
        print(M)
        break
    else:
        right += 1
else:
    print(answer)