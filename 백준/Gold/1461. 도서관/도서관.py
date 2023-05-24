N, M = map(int, input().split())
books = sorted(list(map(int, input().split())) + [0])

pivot = 0
for i in range(N + 1):
    if not books[i]:
        pivot = i
        break

answer = 0
for i in range(0, pivot, M):
    answer += abs(books[i] * 2)

for i in range(N, pivot, -M):
    answer += books[i] * 2

answer -= max(abs(books[0]), abs(books[N]))
print(answer)