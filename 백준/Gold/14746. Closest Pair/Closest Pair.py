import sys
input = sys.stdin.readline
INF = sys.maxsize

def main():
    N, M = map(int, input().split())
    c1, c2 = map(int, input().split())
    P = sorted(list(map(int, input().split())))
    Q = sorted(list(map(int, input().split())))
    right = cnt = 0
    answer = INF
    
    for left in range(N):
        while right < M and P[left] >= Q[right]:
            cur = abs(P[left] - Q[right])
            if answer > cur:
                answer = cur
                cnt = 1
            elif answer == cur:
                cnt += 1
            right += 1
        if right < M and P[left] < Q[right]:
            cur = abs(P[left] - Q[right])
            if answer > cur:
                answer = cur
                cnt = 1
            elif answer == cur:
                cnt += 1
    print(answer + abs(c1 - c2), cnt)

if __name__ == '__main__':
    main()