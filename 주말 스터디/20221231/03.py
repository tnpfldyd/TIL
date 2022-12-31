import itertools
T = int(input())
for i in range(1, T+1):
    j, limit = map(int, input().split())
    temp = []
    for k in range(j):
        a, b = map(int, input().split())
        temp.append((a, b))
    answer = 0
    for k in range(1, j+1):
        for item in itertools.combinations(temp, k):
            cnt = 0
            wofy = 0
            for l in item:
                cnt += l[1]
                wofy += l[0]
            if cnt <= limit:
                answer = max(answer, wofy)
    print(f'#{i} {answer}')