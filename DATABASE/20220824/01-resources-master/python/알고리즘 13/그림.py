# https://www.acmicpc.net/problem/1926
import sys

sys.stdin = open("_그림.txt")

"""
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
"""

def pprint(arr):
    for i in range(len(arr)):
        print(arr[i])

# 상하좌우를 탐색하기 위한 델타 리스트
dy = [-1,0,1,0]
dx = [0,1,0,-1]

# 가로 세로의 크기를 입력
# 두 숫자가 공백으로 구분
n,m = list(map(int,input().split()))

# 이차원 그래프를 생성
# 빈 그래프 생성
graph = []

# n번 만큼 일차원 그래프를 입력 & 추가
for _ in range(n):
    graph_list = list(map(int,input().split()))
    graph.append(graph_list)

# 방문 표시 이차원 그래프
visited = []

# n번 만큼 일차원 그래프를 추가
for _ in range(n):
    # boolean(False) 가 m개인 일차원 그래프?
    visited_list = [False] * m
    visited.append(visited_list)

painting_count = 0
painting_size_list = []

# 모든 좌표에서 DFS 로직 실행
# 이차원 리스트를 순회할 이중 반복문
for sy in range(n):
    for sx in range(m):
        # [y,x] 값이 1이고, 방문하지 않았다면
        # DFS 실행
        if not visited[sy][sx] and graph[sy][sx] == 1: 
            stack = []
            # 시작점을 stack append
            stack.append([sy,sx])
            # 시작점을 방문처리
            visited[sy][sx] = True

            # 그림의 개수 + 1
            painting_count += 1

            # 그림의 넓이?
            painting_size = 0

            # DFS
            # 스택이 비어있지않으면 반복한다.
            # while stack:
            while len(stack) != 0:
                # y,x 값이 갱신
                y, x = stack.pop()

                # 그림의 넓이
                painting_size += 1

                # 델타 탐색을 시행 
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    
                    # 조건 1, 2, 3
                    # 조건 1. 범위 조건
                    if not (-1< ny < n and -1 < nx < m):
                        continue

                    # 조건 2. 방문 확인
                    # 방문을 했던 좌표라면
                    if visited[ny][nx] == True:
                        continue

                    # 조건 3. 좌표의 값이 1
                    # 그림이여야한다
                    if graph[ny][nx] != 1:
                        continue
                        
                    # 조건을 다 통과하면
                    # stack 다음 좌표 넣고,
                    # 방문 처리
                    stack.append((ny,nx))
                    visited[ny][nx] = True

            painting_size_list.append(painting_size)


# 그림의 개수
# 그림의 가장 큰 넓이
if len(painting_size_list) != 0:
    print(painting_count)
    print(max(painting_size_list))
else:
    print(0)
<<<<<<< HEAD
    print(0)
=======
    print(0)
>>>>>>> c9ef8f9c07039487883c1659107900a1b39f5385
