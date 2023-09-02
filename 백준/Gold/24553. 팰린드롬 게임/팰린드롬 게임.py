import sys
input = sys.stdin.readline
[print(1 if not (int(input())) % 10 else 0) for _ in range(int(input()))]