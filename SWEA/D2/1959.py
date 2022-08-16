import sys
sys.stdin = open("1959input.txt", "r")
T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    result = [[] for _ in range(abs(N-M) + 1)]
    if N > M:
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
    else:
        b = list(map(int, input().split()))
        a = list(map(int, input().split()))
    for j in range(abs(N - M) + 1):
        for k in range(min(N, M)):
            result[j].append(b[k]* a[k + j])
    print(f'#{i} {max(map(sum, result))}')
