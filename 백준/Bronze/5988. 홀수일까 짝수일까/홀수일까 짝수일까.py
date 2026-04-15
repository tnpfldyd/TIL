import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    print('odd' if K % 2 else 'even')