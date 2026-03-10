import sys
input = sys.stdin.readline

N, M = map(int, input().split())
scores = list(map(int, input().split()))

best_id = 100001
best_score = -1

for _ in range(M):
    data = input().split()
    student_id = int(data[0])
    result = data[1:]

    total = 0
    for i in range(N):
        if result[i] == 'O':
            total += scores[i]

    if total > best_score or (total == best_score and student_id < best_id):
        best_score = total
        best_id = student_id

print(best_id, best_score)