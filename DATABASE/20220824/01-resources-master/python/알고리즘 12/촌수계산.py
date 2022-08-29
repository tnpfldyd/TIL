# https://www.acmicpc.net/problem/2644
import sys


def pprint(arr):
    for i in range(len(arr)):
        print(i, arr[i])


sys.stdin = open("_촌수계산.txt")

n = int(input())
start, end = list(map(int, input().split()))

m = int(input())

# 빈 리스트를 (n+1)개를 가진 이차원 리스트
# _ : 값을 사용하지않겠다는 의미
graph = [[] for _ in range(0, n + 1)]

for _ in range(m):
    # 공백을 기준으로 2개의 숫자가 입력되기 떄문에
    x, y = list(map(int, input().split()))

    # 무방향 인접 그래프라서
    graph[x].append(y)
    graph[y].append(x)

# 방문 표시를 할 리스트
visited = [False] * (n + 1)

# dfs를 시작하기위해서 기본값 설정
# 스택에 값을 추가할 때 촌수도 같이 추가한다.
# stack = [start]
stack = []
stack.append((start, 0))
visited[start] = True

# 장답을 출력할 변수
answer = -1

# 스택이 비어있지 않으면 반복
while len(stack) != 0:
    # LIFO, 스택의 가장 위에 있는 값을 저장
    # 번호와 촌수를 같이 pop
    number, count = stack.pop()

    # pop을 한 값이 우리가 원하는 값(end)
    # 촌수가 연결이 안되어있으면 line50~line52 실행 X
    if number == end:
        answer = count
        break

    # 해당하는 값의 인접 그래프를 저장
    adj_graph = graph[number]

    # print(number, adj_graph)

    # 인접하는 값들을 탐색
    for adj_number in adj_graph:
        # 방문한적이 없을 때만 스택에 값을 append
        if not visited[adj_number]:
            # 인접 번호와 촌수 + 1를 같이 append
            stack.append((adj_number, count + 1))
            # 인접 값을 방문 표시
            visited[adj_number] = True

# 그래서 촌수는 어떻게 계산을 해야될까?
# 촌수 출력
print(answer)
