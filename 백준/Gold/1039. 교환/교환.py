from collections import deque
N, K = map(int, input().split())

start = deque()
visit = set()
start.append((N, 0))
answer = -1
while start:
    x, k = start.popleft()
    if k == K:
        if answer < x:
            answer = x
        continue
    temp = list(str(x))
    if len(temp) < 2:
        continue
    for i in temp:
        idx = temp.index(i)
        for j in range(len(temp)):
            if j != idx:
                temp2 = temp[:]
                temp2[j] = i
                temp2[idx] = temp[j]
                if temp2[0] != '0':
                    temp2 = int(''.join(temp2))
                    if (temp2, k+1) not in visit:
                        visit.add((temp2, k+1))
                        start.append((temp2, k+1))
print(answer)