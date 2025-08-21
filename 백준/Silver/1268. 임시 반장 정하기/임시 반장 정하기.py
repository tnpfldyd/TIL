import sys
input = sys.stdin.readline

n = int(input())
students = [list(map(int, input().split())) for _ in range(n)]

same_class_count = [0] * n

for i in range(n):
    for j in range(n):
        if i != j:
            for grade in range(5):
                if students[i][grade] == students[j][grade]:
                    same_class_count[i] += 1
                    break

max_count = max(same_class_count)
for i in range(n):
    if same_class_count[i] == max_count:
        print(i + 1)
        break