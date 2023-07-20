def dfs(idx):
    if not children[idx]:
        return 0

    answer = []
    for i in range(len(children[idx])):
        answer.append(dfs(children[idx][i]))

    answer.sort(reverse=True)

    ret = 0
    for i in range(len(answer)):
        ret = max(ret, answer[i] + (i+1))

    return ret


N = int(input())
numbers = list(map(int, input().split()))
children = [[] for _ in range(N+1)]

for i in range(N):
    parent = numbers[i]
    if not i:
        continue
    children[parent].append(i)

print(dfs(0))