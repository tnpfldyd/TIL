N, a, b = map(int, input().split())
answer = []

for i in range(1, a):
    answer.append(i)
answer.append(max(a, b))
for i in range(b-1, 0, -1):
    answer.append(i)

if len(answer) > N:
    print(-1)
else:
    print(answer[0], end=" ")
    for i in range(N - len(answer)):
        print(1, end=" ")
    for i in range(1, len(answer)):
        print(answer[i], end=" ")