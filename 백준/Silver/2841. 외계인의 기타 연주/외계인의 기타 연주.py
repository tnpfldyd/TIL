import sys
input = sys.stdin.readline

N, P = map(int, input().split())
stack = [[] for _ in range(7)]
count = 0

for _ in range(N):
    string, fret = map(int, input().split())
    while stack[string] and stack[string][-1] > fret:
        stack[string].pop()
        count += 1
    if not stack[string] or stack[string][-1] < fret:
        stack[string].append(fret)
        count += 1

print(count)