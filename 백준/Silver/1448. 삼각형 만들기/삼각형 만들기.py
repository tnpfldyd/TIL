import sys
input = sys.stdin.readline

lines = sorted((int(input()) for _ in range(int(input()))), reverse=True)

for i in range(len(lines) - 2):
    if lines[i] < lines[i+1] + lines[i+2]:
        print(lines[i] + lines[i+1] + lines[i+2])
        break
else:
    print(-1)