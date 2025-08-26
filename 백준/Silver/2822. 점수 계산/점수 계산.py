import sys
input = sys.stdin.readline

scores = []
for i in range(8):
    score = int(input())
    scores.append((score, i + 1))

scores.sort(reverse=True)
total = sum(scores[i][0] for i in range(5))
problems = sorted([scores[i][1] for i in range(5)])

print(total)
print(*problems)