import sys
input = sys.stdin.readline

N, I = map(int, input().split())
handles = [input().strip() for _ in range(N)]

handles.sort()
print(handles[I - 1])