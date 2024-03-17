import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    s = input().strip()
    n = len(s)
    prev = '0'
    answer = 0
    for i in range(n):
        if s[i] != prev:
            answer += 1 << (n - i - 1)
        prev = '1' if prev != s[i] else '0'
    print(answer)