import sys, bisect
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    input()
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    answer = 0
    for a in A:
        answer += bisect.bisect_left(B, a)
    print(answer)