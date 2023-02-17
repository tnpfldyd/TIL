from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
time, money = map(int, input().split())
M = int(input())
matrix = [[] for _ in range(N)]
for _ in range(M):
    a, b, t, m = map(int, input().split())
    a -= 1; b -= 1
    matrix[a].append((m, t, b))
    matrix[b].append((m, t, a))
time_visit = [INF] * N; money_visit = [INF] * N # 돈과 시간을 동시에 관리해야해서 visited 2개 생성 2중 visit으로도 가능하나 편의상 따로 만들었음.
time_visit[0] = 0; money_visit[0] = 0
start = []
heappush(start, (0, 0, 0, 0))
cnt = 0
visit = set()
while start:
    mon, x, node, check = heappop(start) # 돈, 시간, node, cnt(check용도) 순
    if check not in visit: # 둘 다 통과했을 경우 다음 들어오는 check는 건너 띄기 위함. 시간을 조금이라도 줄일려는 이유일 뿐 굳이 cnt는 안해도 괜찮음.
        visit.add(check)
    else:
        continue
    if node == N-1:
        print(mon) # 도달하면 돈 출력
        break
    for k, y, v in matrix[node]: # 돈, 시간, node 순
        nx, ny = mon+k, x+y 
        if nx <= money and ny <= time: # 둘 중에 하나라도 범위를 벗어나면 안되기에 먼저 체크
            cnt += 1
            if money_visit[v] > nx: # 둘 다 범위 안에 있고 돈이 적거나 덜 드는 시간이 있다면 힙에 push 둘 다 통과하는 경우나, 둘 중 하나만 통과하는 경우를 나눠서 관리
                money_visit[v] = nx
                heappush(start, (nx, ny, v, cnt))
            if time_visit[v] > ny:
                time_visit[v] = ny
                heappush(start, (nx, ny, v, cnt))
else:
    print(-1)