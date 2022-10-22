from heapq import heappop, heappush
import itertools

t = int(input())
h = list(map(int, input().split()))
start = []
cont = 0
if t == 3:
    while h[0] > 23 and h[1] > 23 and h[2] > 23:
        h[0] -= 13
        h[1] -= 13
        h[2] -= 13
        cont += 3
while len(h) < 3:
    h.append(0)
heappush(start, [cont, h, t])
q = [0, 1, 2]
prev = []
prev2 = [[0, 1], [1, 0]]
for i in itertools.permutations(q, 3):
    prev.append(i)
while start:
    cnt, heal, cntt = heappop(start)
    if heal[0] <= 0 and heal[1] <= 0 and heal[2] <= 0:
        print(cnt)
        break
    if cntt == 3:
        for i in prev:
            temp = []
            cnttt = 0
            temp0 = heal[i[0]] - 9
            temp1 = heal[i[1]] - 3
            temp2 = heal[i[2]] - 1
            if temp0 > 0:
                cnttt += 1
            if temp1 > 0:
                cnttt += 1
            if temp2 > 0:
                cnttt += 1
            temp.append(temp0)
            temp.append(temp1)
            temp.append(temp2)
            temp.sort(reverse=True)
            heappush(start, [cnt + 1, temp, cnttt])
    if cntt == 2:
        for i in prev2:
            temp = []
            cnttt = 0
            temp0 = heal[i[0]] - 9
            temp1 = heal[i[1]] - 3
            if temp0 > 0:
                cnttt += 1
            if temp1 > 0:
                cnttt += 1
            temp.append(temp0)
            temp.append(temp1)
            temp.append(0)
            temp.sort(reverse=True)
            heappush(start, [cnt + 1, temp, cnttt])
    if cntt == 1:
        temp = []
        temp0 = heal[0] - 9
        temp.append(temp0)
        temp.append(0)
        temp.append(0)
        heappush(start, [cnt + 1, temp, 1])
