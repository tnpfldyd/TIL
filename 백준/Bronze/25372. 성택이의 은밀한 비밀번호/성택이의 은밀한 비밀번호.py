import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = len(input().strip())
    print('yes' if s > 5 and s < 10 else 'no')