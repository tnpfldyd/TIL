N = int(input())
result = [[] for _ in range(11)]
cnt = 0
for i in range(N):
    num, load = map(int, input().split())
    if result[num] == []:
        result[num] = load
    elif result[num] != load:
        result[num] = load
        cnt += 1
print(cnt)