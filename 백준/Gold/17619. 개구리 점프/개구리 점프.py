import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
points = sorted([list(map(int, input().split())) + [i] for i in range(N)])

result = [i for i in range(N)]

end, idx = points[0][1], points[0][3]

for i in range(1, N):
    if end >= points[i][0]:
        end = max(end, points[i][1])
        result[points[i][3]] = idx
    else:
        end, idx = points[i][1], points[i][3]
        
for _ in range(Q):
    x, y = map(int, input().split())
    print(1 if result[x - 1] == result[y - 1] else 0)