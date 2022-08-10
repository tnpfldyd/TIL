T = int(input())
T += 1
a, b = map(int, input().split())
matrix = [[] for _ in range(T)]
R = int(input())
for i in range(R):
    num1, num2 = map(int, input().split())
    matrix[num2].append(num1)
    matrix[num1].append(num2)
start = [a]
visited = [0] * T
while start:
    chon = start.pop()
    if chon == b:
        print(visited[b])
        break
    for i in matrix[chon]:
        if visited[i] == 0:
            visited[i] = visited[chon] + 1
            start.append(i)
else:
    print(-1)