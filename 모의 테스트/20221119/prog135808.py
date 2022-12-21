k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
score.sort(reverse=True)
cnt = 0
result = 0
for i in score:
    cnt += 1
    if cnt == m:
        result += m*i
        cnt = 0
print(result)