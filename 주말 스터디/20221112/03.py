reference = 'vxrvip'
track = 'xrviprvipvxrv'
from heapq import heappop,heappush
refer_list = set()
for i in range(len(reference)):
    for j in range(1, len(reference)):
        if not reference[i:j+1]:
            continue
        refer_list.add(reference[i:j+1])
start = []
visited = set()
print(refer_list)
for i in refer_list:
    if i == track[:len(i)]:
        heappush(start, [-len(i), i])
        visited.add((-len(i), i))
while start:
    cnt, text = heappop(start)
    if text == track:
        print(-cnt)
        break
    for i in refer_list:
        if text+i == track[:len(text+i)] and (max(cnt, -len(i)), text+i) not in visited:
            visited.add((max(cnt, -len(i)), text+i))
            heappush(start, [max(cnt, -len(i)), text+i])