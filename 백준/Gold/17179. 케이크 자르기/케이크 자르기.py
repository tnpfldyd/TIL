import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
S = [int(input()) for _ in range(M)] + [L]
Q = [int(input()) for _ in range(N)]

def get_count(mid):
    count = temp = 0
    for s in S:
        if s - temp >= mid:
            count += 1
            temp = s
    return count

for q in Q:
    l, r = 1, L
    answer = 0
    while l <= r:
        mid = (l + r) // 2
        count = get_count(mid)

        if count > q:
            l = mid + 1
            answer = mid
        else:
            r = mid - 1
    print(answer)