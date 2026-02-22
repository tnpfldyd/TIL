from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
name_call = defaultdict(int)

for _ in range(N):
    name = input().strip()
    name_call[name] += 1

result = sorted(name_call.items(), key=lambda x: (x[1], x[0]), reverse=True)

print(*result[0])