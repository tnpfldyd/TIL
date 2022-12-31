import sys
sys.setrecursionlimit(10**9)
target = 50
temp = {2: '1', 3: '7', 4: '4', 5: '2,3,5', 6: '0,6,9', 7:'8'}
result = [[2],[3],[4],[5],[6],[7]]
answer = []
def dfs(cnt):
    if sum(cnt) == target:
        answer.append(cnt)
        return
    for i in result:
        if sum(cnt + i) <= target:
            dfs(cnt+i)

dfs([])
final = 0
for i in answer:
    if 5 in i or 6 in i:
        temp2 = 0
        for j in i:
            if j == 5 or j == 6:
                temp2 += 1
        final += 3 ** temp2
    else:
        final += 1
print(answer)
print(final)