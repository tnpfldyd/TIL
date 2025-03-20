import sys
input = sys.stdin.readline
N, game = input().split()
N = int(N)
names = [input().rstrip() for _ in range(N)]
M = len(set(names))
K = {'Y': 1, 'F': 2, 'O': 3}[game]
result = M // K
print(result)