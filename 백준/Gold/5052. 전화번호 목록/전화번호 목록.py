import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    string = sorted([input().strip() for _ in range(N)])
    flag = True
    for i in range(N - 1):
        cur, nxt = string[i], string[i + 1]
        if len(cur) > len(nxt):
            continue
        if cur == nxt[:len(cur)]:
            flag = False
            break
    print('YES' if flag else 'NO')