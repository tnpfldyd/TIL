import sys
input = sys.stdin.readline

N = int(input())

meeting = []
for _ in range(N):
    a, b = map(int, input().split())
    meeting.append((a, b))

meeting.sort(key=lambda x: (x[1], x[0]))

result = []
for start, end in meeting:
    if result:
        if result[-1][1] <= start:
            result.append((start, end))
    else:
        result.append((start, end))
print(len(result))